import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

# Load data
data = pd.read_csv('/Users/deyus-ex-machina/agwise/combined_soil_data.csv')

print(f"{'='*80}")
print(f"ADVANCED SOIL HEALTH AND NUTRIENT INSIGHTS")
print(f"{'='*80}")

# Soil Health Score Analysis
health_col = 'Soil Health Score' if 'Soil Health Score' in data.columns else 'Soil Health Calculation'

if health_col in data.columns:
    health_data = data[health_col].dropna()

    print(f"\n{health_col} Distribution:")
    print(f"  Count: {len(health_data)}")
    print(f"  Mean: {health_data.mean():.2f}")
    print(f"  Median: {health_data.median():.2f}")
    print(f"  Std Dev: {health_data.std():.2f}")
    print(f"  Min: {health_data.min():.2f}")
    print(f"  Max: {health_data.max():.2f}")
    print(f"  25th percentile: {health_data.quantile(0.25):.2f}")
    print(f"  75th percentile: {health_data.quantile(0.75):.2f}")

    # Categorize soil health
    print(f"\n{health_col} Categories:")
    health_categories = pd.cut(health_data, bins=[0, 2, 5, 10, 25],
                               labels=['Poor (0-2)', 'Fair (2-5)', 'Good (5-10)', 'Excellent (10+)'])
    print(health_categories.value_counts().sort_index())

# Nutrient Availability Analysis
print(f"\n{'='*80}")
print(f"NUTRIENT AVAILABILITY PATTERNS")
print(f"{'='*80}")

nutrient_cols = {
    'Nitrogen': ['Available N', 'Available N, lbs/A', 'H3A Nitrate', 'H3A Nitrate, ppm NO3-N'],
    'Phosphorus': ['Available P', 'Available P, lbs/A', 'H3A Total Phosphorus', 'H3A Total Phosphorus, ppm P'],
    'Potassium': ['Available K', 'Available K, lbs/A', 'H3A ICAP Potassium', 'H3A Potassium, ppm K']
}

nutrient_summary = []
for nutrient, possible_cols in nutrient_cols.items():
    for col in possible_cols:
        if col in data.columns and data[col].notna().sum() > 50:
            values = data[col].dropna()
            nutrient_summary.append({
                'Nutrient': nutrient,
                'Measure': col,
                'Count': len(values),
                'Mean': values.mean(),
                'Median': values.median(),
                'Std': values.std(),
                'Min': values.min(),
                'Max': values.max()
            })
            break

nutrient_df = pd.DataFrame(nutrient_summary)
print(nutrient_df.round(2).to_string(index=False))

# Organic Matter Analysis
print(f"\n{'='*80}")
print(f"ORGANIC MATTER ANALYSIS")
print(f"{'='*80}")

om_cols = ['Organic Matter', 'Organic Matter, % LOI']
for col in om_cols:
    if col in data.columns and data[col].notna().sum() > 50:
        om_data = data[col].dropna()
        print(f"\n{col}:")
        print(f"  Mean: {om_data.mean():.2f}%")
        print(f"  Median: {om_data.median():.2f}%")
        print(f"  Range: {om_data.min():.2f}% - {om_data.max():.2f}%")

        # Categorize
        print(f"\n  Organic Matter Categories:")
        if om_data.max() > 10:  # Likely percentage
            om_categories = pd.cut(om_data, bins=[0, 1, 2, 3, 100],
                                  labels=['Very Low (<1%)', 'Low (1-2%)', 'Medium (2-3%)', 'High (3%+)'])
        else:
            om_categories = pd.cut(om_data, bins=[0, 0.5, 1.0, 2.0, 100],
                                  labels=['Very Low (<0.5%)', 'Low (0.5-1%)', 'Medium (1-2%)', 'High (2%+)'])
        print(om_categories.value_counts().sort_index())
        break

# pH Analysis
print(f"\n{'='*80}")
print(f"SOIL pH ANALYSIS")
print(f"{'='*80}")

