"""
Interactive Agricultural Soil Health EDA Dashboard
Built with Streamlit and Plotly (open-source packages)

Author: Claude Code
Date: October 6, 2025
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

# For ZIP code geocoding
try:
    from uszipcode import SearchEngine
    USZIPCODE_AVAILABLE = True
except ImportError:
    USZIPCODE_AVAILABLE = False

# Page configuration
st.set_page_config(
    page_title="Soil Health EDA Dashboard",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #2c5f2d;
        font-weight: bold;
        text-align: center;
        padding: 1rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #2c5f2d;
    }
    .info-box {
        background-color: #e8f5e9;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
    .feedback-box {
        background-color: #fff3e0;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #ff9800;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Paths
BASE_DIR = Path('/Users/deyus-ex-machina/agwise/agwise_eda')
DATA_FILE = BASE_DIR / 'data' / 'processed' / 'combined_soil_data_FULL.csv'
FEEDBACK_DIR = BASE_DIR / 'feedback'
FEEDBACK_FILE = FEEDBACK_DIR / 'user_feedback.csv'
FEEDBACK_UPLOADS = FEEDBACK_DIR / 'uploads'

# Ensure feedback directories exist
FEEDBACK_DIR.mkdir(exist_ok=True)
FEEDBACK_UPLOADS.mkdir(exist_ok=True)

# Cache data loading
@st.cache_data
def load_data():
    """Load and cache the dataset"""
    df = pd.read_csv(DATA_FILE)
    return df

# Feedback system functions
def save_feedback(page, feedback_type, message, uploaded_file=None):
    """Save user feedback to CSV file"""
    import datetime

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Handle file upload
    file_path = None
    if uploaded_file is not None:
        # Save uploaded file
        file_ext = uploaded_file.name.split('.')[-1]
        file_path = FEEDBACK_UPLOADS / f"feedback_{timestamp.replace(':', '-').replace(' ', '_')}.{file_ext}"
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        file_path = str(file_path.relative_to(BASE_DIR))

    # Prepare feedback entry
    feedback_entry = {
        'timestamp': timestamp,
        'page': page,
        'type': feedback_type,
        'message': message,
        'file_attachment': file_path or 'None'
    }

    # Append to CSV
    feedback_df = pd.DataFrame([feedback_entry])

    if FEEDBACK_FILE.exists():
        # Append to existing file
        feedback_df.to_csv(FEEDBACK_FILE, mode='a', header=False, index=False)
    else:
        # Create new file with header
        feedback_df.to_csv(FEEDBACK_FILE, mode='w', header=True, index=False)

    return True

# Load data
try:
    data = load_data()
    data_loaded = True
except Exception as e:
    st.error(f"Error loading data: {e}")
    data_loaded = False

if data_loaded:
    # Header
    st.markdown('<p class="main-header">🌱 Agricultural Soil Health EDA Dashboard</p>',
                unsafe_allow_html=True)

    # Count batches dynamically
    n_batches = data['_source_batch'].nunique() if '_source_batch' in data.columns else 'Unknown'

    st.markdown(f"""
    <div class="info-box">
    <b>Dataset Overview:</b> {len(data):,} samples | {len(data.columns)} variables |
    {n_batches} batches | Interactive analysis of full soil health dataset
    </div>
    """, unsafe_allow_html=True)

    # Sidebar
    st.sidebar.title("📊 Dashboard Controls")
    st.sidebar.markdown("---")

    # Page selection
    page = st.sidebar.radio(
        "Select Analysis View:",
        ["📈 Overview & Statistics",
         "🔬 Soil Health Analysis",
         "🌾 Cover Crop Analysis",
         "💰 Economic Analysis",
         "🔗 Correlation Explorer",
         "📊 Custom Analysis",
         "📚 Data Dictionary",
         "📦 Project Deliverables"]
    )

    st.sidebar.markdown("---")
    st.sidebar.info(f"""
    **About This Dashboard**

    Interactive exploration of {len(data):,} soil samples from agricultural testing across 4 data batches.

    Built with:
    - Streamlit (UI)
    - Plotly (Interactive charts)
    - Pandas (Data analysis)
    """)

    # Feedback Section
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 💬 Feedback")

    with st.sidebar.expander("📝 Submit Feedback", expanded=False):
        st.markdown("""
        <div class="feedback-box">
        Have a question, comment, or concern? Let us know!
        </div>
        """, unsafe_allow_html=True)

        feedback_type = st.selectbox(
            "Type:",
            ["Question", "Comment", "Bug Report", "Feature Request", "Data Issue", "Other"],
            key="feedback_type"
        )

        feedback_message = st.text_area(
            "Message:",
            placeholder="Describe your feedback here...",
            height=100,
            key="feedback_message"
        )

        uploaded_file = st.file_uploader(
            "Attach file (optional):",
            type=['png', 'jpg', 'jpeg', 'pdf', 'csv', 'xlsx', 'txt', 'docx'],
            key="feedback_file"
        )

        if st.button("📤 Submit Feedback", key="submit_feedback"):
            if feedback_message.strip():
                try:
                    save_feedback(
                        page=page,
                        feedback_type=feedback_type,
                        message=feedback_message,
                        uploaded_file=uploaded_file
                    )
                    st.success("✅ Feedback submitted successfully! Thank you!")
                    st.balloons()
                except Exception as e:
                    st.error(f"❌ Error submitting feedback: {e}")
            else:
                st.warning("⚠️ Please enter a message before submitting.")

    # ==================================================================
    # PAGE 1: OVERVIEW & STATISTICS
    # ==================================================================
    if page == "📈 Overview & Statistics":
        st.header("📈 Dataset Overview & Key Statistics")

        # Top metrics
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("Total Samples", f"{len(data):,}",
                     delta=f"{len(data):,} samples")
        with col2:
            unique = len(data) - data.duplicated().sum()
            dup_pct = (data.duplicated().sum() / len(data) * 100)
            st.metric("Unique Samples", f"{unique:,}",
                     delta=f"-{dup_pct:.1f}% duplicates", delta_color="inverse")
        with col3:
            st.metric("Variables", len(data.columns),
                     delta=f"{len(data.columns)} total")
        with col4:
            batch_col = '_source_batch'
            if batch_col in data.columns:
                n_batches = data[batch_col].nunique()
                st.metric("Data Batches", n_batches)

        st.markdown("---")

        # Batch comparison
        st.subheader("📦 Batch Distribution")
        if '_source_batch' in data.columns:
            batch_counts = data['_source_batch'].value_counts().sort_index()

            fig = go.Figure(data=[
                go.Bar(x=batch_counts.index, y=batch_counts.values,
                      marker_color=['#2c5f2d', '#97c93d'])
            ])
            fig.update_layout(
                title="Samples by Batch",
                xaxis_title="Batch",
                yaxis_title="Number of Samples",
                height=400
            )
            st.plotly_chart(fig, use_container_width=True)

        st.markdown("---")

        # Geographic Distribution
        st.subheader("🗺️ Geographic Distribution of Samples")

        if 'Zip' in data.columns:
            zip_data = data['Zip'].dropna()

            if len(zip_data) > 0:
                # Clean ZIP codes: handle both string and numeric formats
                def clean_zip(z):
                    try:
                        z_str = str(z)
                        if '.' in z_str:
                            z_str = str(int(float(z_str)))
                        return z_str.zfill(5) if z_str.isdigit() and len(z_str) <= 5 else None
                    except:
                        return None

                zip_cleaned = zip_data.apply(clean_zip).dropna()

                # Count samples by ZIP code
                zip_counts = zip_cleaned.value_counts().reset_index()
                zip_counts.columns = ['zip', 'count']

                # Display summary stats
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.metric("Samples with ZIP", f"{len(zip_cleaned):,}")
                with col2:
                    st.metric("Unique ZIP Codes", f"{len(zip_counts):,}")
                with col3:
                    st.metric("Most Common ZIP", str(zip_counts.iloc[0]['zip']))
                with col4:
                    st.metric("Samples in Top ZIP", f"{zip_counts.iloc[0]['count']:,}")

                # Create map visualization
                if USZIPCODE_AVAILABLE:
                    st.info("💡 Geocoding ZIP codes for map visualization... This may take a moment on first load.")

                    # Cache the geocoding result
                    @st.cache_data
                    def geocode_zips(zip_counts_df):
                        search = SearchEngine()
                        geocoded = []

                        for idx, row in zip_counts_df.head(200).iterrows():  # Limit to top 200 for performance
                            try:
                                # Handle both string and numeric ZIP codes
                                zip_raw = row['zip']
                                if pd.isna(zip_raw):
                                    continue

                                # Convert to string, handle float format
                                zip_str = str(zip_raw)
                                if '.' in zip_str:
                                    zip_str = str(int(float(zip_str)))

                                # Ensure 5-digit format
                                zip_str = zip_str.zfill(5)

                                # Only process valid 5-digit US ZIP codes
                                if len(zip_str) == 5 and zip_str.isdigit():
                                    result = search.by_zipcode(zip_str)
                                    if result and result.lat and result.lng:
                                        geocoded.append({
                                            'zip': zip_str,
                                            'count': row['count'],
                                            'lat': result.lat,
                                            'lng': result.lng,
                                            'city': result.major_city or 'Unknown',
                                            'state': result.state or 'Unknown'
                                        })
                            except (ValueError, TypeError) as e:
                                # Skip invalid ZIP codes
                                continue

                        return pd.DataFrame(geocoded)

                    try:
                        geo_data = geocode_zips(zip_counts)

                        if len(geo_data) > 0:
                            # Create scatter map
                            fig = px.scatter_geo(
                                geo_data,
                                lat='lat',
                                lon='lng',
                                size='count',
                                hover_name='zip',
                                hover_data={
                                    'city': True,
                                    'state': True,
                                    'count': True,
                                    'lat': ':.3f',
                                    'lng': ':.3f'
                                },
                                title=f'Sample Distribution Across ZIP Codes (Top {len(geo_data)} ZIPs)',
                                size_max=40,
                                color='count',
                                color_continuous_scale='Greens'
                            )

                            fig.update_geos(
                                scope='usa',
                                showcountries=True,
                                showsubunits=True,
                                showlakes=True
                            )

                            fig.update_layout(
                                height=600,
                                geo=dict(
                                    bgcolor='rgba(0,0,0,0)',
                                    lakecolor='lightblue',
                                    landcolor='white'
                                )
                            )

                            st.plotly_chart(fig, use_container_width=True)

                            # Show top 10 locations
                            st.subheader("📍 Top 10 Sample Locations")
                            top_10 = geo_data.nlargest(10, 'count')[['zip', 'city', 'state', 'count']]
                            top_10.columns = ['ZIP Code', 'City', 'State', 'Sample Count']
                            st.dataframe(top_10.reset_index(drop=True), use_container_width=True, hide_index=True)
                        else:
                            st.warning("Unable to geocode ZIP codes. Showing distribution table instead.")
                            # Fallback to table
                            st.dataframe(zip_counts.head(20), use_container_width=True)

                    except Exception as e:
                        st.warning(f"Map geocoding encountered an issue: {e}. Showing distribution table.")
                        st.dataframe(zip_counts.head(20), use_container_width=True)

                else:
                    # Fallback if uszipcode not available
                    st.warning("⚠️ Geographic mapping requires the `uszipcode` package. Install it with: `pip install uszipcode`")

                    st.subheader("📊 Top 20 ZIP Codes by Sample Count")
                    top_20 = zip_counts.head(20)

                    fig = go.Figure(data=[
                        go.Bar(x=top_20['zip'].astype(str), y=top_20['count'],
                              marker_color='#2c5f2d')
                    ])
                    fig.update_layout(
                        title="Sample Distribution by ZIP Code (Top 20)",
                        xaxis_title="ZIP Code",
                        yaxis_title="Number of Samples",
                        height=500
                    )
                    fig.update_xaxes(tickangle=45)
                    st.plotly_chart(fig, use_container_width=True)

                    st.dataframe(zip_counts.head(20), use_container_width=True)
        else:
            st.info("ZIP code data not available in the dataset.")

        st.markdown("---")

        # Key metrics statistics
        st.subheader("📊 Key Soil Metrics Statistics")

        key_metrics = ['1:1 Soil pH', 'Organic Matter', 'CO2-C',
                      'Soil Health Calculation', 'H3A Nitrate']
        available_metrics = [col for col in key_metrics if col in data.columns]

        if available_metrics:
            stats_data = []
            for col in available_metrics:
                values = pd.to_numeric(data[col], errors='coerce').dropna()
                if len(values) > 0:
                    stats_data.append({
                        'Metric': col,
                        'Count': f"{len(values):,}",
                        'Mean': f"{values.mean():.2f}",
                        'Median': f"{values.median():.2f}",
                        'Std Dev': f"{values.std():.2f}",
                        'Min': f"{values.min():.2f}",
                        'Max': f"{values.max():.2f}"
                    })

            stats_df = pd.DataFrame(stats_data)
            st.dataframe(stats_df, use_container_width=True, height=250)

    # ==================================================================
    # PAGE 2: SOIL HEALTH ANALYSIS
    # ==================================================================
    elif page == "🔬 Soil Health Analysis":
        st.header("🔬 Soil Health Score Analysis")

        health_col = 'Soil Health Calculation' if 'Soil Health Calculation' in data.columns else 'Soil Health Score'

        if health_col in data.columns:
            health_data = pd.to_numeric(data[health_col], errors='coerce').dropna()

            # Key metrics
            col1, col2, col3, col4, col5 = st.columns(5)
            with col1:
                st.metric("Mean Score", f"{health_data.mean():.2f}")
            with col2:
                st.metric("Median Score", f"{health_data.median():.2f}")
            with col3:
                st.metric("Std Dev", f"{health_data.std():.2f}")
            with col4:
                st.metric("Min", f"{health_data.min():.2f}")
            with col5:
                st.metric("Max", f"{health_data.max():.2f}")

            st.markdown("---")

            # Distribution plot
            col1, col2 = st.columns([2, 1])

            with col1:
                fig = go.Figure()
                fig.add_trace(go.Histogram(
                    x=health_data,
                    nbinsx=50,
                    name='Distribution',
                    marker_color='#2c5f2d',
                    opacity=0.7
                ))
                fig.add_vline(x=health_data.mean(), line_dash="dash",
                             line_color="red", annotation_text="Mean")
                fig.add_vline(x=health_data.median(), line_dash="dash",
                             line_color="blue", annotation_text="Median")
                fig.update_layout(
                    title=f"{health_col} Distribution",
                    xaxis_title=health_col,
                    yaxis_title="Frequency",
                    height=500
                )
                st.plotly_chart(fig, use_container_width=True)

            with col2:
                # Categories
                st.subheader("Score Categories")
                bins = [0, 2, 5, 10, 150]
                labels = ['Poor (0-2)', 'Fair (2-5)', 'Good (5-10)', 'Excellent (10+)']
                categories = pd.cut(health_data, bins=bins, labels=labels)
                cat_counts = categories.value_counts().sort_index()

                fig = go.Figure(data=[
                    go.Pie(labels=cat_counts.index, values=cat_counts.values,
                          marker_colors=['#d32f2f', '#ff9800', '#ffc107', '#4caf50'])
                ])
                fig.update_layout(height=400, title="Health Categories")
                st.plotly_chart(fig, use_container_width=True)

            # Factors analysis
            st.subheader("🎯 Top Factors Correlated with Soil Health")

            analysis_cols = ['CO2-C', 'Organic Matter', '1:1 Soil pH',
                           'H3A ICAP Potassium', 'H3A ICAP Calcium']
            available_analysis = [col for col in analysis_cols
                                if col in data.columns and data[col].notna().sum() > 100]

            if available_analysis:
                correlations = []
                for col in available_analysis:
                    temp_df = data[[health_col, col]].apply(pd.to_numeric, errors='coerce').dropna()
                    if len(temp_df) > 50:
                        corr = temp_df[health_col].corr(temp_df[col])
                        correlations.append({'Factor': col, 'Correlation': corr})

                if correlations:
                    corr_df = pd.DataFrame(correlations).sort_values('Correlation', ascending=False)

                    fig = go.Figure(data=[
                        go.Bar(x=corr_df['Factor'], y=corr_df['Correlation'],
                              marker_color=['#2c5f2d' if x > 0 else '#d32f2f'
                                          for x in corr_df['Correlation']])
                    ])
                    fig.update_layout(
                        title="Correlation with Soil Health",
                        xaxis_title="Factor",
                        yaxis_title="Correlation Coefficient",
                        height=400
                    )
                    st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("Soil Health Score data not available in dataset.")

    # ==================================================================
    # PAGE 3: COVER CROP ANALYSIS
    # ==================================================================
    elif page == "🌾 Cover Crop Analysis":
        st.header("🌾 Cover Crop Mix Analysis")

        cover_cols = ['Cover Crop Mix', 'Cover crop mix']
        cover_col = None
        for col in cover_cols:
            if col in data.columns and data[col].notna().sum() > 50:
                cover_col = col
                break

        if cover_col:
            cover_data = data[cover_col].dropna()

            # Distribution
            st.subheader("📊 Cover Crop Mix Distribution")
            value_counts = cover_data.value_counts()

            fig = go.Figure(data=[
                go.Bar(x=value_counts.index, y=value_counts.values,
                      marker_color='#2c5f2d')
            ])
            fig.update_layout(
                title=f"Distribution of {cover_col}",
                xaxis_title="Cover Crop Mix",
                yaxis_title="Count",
                height=500
            )
            fig.update_xaxes(tickangle=45)
            st.plotly_chart(fig, use_container_width=True)

            # Health by cover crop
            health_col = 'Soil Health Calculation' if 'Soil Health Calculation' in data.columns else 'Soil Health Score'

            if health_col in data.columns:
                st.subheader("🌱 Soil Health by Cover Crop Mix")

                cover_health = data[[cover_col, health_col]].copy()
                cover_health[health_col] = pd.to_numeric(cover_health[health_col], errors='coerce')
                cover_health = cover_health.dropna()

                if len(cover_health) > 0:
                    # Box plot
                    fig = go.Figure()

                    for mix in sorted(cover_health[cover_col].unique()):
                        mix_data = cover_health[cover_health[cover_col] == mix][health_col]
                        fig.add_trace(go.Box(y=mix_data, name=mix))

                    fig.update_layout(
                        title=f"{health_col} by Cover Crop Mix",
                        yaxis_title=health_col,
                        xaxis_title="Cover Crop Mix",
                        height=500,
                        showlegend=False
                    )
                    fig.update_xaxes(tickangle=45)
                    st.plotly_chart(fig, use_container_width=True)

                    # Summary statistics
                    summary = cover_health.groupby(cover_col)[health_col].agg([
                        'count', 'mean', 'median', 'std', 'min', 'max'
                    ]).round(2).sort_values('mean', ascending=False)

                    st.subheader("📈 Summary Statistics by Cover Crop")
                    st.dataframe(summary, use_container_width=True)
        else:
            st.warning("Cover Crop Mix data not available in dataset.")

    # ==================================================================
    # PAGE 4: ECONOMIC ANALYSIS
    # ==================================================================
    elif page == "💰 Economic Analysis":
        st.header("💰 Traditional vs Haney Test Economic Analysis")

        trad_col = 'Traditional N'
        haney_col = 'Haney Test N'

        if trad_col in data.columns and haney_col in data.columns:
            comparison = data[[trad_col, haney_col]].apply(pd.to_numeric, errors='coerce').dropna()

            if len(comparison) > 0:
                # Key metrics
                col1, col2, col3, col4 = st.columns(4)

                with col1:
                    st.metric("Sample Size", f"{len(comparison):,}")
                with col2:
                    st.metric("Traditional Mean", f"{comparison[trad_col].mean():.2f} lbs/A")
                with col3:
                    st.metric("Haney Mean", f"{comparison[haney_col].mean():.2f} lbs/A")
                with col4:
                    diff = comparison[haney_col].mean() - comparison[trad_col].mean()
                    st.metric("Mean Difference", f"{diff:.2f} lbs/A",
                             delta=f"+{diff:.1f}")

                st.markdown("---")

                # Scatter plot with 1:1 line
                col1, col2 = st.columns(2)

                with col1:
                    # Sample for performance
                    if len(comparison) > 2000:
                        plot_data = comparison.sample(2000, random_state=42)
                    else:
                        plot_data = comparison

                    fig = go.Figure()
                    fig.add_trace(go.Scatter(
                        x=plot_data[trad_col],
                        y=plot_data[haney_col],
                        mode='markers',
                        marker=dict(color='#2c5f2d', size=5, opacity=0.5),
                        name='Samples'
                    ))

                    # 1:1 line
                    max_val = max(plot_data[trad_col].max(), plot_data[haney_col].max())
                    fig.add_trace(go.Scatter(
                        x=[0, max_val], y=[0, max_val],
                        mode='lines',
                        line=dict(color='red', dash='dash'),
                        name='1:1 Line'
                    ))

                    fig.update_layout(
                        title="Traditional vs Haney N Recommendations",
                        xaxis_title=f"{trad_col} (lbs/A)",
                        yaxis_title=f"{haney_col} (lbs/A)",
                        height=500
                    )
                    st.plotly_chart(fig, use_container_width=True)

                with col2:
                    # Box plot comparison
                    fig = go.Figure()
                    fig.add_trace(go.Box(y=comparison[trad_col], name='Traditional',
                                        marker_color='#ffc107'))
                    fig.add_trace(go.Box(y=comparison[haney_col], name='Haney',
                                        marker_color='#2c5f2d'))

                    fig.update_layout(
                        title="Distribution Comparison",
                        yaxis_title="N Recommendation (lbs/A)",
                        height=500
                    )
                    st.plotly_chart(fig, use_container_width=True)

                # Economic impact
                st.subheader("💵 Economic Impact Calculation")

                n_cost = st.slider("Nitrogen Cost ($/lb)", 0.5, 2.0, 1.0, 0.1)

                difference = comparison[haney_col] - comparison[trad_col]
                cost_savings = difference * n_cost

                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Avg Savings/Sample", f"${cost_savings.mean():.2f}")
                with col2:
                    st.metric("Median Savings/Sample", f"${cost_savings.median():.2f}")
                with col3:
                    st.metric("Total Dataset Savings", f"${cost_savings.sum():,.2f}")
        else:
            st.warning("Traditional vs Haney test data not available.")

    # ==================================================================
    # PAGE 5: CORRELATION EXPLORER
    # ==================================================================
    elif page == "🔗 Correlation Explorer":
        st.header("🔗 Correlation Explorer")

        # Select variables for correlation
        numeric_cols = data.select_dtypes(include=[np.number]).columns.tolist()
        # Filter to columns with sufficient data
        valid_cols = [col for col in numeric_cols
                     if data[col].notna().sum() > 100 and col not in ['_source_file', '_source_batch']]

        st.subheader("Select Variables to Analyze")

        col1, col2 = st.columns(2)

        with col1:
            var1 = st.selectbox("Variable 1:", valid_cols,
                               index=valid_cols.index('Soil Health Calculation')
                               if 'Soil Health Calculation' in valid_cols else 0)

        with col2:
            var2 = st.selectbox("Variable 2:", valid_cols,
                               index=valid_cols.index('CO2-C')
                               if 'CO2-C' in valid_cols else 1)

        if var1 and var2:
            corr_data = data[[var1, var2]].apply(pd.to_numeric, errors='coerce').dropna()

            if len(corr_data) > 0:
                correlation = corr_data[var1].corr(corr_data[var2])

                # Display correlation
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Sample Size", f"{len(corr_data):,}")
                with col2:
                    corr_color = "normal" if abs(correlation) < 0.5 else "inverse" if correlation < 0 else "normal"
                    st.metric("Correlation (r)", f"{correlation:.3f}")
                with col3:
                    strength = "Very Strong" if abs(correlation) > 0.7 else \
                              "Strong" if abs(correlation) > 0.5 else \
                              "Moderate" if abs(correlation) > 0.3 else "Weak"
                    st.metric("Strength", strength)

                # Scatter plot
                # Sample for performance
                if len(corr_data) > 2000:
                    plot_data = corr_data.sample(2000, random_state=42)
                else:
                    plot_data = corr_data

                fig = go.Figure()
                fig.add_trace(go.Scatter(
                    x=plot_data[var1],
                    y=plot_data[var2],
                    mode='markers',
                    marker=dict(
                        color=plot_data[var1],
                        colorscale='Viridis',
                        size=5,
                        opacity=0.6,
                        showscale=True
                    ),
                    name='Data'
                ))

                # Add regression line
                z = np.polyfit(plot_data[var1], plot_data[var2], 1)
                p = np.poly1d(z)
                x_line = np.linspace(plot_data[var1].min(), plot_data[var1].max(), 100)
                fig.add_trace(go.Scatter(
                    x=x_line, y=p(x_line),
                    mode='lines',
                    line=dict(color='red', width=2),
                    name='Regression Line'
                ))

                fig.update_layout(
                    title=f"{var1} vs {var2} (r={correlation:.3f})",
                    xaxis_title=var1,
                    yaxis_title=var2,
                    height=600
                )
                st.plotly_chart(fig, use_container_width=True)

    # ==================================================================
    # PAGE 6: CUSTOM ANALYSIS
    # ==================================================================
    elif page == "📊 Custom Analysis":
        st.header("📊 Custom Data Analysis")

        st.markdown("""
        Explore the dataset with custom filters and visualizations.
        """)

        # Variable selection
        numeric_cols = data.select_dtypes(include=[np.number]).columns.tolist()
        valid_cols = [col for col in numeric_cols
                     if data[col].notna().sum() > 100]

        st.subheader("🔍 Variable Distribution Explorer")

        selected_var = st.selectbox("Select Variable to Analyze:", valid_cols)

        if selected_var:
            var_data = pd.to_numeric(data[selected_var], errors='coerce').dropna()

            # Statistics
            col1, col2, col3, col4, col5 = st.columns(5)
            with col1:
                st.metric("Count", f"{len(var_data):,}")
            with col2:
                st.metric("Mean", f"{var_data.mean():.2f}")
            with col3:
                st.metric("Median", f"{var_data.median():.2f}")
            with col4:
                st.metric("Std Dev", f"{var_data.std():.2f}")
            with col5:
                cv = (var_data.std() / var_data.mean() * 100) if var_data.mean() != 0 else 0
                st.metric("CV", f"{cv:.1f}%")

            # Visualization options
            viz_type = st.radio("Visualization Type:",
                               ["Histogram", "Box Plot", "Violin Plot"])

            if viz_type == "Histogram":
                bins = st.slider("Number of Bins:", 10, 100, 50)
                fig = go.Figure(data=[go.Histogram(x=var_data, nbinsx=bins,
                                                   marker_color='#2c5f2d')])
                fig.add_vline(x=var_data.mean(), line_dash="dash",
                             line_color="red", annotation_text="Mean")
                fig.add_vline(x=var_data.median(), line_dash="dash",
                             line_color="blue", annotation_text="Median")

            elif viz_type == "Box Plot":
                fig = go.Figure(data=[go.Box(y=var_data, marker_color='#2c5f2d')])

            else:  # Violin Plot
                fig = go.Figure(data=[go.Violin(y=var_data, marker_color='#2c5f2d',
                                                box_visible=True, meanline_visible=True)])

            fig.update_layout(
                title=f"Distribution of {selected_var}",
                yaxis_title="Value" if viz_type != "Histogram" else "Frequency",
                xaxis_title=selected_var if viz_type == "Histogram" else "",
                height=500
            )
            st.plotly_chart(fig, use_container_width=True)

            # Percentiles
            st.subheader("📊 Percentile Distribution")
            percentiles = [0, 10, 25, 50, 75, 90, 100]
            percentile_vals = [var_data.quantile(p/100) for p in percentiles]

            perc_df = pd.DataFrame({
                'Percentile': [f"{p}th" for p in percentiles],
                'Value': [f"{v:.2f}" for v in percentile_vals]
            })
            st.dataframe(perc_df, use_container_width=True)

    # ==================================================================
    # PAGE 7: DATA DICTIONARY
    # ==================================================================
    elif page == "📚 Data Dictionary":
        st.header("📚 Data Dictionary")

        st.markdown("""
        Complete reference for all 211 variables in the dataset, organized by category.
        """)

        # Load data dictionary
        dict_file = BASE_DIR / 'DATA_DICTIONARY.md'
        try:
            with open(dict_file, 'r') as f:
                dict_content = f.read()

            # Show summary stats first
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Total Variables", "211")
            with col2:
                st.metric("Numeric Variables", "94")
            with col3:
                st.metric("Categorical Variables", "117")
            with col4:
                st.metric("Categories", "17")

            st.markdown("---")

            # Add search functionality
            st.subheader("🔍 Search Variables")
            search_term = st.text_input("Enter variable name or keyword:", "")

            if search_term:
                # Filter dictionary content
                lines = dict_content.split('\n')
                filtered_lines = []
                show_context = False
                context_lines = 0

                for line in lines:
                    if search_term.lower() in line.lower():
                        show_context = True
                        context_lines = 10  # Show 10 lines after match

                    if show_context:
                        filtered_lines.append(line)
                        context_lines -= 1
                        if context_lines <= 0:
                            show_context = False
                            filtered_lines.append("\n---\n")

                if filtered_lines:
                    st.markdown('\n'.join(filtered_lines))
                else:
                    st.warning(f"No variables found matching '{search_term}'")
            else:
                # Show full dictionary
                st.markdown(dict_content)

        except FileNotFoundError:
            st.error("Data dictionary file not found. Please ensure DATA_DICTIONARY.md exists in the project directory.")
            st.info(f"Expected location: {dict_file}")

    # ==================================================================
    # PAGE 8: PROJECT DELIVERABLES
    # ==================================================================
    elif page == "📦 Project Deliverables":
        st.header("📦 Project Deliverables & File Inventory")

        st.markdown("""
        Complete overview of all analysis outputs, reports, and data files.
        """)

        # Summary metrics
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Samples", f"{len(data):,}")
        with col2:
            st.metric("Data Batches", "4")
        with col3:
            st.metric("Visualizations", "15+")
        with col4:
            st.metric("Reports", "Multiple")

        st.markdown("---")

        # Load and display analysis summary
        summary_file = BASE_DIR / 'ANALYSIS_SUMMARY_ALL_BATCHES.md'
        try:
            with open(summary_file, 'r') as f:
                summary_content = f.read()

            st.markdown(summary_content)

        except FileNotFoundError:
            st.warning("Analysis summary not found. Showing basic inventory...")

        # File structure
        st.subheader("📁 Project Structure")

        structure = """
        ```
        agwise_eda/
        ├── 📄 Documentation
        │   ├── README.md
        │   ├── DATA_DICTIONARY.md
        │   ├── ANALYSIS_SUMMARY_ALL_BATCHES.md
        │   └── PROJECT_SUMMARY.md
        │
        ├── 📊 Reports
        │   ├── COMPREHENSIVE_EDA_REPORT_FULL_DATASET.pdf (5.7 MB)
        │   └── EXECUTIVE_SUMMARY_FULL_DATASET.md
        │
        ├── 💾 Data
        │   ├── raw/ (4 batches, 2,504 files)
        │   └── processed/
        │       └── combined_soil_data_FULL.csv (37,310 samples)
        │
        ├── 🐍 Scripts
        │   ├── run_all_analyses.py
        │   ├── 01_eda_analysis.py
        │   ├── 02_eda_visualizations.py
        │   ├── 03_eda_correlations.py
        │   ├── 04_eda_categorical_crops.py
        │   └── 05_eda_advanced_insights.py
        │
        ├── 📈 Outputs
        │   ├── visualizations/ (15+ charts)
        │   └── tables/ (11+ CSV reports)
        │
        └── 🖥️  Dashboard
            └── app.py (this dashboard)
        ```
        """
        st.markdown(structure)

        # Download links section
        st.subheader("📥 Key Downloads")

        st.markdown("""
        **Main Reports:**
        - `reports/COMPREHENSIVE_EDA_REPORT_FULL_DATASET.pdf` - Complete analysis (5.7 MB)
        - `ANALYSIS_SUMMARY_ALL_BATCHES.md` - Executive summary
        - `DATA_DICTIONARY.md` - Variable reference

        **Data Files:**
        - `combined_soil_data.csv` - Full dataset (37,310 samples, 13 MB)
        - `agwise_eda/data/processed/combined_soil_data_FULL.csv` - Dashboard data

        **Analysis Outputs:**
        - `outputs/visualizations/` - All charts (PNG, 300 DPI)
        - `outputs/tables/` - All statistical tables (CSV)
        """)

        # Quality metrics
        st.subheader("✅ Quality Metrics")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("""
            **Data Quality:**
            - ✅ All 4 batches processed
            - ✅ 37,310 total samples
            - ✅ 211 variables tracked
            - ✅ Batch tracking enabled
            - ✅ Missing data documented
            """)

        with col2:
            st.markdown("""
            **Deliverables:**
            - ✅ Comprehensive PDF report
            - ✅ Interactive dashboard (8 views)
            - ✅ 15+ visualizations (300 DPI)
            - ✅ 11+ statistical tables
            - ✅ Complete data dictionary
            """)

else:
    st.error("Unable to load data. Please check that the data file exists.")
    st.info(f"Expected location: {DATA_FILE}")
