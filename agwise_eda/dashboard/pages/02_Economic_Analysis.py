"""
Economic Analysis: Haney vs Traditional Soil Testing
Interactive What-If Simulation Tool

Robust economic model for agronomic decision-making
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from pathlib import Path

st.set_page_config(page_title="Economic Analysis", page_icon="💰", layout="wide")

# Custom CSS
st.markdown("""
<style>
    .equation-box {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 0.5rem;
        border-left: 4px solid #2c5f2d;
        margin: 1rem 0;
        font-family: 'Courier New', monospace;
    }
    .assumption-header {
        background-color: #e8f5e9;
        padding: 0.5rem;
        border-radius: 0.3rem;
        font-weight: bold;
        margin-top: 1rem;
    }
    .metric-positive {
        color: #2e7d32;
        font-weight: bold;
    }
    .metric-negative {
        color: #c62828;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1 style='color: #2c5f2d;'>💰 Economic Analysis: Soil Testing ROI</h1>", unsafe_allow_html=True)
st.markdown("### Interactive What-If Simulation for Haney vs Traditional Testing")

# Load data
@st.cache_data
def load_data():
    data_file = Path(__file__).parent.parent.parent / 'data' / 'processed' / 'combined_soil_data_FULL.csv'
    df = pd.read_csv(data_file)
    return df

try:
    df = load_data()
    st.success(f"✓ Loaded {len(df):,} soil samples for analysis")
except:
    st.error("Could not load data. Using synthetic data for demonstration.")
    df = pd.DataFrame({
        'Traditional N Rec': np.random.normal(27, 15, 1000),
        'Available N (Haney)': np.random.normal(60, 35, 1000)
    })

# ============================================================================
# SECTION 1: ASSUMPTIONS & PARAMETERS
# ============================================================================

st.markdown("---")
st.markdown("## 📋 Model Assumptions & Parameters")

col1, col2 = st.columns(2)

with col1:
    st.markdown("<div class='assumption-header'>🧪 Testing Parameters</div>", unsafe_allow_html=True)

    haney_cost = st.slider(
        "Haney Test Cost ($/sample)",
        min_value=30.0, max_value=100.0, value=50.0, step=5.0,
        help="Typical range: $45-65 per sample"
    )

    traditional_cost = st.slider(
        "Traditional Test Cost ($/sample)",
        min_value=10.0, max_value=50.0, value=25.0, step=2.5,
        help="Typical range: $20-35 per sample"
    )

    num_depths = st.slider(
        "Sampling Depths per Location",
        min_value=1, max_value=4, value=1, step=1,
        help="Common: 1 (0-6\") or 2 (0-6\", 6-12\")"
    )

    acres_per_field = st.slider(
        "Average Field Size (acres)",
        min_value=10, max_value=500, value=80, step=10,
        help="Used to calculate per-acre economics"
    )

    samples_per_field = st.slider(
        "Samples per Field",
        min_value=1, max_value=20, value=4, step=1,
        help="More samples = better spatial resolution"
    )

    testing_frequency_years = st.slider(
        "Testing Frequency (years)",
        min_value=1, max_value=5, value=3, step=1,
        help="How often do you test? (every X years)"
    )

with col2:
    st.markdown("<div class='assumption-header'>🌾 Crop & Economic Parameters</div>", unsafe_allow_html=True)

    nitrogen_price = st.slider(
        "Nitrogen Price ($/lb N)",
        min_value=0.40, max_value=1.50, value=0.75, step=0.05,
        help="Anhydrous ammonia ~$0.50-0.70, Urea ~$0.60-0.90, UAN ~$0.70-1.00"
    )

    application_cost = st.slider(
        "Application Cost ($/acre)",
        min_value=5.0, max_value=25.0, value=12.0, step=1.0,
        help="Custom application or equipment cost per acre"
    )

    crop_type = st.selectbox(
        "Primary Crop",
        ["Corn", "Soybeans", "Wheat", "Cotton", "Other"],
        help="Different crops have different N response curves"
    )

    # Crop-specific parameters
    if crop_type == "Corn":
        n_response_efficiency = st.slider(
            "N Use Efficiency (%)",
            min_value=30, max_value=70, value=50, step=5,
            help="% of applied N actually used by crop"
        )
        yield_response_per_lb_n = st.slider(
            "Yield Response (bu/acre per lb N)",
            min_value=0.5, max_value=2.0, value=1.0, step=0.1,
            help="Additional yield per lb N applied (diminishing returns assumed)"
        )
        corn_price = st.slider(
            "Corn Price ($/bu)",
            min_value=3.0, max_value=8.0, value=5.50, step=0.25
        )
    else:
        n_response_efficiency = 50
        yield_response_per_lb_n = 0.5
        corn_price = 5.50

    environmental_cost = st.slider(
        "Environmental/Risk Cost ($/lb excess N)",
        min_value=0.0, max_value=0.50, value=0.10, step=0.05,
        help="Cost of N leaching, runoff, regulatory risk (often overlooked)"
    )

# ============================================================================
# SECTION 2: MATHEMATICAL MODEL
# ============================================================================

st.markdown("---")
st.markdown("## 🧮 Economic Model Equations")

with st.expander("📐 View Detailed Equations", expanded=False):
    st.markdown("""
    ### Core Economic Model

    #### 1. Testing Costs
    ```
    Total_Test_Cost = (Test_Cost_per_Sample × Samples_per_Field × Depths × Fields) / Testing_Frequency

    Annual_Test_Cost_per_Acre = Total_Test_Cost / (Fields × Acres_per_Field × Testing_Frequency)
    ```

    #### 2. Nitrogen Recommendation Difference
    ```
    ΔN = N_Traditional - N_Haney

    where:
        N_Traditional = Traditional soil test N recommendation (lbs/acre)
        N_Haney = Haney test available N (lbs/acre)
        ΔN = Difference in N recommendation (typically positive)
    ```

    #### 3. Fertilizer Cost Impact
    ```
    Fertilizer_Cost_Savings = ΔN × N_Price × Acres

    Application_Cost_Savings = (ΔN / Typical_Application_Rate) × Application_Cost × Acres
        where Typical_Application_Rate = 100 lbs N/acre
    ```

    #### 4. Yield Impact (Precision N Management)
    ```
    Yield_Value_Change = (ΔN × N_Use_Efficiency/100 × Yield_Response × Crop_Price) × Acres

    Note: Assumes Haney test provides more accurate N recommendation,
          reducing both over-application and under-application risk
    ```

    #### 5. Environmental Cost Savings
    ```
    Environmental_Savings = |ΔN| × Environmental_Cost × Acres

    (Avoided costs: nitrate leaching, water quality, regulatory compliance)
    ```

    #### 6. Net Economic Benefit
    ```
    Annual_Net_Benefit = (Fertilizer_Savings + Application_Savings + Yield_Value + Environmental_Savings)
                        - (Haney_Test_Cost - Traditional_Test_Cost)

    Payback_Period = (Haney_Test_Cost - Traditional_Test_Cost) / Annual_Net_Benefit

    ROI = (Annual_Net_Benefit × Years) / Additional_Test_Investment × 100%
    ```

    #### 7. Break-Even Analysis
    ```
    Break_Even_Acres = (Haney_Cost - Traditional_Cost) × Samples / (ΔN × N_Price)
    ```
    """)

# ============================================================================
# SECTION 3: CALCULATIONS FROM ACTUAL DATA
# ============================================================================

st.markdown("---")
st.markdown("## 📊 Analysis Based on Your Data")

# Get actual nitrogen data
trad_col = None
haney_col = None

for col in df.columns:
    if 'traditional' in col.lower() and 'rec' in col.lower():
        trad_col = col
    if 'available n' in col.lower() or ('haney' in col.lower() and 'n' in col.lower()):
        haney_col = col

if trad_col and haney_col:
    # Filter valid data
    valid_data = df[[trad_col, haney_col]].dropna()

    if len(valid_data) > 0:
        traditional_n_mean = valid_data[trad_col].mean()
        haney_n_mean = valid_data[haney_col].mean()
        n_difference_mean = haney_n_mean - traditional_n_mean
        n_difference_median = valid_data[haney_col].median() - valid_data[trad_col].median()

        st.success(f"✓ Using actual data: {len(valid_data):,} samples with both Traditional and Haney N values")
    else:
        st.warning("Using estimated values based on literature")
        traditional_n_mean = 27.0
        haney_n_mean = 60.0
        n_difference_mean = 33.0
        n_difference_median = 31.0
else:
    traditional_n_mean = 27.0
    haney_n_mean = 60.0
    n_difference_mean = 33.0
    n_difference_median = 31.0

# ============================================================================
# SECTION 4: ECONOMIC CALCULATIONS
# ============================================================================

# Total samples needed
total_samples_per_field = samples_per_field * num_depths
annual_test_cost_traditional = (traditional_cost * total_samples_per_field) / testing_frequency_years
annual_test_cost_haney = (haney_cost * total_samples_per_field) / testing_frequency_years
additional_test_cost = annual_test_cost_haney - annual_test_cost_traditional

# Per acre testing cost
test_cost_per_acre_traditional = annual_test_cost_traditional / acres_per_field
test_cost_per_acre_haney = annual_test_cost_haney / acres_per_field

# Nitrogen savings
fertilizer_savings_per_acre = n_difference_mean * nitrogen_price
application_savings_per_acre = (n_difference_mean / 100) * application_cost if n_difference_mean > 10 else 0

# Yield impact (assuming better precision with Haney)
# Conservative: assume 20% of excess N was actually needed, 80% was waste
precision_value_per_acre = (n_difference_mean * 0.2 * (n_response_efficiency/100) *
                            yield_response_per_lb_n * corn_price)

# Environmental savings
environmental_savings_per_acre = abs(n_difference_mean) * environmental_cost

# Total savings
total_savings_per_acre = (fertilizer_savings_per_acre +
                         application_savings_per_acre +
                         precision_value_per_acre +
                         environmental_savings_per_acre)

net_benefit_per_acre = total_savings_per_acre - (test_cost_per_acre_haney - test_cost_per_acre_traditional)

# Field level
net_benefit_per_field = net_benefit_per_acre * acres_per_field
total_field_savings = net_benefit_per_field * testing_frequency_years

# Break-even
if fertilizer_savings_per_acre > 0:
    breakeven_acres = additional_test_cost / fertilizer_savings_per_acre
else:
    breakeven_acres = float('inf')

# ROI
if additional_test_cost > 0:
    roi_1_year = (net_benefit_per_acre * acres_per_field) / additional_test_cost * 100
    roi_3_year = (net_benefit_per_acre * acres_per_field * 3) / (additional_test_cost * 3) * 100
else:
    roi_1_year = 0
    roi_3_year = 0

# ============================================================================
# SECTION 5: RESULTS DASHBOARD
# ============================================================================

st.markdown("---")
st.markdown("## 💡 Economic Results")

# Key metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Net Benefit per Acre",
        f"${net_benefit_per_acre:.2f}",
        delta=f"{roi_1_year:.1f}% ROI" if net_benefit_per_acre > 0 else None,
        delta_color="normal" if net_benefit_per_acre > 0 else "inverse"
    )