ph_cols = ['Soil pH 1:1', '1:1 Soil pH']
for col in ph_cols:
    if col in data.columns and data[col].notna().sum() > 50:
        ph_data = data[col].dropna()
        print(f"\n{col}:")
        print(f"  Mean: {ph_data.mean():.2f}")
        print(f"  Median: {ph_data.median():.2f}")
        print(f"  Range: {ph_data.min():.2f} - {ph_data.max():.2f}")

        # Categorize pH
        print(f"\n  pH Categories:")
        ph_categories = pd.cut(ph_data, bins=[0, 5.5, 6.5, 7.5, 14],
                              labels=['Acidic (<5.5)', 'Slightly Acidic (5.5-6.5)',
                                     'Neutral (6.5-7.5)', 'Alkaline (7.5+)'])
        print(ph_categories.value_counts().sort_index())
        break

# N-P-K Balance Analysis
print(f"\n{'='*80}")
print(f"N-P-K BALANCE ANALYSIS")
print(f"{'='*80}")

# Find available N, P, K columns
n_col = None
p_col = None
k_col = None

for col in ['Available N', 'Available N, lbs/A']:
    if col in data.columns and data[col].notna().sum() > 50:
        n_col = col
        break

for col in ['Available P', 'Available P, lbs/A']:
    if col in data.columns and data[col].notna().sum() > 50:
        p_col = col
        break

for col in ['Available K', 'Available K, lbs/A']:
    if col in data.columns and data[col].notna().sum() > 50:
        k_col = col
        break

if n_col and p_col and k_col:
    npk_data = data[[n_col, p_col, k_col]].dropna()
    print(f"\nSamples with complete N-P-K data: {len(npk_data)}")

    # Calculate ratios
    npk_data['N:P'] = npk_data[n_col] / npk_data[p_col].replace(0, np.nan)
    npk_data['N:K'] = npk_data[n_col] / npk_data[k_col].replace(0, np.nan)
    npk_data['P:K'] = npk_data[p_col] / npk_data[k_col].replace(0, np.nan)

    print(f"\nNutrient Ratios:")
    print(f"  N:P ratio - Mean: {npk_data['N:P'].mean():.2f}, Median: {npk_data['N:P'].median():.2f}")
    print(f"  N:K ratio - Mean: {npk_data['N:K'].mean():.2f}, Median: {npk_data['N:K'].median():.2f}")
    print(f"  P:K ratio - Mean: {npk_data['P:K'].mean():.2f}, Median: {npk_data['P:K'].median():.2f}")

# Traditional vs Haney Test Comparison
print(f"\n{'='*80}")
print(f"TRADITIONAL VS HANEY TEST N RECOMMENDATIONS")
print(f"{'='*80}")

trad_cols = ['Traditional N', 'Traditional Test N, lbs/A']
haney_cols = ['Haney Test N', 'Haney Test N, lbs/A']
diff_cols = ['Lbs N Difference', 'N Difference, lbs/A']
savings_cols = ['N savings', 'N Savings, $']

trad_col = next((col for col in trad_cols if col in data.columns and data[col].notna().sum() > 50), None)
haney_col = next((col for col in haney_cols if col in data.columns and data[col].notna().sum() > 50), None)
diff_col = next((col for col in diff_cols if col in data.columns and data[col].notna().sum() > 50), None)
savings_col = next((col for col in savings_cols if col in data.columns and data[col].notna().sum() > 50), None)

if trad_col and haney_col:
    comparison_data = data[[trad_col, haney_col]].dropna()
    print(f"\nSamples with both tests: {len(comparison_data)}")
    print(f"\nTraditional Test N:")
    print(f"  Mean: {comparison_data[trad_col].mean():.2f} lbs/A")
    print(f"  Median: {comparison_data[trad_col].median():.2f} lbs/A")

    print(f"\nHaney Test N:")
    print(f"  Mean: {comparison_data[haney_col].mean():.2f} lbs/A")
    print(f"  Median: {comparison_data[haney_col].median():.2f} lbs/A")

    if diff_col:
        diff_data = data[diff_col].dropna()
        print(f"\nN Difference (Traditional - Haney):")
        print(f"  Mean: {diff_data.mean():.2f} lbs/A")
        print(f"  Median: {diff_data.median():.2f} lbs/A")

    if savings_col:
        savings_data = data[savings_col].dropna()
        print(f"\nPotential N Savings:")
        print(f"  Mean: ${savings_data.mean():.2f}")
        print(f"  Median: ${savings_data.median():.2f}")
        print(f"  Total potential savings: ${savings_data.sum():.2f}")

# Visualizations
print(f"\n{'='*80}")
print(f"GENERATING ADVANCED VISUALIZATIONS")
print(f"{'='*80}")

