import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr
import warnings
warnings.filterwarnings('ignore')

# Load data
data = pd.read_csv('/Users/deyus-ex-machina/agwise/combined_soil_data.csv')

print(f"{'='*80}")
print(f"CORRELATION AND RELATIONSHIP ANALYSIS")
print(f"{'='*80}")

# Select key numeric columns for correlation analysis
key_cols_v1 = [
    'Soil pH 1:1', '1:1 Electrical Conductivity, mmho/cm',
    'Organic Matter, % LOI', 'Soil Respiration, ppm CO2-C',
    'H3A Nitrate, ppm NO3-N', 'H3A Ammonium, ppm NH4-N',
    'H3A Total Phosphorus, ppm P', 'H3A Potassium, ppm K',
    'H3A Calcium, ppm Ca', 'H3A Magnesium, ppm Mg',
    'Soil Health Score', 'Available N, lbs/A',
    'Available P, lbs/A', 'Available K, lbs/A'
]

key_cols_v2 = [
    '1:1 Soil pH', '1:1 Soluble Salt', 'Organic Matter',
    'CO2-C', 'H3A Nitrate', 'H3A Ammonium',
    'H3A Total Phosphorus', 'H3A ICAP Potassium',
    'H3A ICAP Calcium', 'H3A ICAP Magnesium',
    'Soil Health Calculation', 'Available N',
    'Available P', 'Available K'
]

# Identify available columns
available_cols = []
for col in key_cols_v1 + key_cols_v2:
    if col in data.columns and col not in available_cols:
        # Only include if has sufficient data
        if data[col].notna().sum() > 50:
            available_cols.append(col)

print(f"\nAnalyzing correlations for {len(available_cols)} key variables")
print("Variables included:")
for i, col in enumerate(available_cols, 1):
    non_null = data[col].notna().sum()
    print(f"{i}. {col} (n={non_null})")

# Create correlation matrix (convert to numeric to handle mixed types)
correlation_data = data[available_cols].copy()
for col in correlation_data.columns:
    correlation_data[col] = pd.to_numeric(correlation_data[col], errors='coerce')
corr_matrix = correlation_data.corr()

# Save correlation matrix
corr_matrix.to_csv('/Users/deyus-ex-machina/agwise/correlation_matrix.csv')
print(f"\n✓ Correlation matrix saved to: correlation_matrix.csv")

# Find strongest correlations
print(f"\n{'='*80}")
print(f"STRONGEST CORRELATIONS (|r| > 0.5)")
print(f"{'='*80}")

# Get upper triangle of correlation matrix
mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
corr_pairs = corr_matrix.where(~mask).stack().sort_values(ascending=False)

# Filter for strong correlations
strong_corr = corr_pairs[(abs(corr_pairs) > 0.5) & (abs(corr_pairs) < 1.0)]
print(f"\nFound {len(strong_corr)} strong correlations:")
for idx, (pair, value) in enumerate(strong_corr.head(20).items(), 1):
    print(f"{idx}. {pair[0][:40]:40s} <-> {pair[1][:40]:40s}: {value:6.3f}")

# Save strong correlations
strong_corr_df = pd.DataFrame({
    'Variable_1': [pair[0] for pair in strong_corr.index],
    'Variable_2': [pair[1] for pair in strong_corr.index],
    'Correlation': strong_corr.values
})
strong_corr_df.to_csv('/Users/deyus-ex-machina/agwise/strong_correlations.csv', index=False)
print(f"\n✓ Strong correlations saved to: strong_correlations.csv")

# Visualizations
print(f"\n{'='*80}")
print(f"GENERATING CORRELATION VISUALIZATIONS")
print(f"{'='*80}")

# 1. Correlation heatmap
fig, ax = plt.subplots(figsize=(16, 14))
sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm', center=0,
            square=True, linewidths=0.5, cbar_kws={"shrink": 0.8},
            vmin=-1, vmax=1, ax=ax, annot_kws={'size': 7})