with col2:
    st.metric(
        "Total Field Benefit",
        f"${net_benefit_per_field:,.2f}",
        delta=f"{acres_per_field} acres"
    )

with col3:
    st.metric(
        "Break-Even Field Size",
        f"{breakeven_acres:.1f} acres" if breakeven_acres != float('inf') else "N/A",
        delta="per test cycle"
    )

with col4:
    st.metric(
        "N Savings per Acre",
        f"{n_difference_mean:.1f} lbs N",
        delta=f"${fertilizer_savings_per_acre:.2f}"
    )

# Detailed breakdown
st.markdown("### 📈 Detailed Cost-Benefit Breakdown (Per Acre, Annualized)")

breakdown_data = {
    'Category': [
        'Testing Cost (Traditional)',
        'Testing Cost (Haney)',
        'Additional Testing Investment',
        '',
        'Fertilizer Cost Savings',
        'Application Cost Savings',
        'Precision Value Gain',
        'Environmental Savings',
        '',
        'Total Savings',
        'Net Benefit'
    ],
    'Amount ($/acre)': [
        -test_cost_per_acre_traditional,
        -test_cost_per_acre_haney,
        -(test_cost_per_acre_haney - test_cost_per_acre_traditional),
        0,
        fertilizer_savings_per_acre,
        application_savings_per_acre,
        precision_value_per_acre,
        environmental_savings_per_acre,
        0,
        total_savings_per_acre,
        net_benefit_per_acre
    ],
    'Description': [
        f"${traditional_cost}/sample × {total_samples_per_field} samples ÷ {testing_frequency_years} yrs ÷ {acres_per_field} ac",
        f"${haney_cost}/sample × {total_samples_per_field} samples ÷ {testing_frequency_years} yrs ÷ {acres_per_field} ac",
        "Additional investment for Haney testing",
        "",
        f"{n_difference_mean:.1f} lbs N × ${nitrogen_price:.2f}/lb",
        f"Reduced application trips/equipment use",
        f"Improved N management precision, reduced risk",
        f"{abs(n_difference_mean):.1f} lbs excess N × ${environmental_cost:.2f}/lb",
        "",
        "Sum of all savings categories",
        "Total Savings - Additional Test Investment"
    ]
}