# 1. Soil Health Score distribution with categories
if health_col in data.columns:
    fig, ax = plt.subplots(figsize=(12, 8))
    health_data = data[health_col].dropna()
    ax.hist(health_data, bins=50, edgecolor='black', alpha=0.7, color='forestgreen')
    ax.axvline(health_data.median(), color='red', linestyle='--', linewidth=2, label=f'Median: {health_data.median():.2f}')
    ax.axvline(health_data.mean(), color='blue', linestyle='--', linewidth=2, label=f'Mean: {health_data.mean():.2f}')
    ax.set_xlabel(health_col, fontsize=12)
    ax.set_ylabel('Frequency', fontsize=12)
    ax.set_title(f'Distribution of {health_col}', fontsize=14)
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('/Users/deyus-ex-machina/agwise/soil_health_distribution.png', dpi=300, bbox_inches='tight')
    print("✓ Soil health distribution plot saved")
    plt.close()

# 2. N-P-K availability comparison
if n_col and p_col and k_col:
    npk_compare = data[[n_col, p_col, k_col]].dropna()
    if len(npk_compare) > 0:
        fig, ax = plt.subplots(figsize=(10, 8))
        npk_compare.boxplot(ax=ax)
        ax.set_ylabel('Availability (lbs/A)', fontsize=12)
        ax.set_title('N-P-K Nutrient Availability Distribution', fontsize=14)
        ax.grid(True, alpha=0.3)
        plt.xticks(rotation=0)
        plt.tight_layout()
        plt.savefig('/Users/deyus-ex-machina/agwise/npk_comparison.png', dpi=300, bbox_inches='tight')
        print("✓ N-P-K comparison plot saved")
        plt.close()

# 3. Traditional vs Haney comparison
if trad_col and haney_col:
    comparison_data = data[[trad_col, haney_col]].dropna()
    if len(comparison_data) > 0:
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

        # Scatter plot
        ax1.scatter(comparison_data[trad_col], comparison_data[haney_col], alpha=0.5, s=30)
        ax1.plot([0, comparison_data[trad_col].max()], [0, comparison_data[trad_col].max()],
                'r--', linewidth=2, label='1:1 Line')
        ax1.set_xlabel(trad_col, fontsize=11)
        ax1.set_ylabel(haney_col, fontsize=11)
        ax1.set_title('Traditional vs Haney Test N Recommendations', fontsize=12)
        ax1.legend()
        ax1.grid(True, alpha=0.3)

        # Box plot comparison
        comparison_data.boxplot(ax=ax2)
        ax2.set_ylabel('N Recommendation (lbs/A)', fontsize=11)
        ax2.set_title('Distribution Comparison', fontsize=12)
        ax2.grid(True, alpha=0.3)

        plt.tight_layout()
        plt.savefig('/Users/deyus-ex-machina/agwise/traditional_vs_haney.png', dpi=300, bbox_inches='tight')
        print("✓ Traditional vs Haney comparison plot saved")
        plt.close()

# 4. Organic Matter vs Soil Health
om_col = 'Organic Matter, % LOI' if 'Organic Matter, % LOI' in data.columns else 'Organic Matter'
if om_col in data.columns and health_col in data.columns:
    om_health = data[[om_col, health_col]].dropna()
    if len(om_health) > 0:
        fig, ax = plt.subplots(figsize=(12, 8))
        ax.scatter(om_health[om_col], om_health[health_col], alpha=0.5, s=30)
        ax.set_xlabel(om_col, fontsize=12)
        ax.set_ylabel(health_col, fontsize=12)
        ax.set_title(f'{health_col} vs {om_col}', fontsize=14)
        ax.grid(True, alpha=0.3)

        # Add correlation
        corr = om_health[om_col].corr(om_health[health_col])
        ax.text(0.05, 0.95, f'Correlation: {corr:.3f}', transform=ax.transAxes,
               fontsize=12, verticalalignment='top',
               bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

        plt.tight_layout()
        plt.savefig('/Users/deyus-ex-machina/agwise/om_vs_health.png', dpi=300, bbox_inches='tight')
        print("✓ Organic matter vs soil health plot saved")
        plt.close()

print(f"\n{'='*80}")
print(f"ADVANCED INSIGHTS ANALYSIS COMPLETE")
print(f"{'='*80}")