ax.set_title('Correlation Matrix - Key Soil Health Metrics', fontsize=14, pad=20)
plt.xticks(rotation=45, ha='right', fontsize=9)
plt.yticks(rotation=0, fontsize=9)
plt.tight_layout()
plt.savefig('/Users/deyus-ex-machina/agwise/correlation_heatmap.png', dpi=300, bbox_inches='tight')
print("✓ Correlation heatmap saved to: correlation_heatmap.png")
plt.close()

# 2. Scatter plots for top correlated pairs
if len(strong_corr) >= 6:
    fig, axes = plt.subplots(2, 3, figsize=(18, 12))
    fig.suptitle('Scatter Plots - Top 6 Strongest Correlations', fontsize=16, y=0.995)

    for idx, ((var1, var2), corr_val) in enumerate(strong_corr.head(6).items()):
        row = idx // 3
        col = idx % 3
        ax = axes[row, col]

        # Get data for both variables and convert to numeric
        plot_data = data[[var1, var2]].copy()
        plot_data[var1] = pd.to_numeric(plot_data[var1], errors='coerce')
        plot_data[var2] = pd.to_numeric(plot_data[var2], errors='coerce')
        plot_data = plot_data.dropna()

        if len(plot_data) > 0:
            ax.scatter(plot_data[var1], plot_data[var2], alpha=0.5, s=30)
            ax.set_xlabel(var1, fontsize=9)
            ax.set_ylabel(var2, fontsize=9)
            ax.set_title(f'r = {corr_val:.3f} (n={len(plot_data)})', fontsize=10)
            ax.grid(True, alpha=0.3)

            # Add regression line
            z = np.polyfit(plot_data[var1], plot_data[var2], 1)
            p = np.poly1d(z)
            ax.plot(plot_data[var1], p(plot_data[var1]), "r--", alpha=0.8, linewidth=2)

    plt.tight_layout()
    plt.savefig('/Users/deyus-ex-machina/agwise/scatter_correlations.png', dpi=300, bbox_inches='tight')
    print("✓ Scatter plots saved to: scatter_correlations.png")
    plt.close()

print(f"\n{'='*80}")
print(f"SOIL HEALTH SCORE ANALYSIS")
print(f"{'='*80}")

# Analyze what drives Soil Health Score
health_score_col = 'Soil Health Score' if 'Soil Health Score' in data.columns else 'Soil Health Calculation'

if health_score_col in data.columns:
    # Get correlations with soil health score
    health_correlations = correlation_data.corr()[health_score_col].sort_values(ascending=False)
    print(f"\nFactors most correlated with {health_score_col}:")
    for var, corr in health_correlations.items():
        if var != health_score_col:
            print(f"  {var[:60]:60s}: {corr:6.3f}")

    # Save health score correlations
    health_corr_df = pd.DataFrame({
        'Variable': health_correlations.index,
        'Correlation_with_Soil_Health': health_correlations.values
    })
    health_corr_df.to_csv('/Users/deyus-ex-machina/agwise/soil_health_correlations.csv', index=False)
    print(f"\n✓ Soil health correlations saved to: soil_health_correlations.csv")

    # Visualize top factors
    top_factors = health_correlations[health_correlations.index != health_score_col].head(8)

    fig, axes = plt.subplots(2, 4, figsize=(20, 10))
    fig.suptitle(f'Top 8 Factors Correlated with {health_score_col}', fontsize=16, y=0.995)

    for idx, (var, corr) in enumerate(top_factors.items()):
        row = idx // 4
        col = idx % 4
        ax = axes[row, col]

        plot_data = data[[health_score_col, var]].dropna()

        if len(plot_data) > 0:
            ax.scatter(plot_data[var], plot_data[health_score_col], alpha=0.5, s=20)
            ax.set_xlabel(var, fontsize=9)
            ax.set_ylabel(health_score_col, fontsize=9)
            ax.set_title(f'r = {corr:.3f}', fontsize=10)
            ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('/Users/deyus-ex-machina/agwise/soil_health_factors.png', dpi=300, bbox_inches='tight')
    print("✓ Soil health factors plot saved to: soil_health_factors.png")
    plt.close()

print(f"\n{'='*80}")
print(f"CORRELATION ANALYSIS COMPLETE")
print(f"{'='*80}")