breakdown_df = pd.DataFrame(breakdown_data)

# Color coding
def color_amount(val):
    if val > 0:
        return f'<span class="metric-positive">+${val:.2f}</span>'
    elif val < 0:
        return f'<span class="metric-negative">-${abs(val):.2f}</span>'
    else:
        return ''

breakdown_df['Amount Display'] = breakdown_df['Amount ($/acre)'].apply(color_amount)

st.markdown(breakdown_df[['Category', 'Amount Display', 'Description']].to_html(escape=False, index=False),
            unsafe_allow_html=True)

# ============================================================================
# SECTION 6: VISUALIZATIONS
# ============================================================================

st.markdown("---")
st.markdown("## 📊 Interactive Visualizations")

# Visualization 1: Waterfall chart
fig_waterfall = go.Figure(go.Waterfall(
    name = "Economic Analysis",
    orientation = "v",
    measure = ["relative", "relative", "relative", "relative", "relative", "total"],
    x = ["Additional<br>Test Cost", "Fertilizer<br>Savings", "Application<br>Savings",
         "Precision<br>Value", "Environmental<br>Savings", "Net<br>Benefit"],
    textposition = "outside",
    text = [f"-${additional_test_cost/acres_per_field:.2f}",
            f"+${fertilizer_savings_per_acre:.2f}",
            f"+${application_savings_per_acre:.2f}",
            f"+${precision_value_per_acre:.2f}",
            f"+${environmental_savings_per_acre:.2f}",
            f"${net_benefit_per_acre:.2f}"],
    y = [-additional_test_cost/acres_per_field,
         fertilizer_savings_per_acre,
         application_savings_per_acre,
         precision_value_per_acre,
         environmental_savings_per_acre,
         net_benefit_per_acre],
    connector = {"line":{"color":"rgb(63, 63, 63)"}},
    decreasing = {"marker":{"color":"#c62828"}},
    increasing = {"marker":{"color":"#2e7d32"}},
    totals = {"marker":{"color":"#1565c0"}}
))

fig_waterfall.update_layout(
    title = "Economic Waterfall: Haney Testing ROI ($/acre)",
    showlegend = False,
    height = 500
)

st.plotly_chart(fig_waterfall, use_container_width=True)

# Visualization 2: Sensitivity Analysis
st.markdown("### 🎯 Sensitivity Analysis: How Do Key Variables Affect ROI?")

sensitivity_var = st.selectbox(
    "Select Variable to Analyze",
    ["Nitrogen Price", "Field Size", "N Difference", "Haney Test Cost", "Testing Frequency"]
)

if sensitivity_var == "Nitrogen Price":
    x_range = np.linspace(0.40, 1.50, 50)
    y_values = [(n_difference_mean * x - (test_cost_per_acre_haney - test_cost_per_acre_traditional))
                for x in x_range]
    x_label = "Nitrogen Price ($/lb)"
    current_val = nitrogen_price

elif sensitivity_var == "Field Size":
    x_range = np.linspace(10, 500, 50)
    y_values = []
    for acres in x_range:
        test_cost_diff = ((haney_cost - traditional_cost) * total_samples_per_field / testing_frequency_years) / acres
        savings = fertilizer_savings_per_acre + application_savings_per_acre + precision_value_per_acre + environmental_savings_per_acre
        y_values.append(savings - test_cost_diff)
    x_label = "Field Size (acres)"
    current_val = acres_per_field

elif sensitivity_var == "N Difference":
    x_range = np.linspace(0, 80, 50)
    y_values = []
    for delta_n in x_range:
        fert_save = delta_n * nitrogen_price
        app_save = (delta_n / 100) * application_cost if delta_n > 10 else 0
        prec_val = (delta_n * 0.2 * (n_response_efficiency/100) * yield_response_per_lb_n * corn_price)
        env_save = delta_n * environmental_cost
        y_values.append(fert_save + app_save + prec_val + env_save - (test_cost_per_acre_haney - test_cost_per_acre_traditional))
    x_label = "N Difference: Haney - Traditional (lbs/acre)"
    current_val = n_difference_mean

elif sensitivity_var == "Haney Test Cost":
    x_range = np.linspace(30, 100, 50)
    y_values = []
    for cost in x_range:
        test_cost_diff = ((cost - traditional_cost) * total_samples_per_field / testing_frequency_years) / acres_per_field
        savings = fertilizer_savings_per_acre + application_savings_per_acre + precision_value_per_acre + environmental_savings_per_acre
        y_values.append(savings - test_cost_diff)
    x_label = "Haney Test Cost ($/sample)"
    current_val = haney_cost

else:  # Testing Frequency
    x_range = np.linspace(1, 5, 5)
    y_values = []
    for freq in x_range:
        test_cost_diff = ((haney_cost - traditional_cost) * total_samples_per_field / freq) / acres_per_field
        savings = fertilizer_savings_per_acre + application_savings_per_acre + precision_value_per_acre + environmental_savings_per_acre
        y_values.append(savings - test_cost_diff)
    x_label = "Testing Frequency (years)"
    current_val = testing_frequency_years

fig_sensitivity = go.Figure()

fig_sensitivity.add_trace(go.Scatter(
    x=x_range,
    y=y_values,
    mode='lines',
    name='Net Benefit',
    line=dict(color='#2e7d32', width=3)
))

# Add zero line
fig_sensitivity.add_hline(y=0, line_dash="dash", line_color="red",
                          annotation_text="Break-Even", annotation_position="right")

# Add current value marker
fig_sensitivity.add_vline(x=current_val, line_dash="dot", line_color="blue",
                         annotation_text="Current", annotation_position="top")

fig_sensitivity.update_layout(
    title=f"Sensitivity: Net Benefit per Acre vs {sensitivity_var}",
    xaxis_title=x_label,
    yaxis_title="Net Benefit ($/acre)",
    height=500,
    hovermode='x unified'
)

st.plotly_chart(fig_sensitivity, use_container_width=True)

# Visualization 3: Multi-variable scenario matrix
st.markdown("### 🎲 Scenario Matrix: Field Size × Nitrogen Price")

field_sizes = np.array([20, 40, 80, 160, 320])
n_prices = np.array([0.50, 0.65, 0.75, 0.90, 1.20])

scenario_matrix = np.zeros((len(n_prices), len(field_sizes)))

for i, n_price in enumerate(n_prices):
    for j, field_size in enumerate(field_sizes):
        test_cost_diff = ((haney_cost - traditional_cost) * total_samples_per_field / testing_frequency_years) / field_size
        fert_save = n_difference_mean * n_price
        app_save = (n_difference_mean / 100) * application_cost if n_difference_mean > 10 else 0
        prec_val = (n_difference_mean * 0.2 * (n_response_efficiency/100) * yield_response_per_lb_n * corn_price)
        env_save = n_difference_mean * environmental_cost
        scenario_matrix[i, j] = fert_save + app_save + prec_val + env_save - test_cost_diff

fig_heatmap = go.Figure(data=go.Heatmap(
    z=scenario_matrix,
    x=field_sizes,
    y=n_prices,
    colorscale='RdYlGn',
    text=np.round(scenario_matrix, 2),
    texttemplate='$%{text}',
    textfont={"size":12},
    colorbar=dict(title="Net Benefit<br>($/acre)")
))

fig_heatmap.update_layout(
    title="Scenario Analysis: Net Benefit per Acre",
    xaxis_title="Field Size (acres)",
    yaxis_title="Nitrogen Price ($/lb)",
    height=500
)

st.plotly_chart(fig_heatmap, use_container_width=True)

# ============================================================================
# SECTION 7: RECOMMENDATIONS
# ============================================================================

st.markdown("---")
st.markdown("## 🎯 Recommendations & Decision Framework")

if net_benefit_per_acre > 5:
    st.success(f"""
    ### ✅ Strong Economic Case for Haney Testing

    **Net benefit of ${net_benefit_per_acre:.2f}/acre justifies the additional testing investment.**

    **Key Drivers:**
    - Nitrogen savings: ${fertilizer_savings_per_acre:.2f}/acre
    - Break-even at {breakeven_acres:.1f} acres (you have {acres_per_field} acres)
    - ROI: {roi_1_year:.1f}% in first year

    **Recommended Action:** Adopt Haney testing for improved N management precision.
    """)
elif net_benefit_per_acre > 0:
    st.info(f"""
    ### ⚖️ Marginal Economic Case

    **Net benefit of ${net_benefit_per_acre:.2f}/acre is positive but modest.**

    **Considerations:**
    - May become more attractive with larger field sizes or higher N prices
    - Environmental benefits provide additional non-quantified value
    - Consider for high-value fields or problematic soils first

    **Recommended Action:** Pilot on select fields, evaluate results.
    """)
else:
    st.warning(f"""
    ### ⚠️ Economics Currently Unfavorable

    **Net benefit of ${net_benefit_per_acre:.2f}/acre suggests traditional testing is more economical under current assumptions.**

    **Factors that could change the analysis:**
    - Larger field sizes (break-even: {breakeven_acres:.1f} acres)
    - Higher nitrogen prices
    - More samples per field (reducing per-acre test cost)
    - Different crop with higher N response

    **Recommended Action:** Re-evaluate if conditions change.
    """)

# Additional insights
with st.expander("📚 Additional Considerations"):
    st.markdown("""
    ### Non-Quantified Benefits of Haney Testing:

    1. **Risk Management**
       - Reduced over-fertilization risk
       - Better compliance with nutrient management regulations
       - Improved documentation for sustainability certifications

    2. **Soil Health Insights**
       - Haney test provides soil respiration data (biological activity)
       - Better understanding of organic matter quality
       - Water-extractable organic carbon (WEOC) measurements

    3. **Long-Term Soil Building**
       - More accurate picture supports soil health investments
       - Can track biological improvements over time
       - Aligns with regenerative agriculture goals

    4. **Precision Agriculture Integration**
       - Better data for variable rate N applications
       - Improves predictive models
       - Supports zone management decisions

    ### Limitations of This Analysis:

    - Assumes uniform soil conditions across field
    - Does not account for spatial variability benefits
    - Yield response curves are simplified (reality: diminishing returns)
    - Weather and management factors not included
    - Environmental costs are estimates (regulatory landscape varies)

    ### Next Steps for Validation:

    1. Conduct on-farm trials with split fields (Haney vs Traditional)
    2. Track actual N applications and yields
    3. Measure soil health improvements over multiple years
    4. Calculate actual ROI with your specific data
    """)

# ============================================================================
# SECTION 8: EXPORT RESULTS
# ============================================================================

st.markdown("---")
st.markdown("## 📥 Export Analysis")

if st.button("Generate PDF Report"):
    st.info("PDF generation feature coming soon. Currently, use browser print to save as PDF.")

# CSV export of scenarios
export_scenarios = []
for field_size in [20, 40, 80, 160, 320]:
    for n_price in [0.50, 0.65, 0.75, 0.90, 1.20]:
        test_cost_diff = ((haney_cost - traditional_cost) * total_samples_per_field / testing_frequency_years) / field_size
        fert_save = n_difference_mean * n_price
        app_save = (n_difference_mean / 100) * application_cost if n_difference_mean > 10 else 0
        prec_val = (n_difference_mean * 0.2 * (n_response_efficiency/100) * yield_response_per_lb_n * corn_price)
        env_save = n_difference_mean * environmental_cost
        net = fert_save + app_save + prec_val + env_save - test_cost_diff

        export_scenarios.append({
            'Field_Size_Acres': field_size,
            'N_Price_per_lb': n_price,
            'Test_Cost_Difference_per_Acre': test_cost_diff,
            'Fertilizer_Savings_per_Acre': fert_save,
            'Application_Savings_per_Acre': app_save,
            'Precision_Value_per_Acre': prec_val,
            'Environmental_Savings_per_Acre': env_save,
            'Net_Benefit_per_Acre': net,
            'Total_Field_Benefit': net * field_size
        })

export_df = pd.DataFrame(export_scenarios)

csv = export_df.to_csv(index=False)
st.download_button(
    label="📊 Download Scenario Analysis (CSV)",
    data=csv,
    file_name="haney_economic_scenarios.csv",
    mime="text/csv"
)

st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 2rem;'>
    <p><strong>Economic Analysis Tool v1.0</strong></p>
    <p>Model assumptions based on agronomic research and industry standards.</p>
    <p>For specific recommendations, consult with a certified crop advisor or agronomist.</p>
</div>
""", unsafe_allow_html=True)
