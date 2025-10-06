import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

# Set style
sns.set_style("whitegrid")
sns.set_palette("husl")

# Load the combined dataset
data = pd.read_csv('/Users/deyus-ex-machina/agwise/combined_soil_data.csv')

print(f"{'='*80}")
print(f"ADVANCED DATA QUALITY ASSESSMENT")
print(f"{'='*80}")

# Remove completely empty columns (100% missing)
cols_to_drop = data.columns[data.isnull().all()].tolist()
print(f"\nColumns with 100% missing values (to be excluded from analysis): {len(cols_to_drop)}")

# Work with non-empty data
data_clean = data.drop(columns=cols_to_drop)

# Analyze duplicates more deeply
print(f"\n{'='*80}")
print(f"DETAILED DUPLICATE ANALYSIS")
print(f"{'='*80}")
print(f"Total rows: {len(data)}")
print(f"Duplicate rows: {data.duplicated().sum()} ({(data.duplicated().sum()/len(data)*100):.2f}%)")
print(f"Unique rows: {len(data.drop_duplicates())}")

# Check key identifier columns
key_cols = ['Lab No', 'Date Recd', 'Date Rept']
key_cols = [col for col in key_cols if col in data.columns]
if key_cols:
    print(f"\nDuplicates based on {key_cols}: {data[key_cols].duplicated().sum()}")

# Identify primary numeric columns for analysis
numeric_cols = data_clean.select_dtypes(include=[np.number]).columns.tolist()

# Focus on key soil health metrics that have data
key_metrics_v1 = [
    'Soil pH 1:1', '1:1 Electrical Conductivity, mmho/cm',
    'Organic Matter, % LOI', 'Soil Respiration, ppm CO2-C',
    'H3A Nitrate, ppm NO3-N', 'H3A Total Phosphorus, ppm P',
    'H3A Potassium, ppm K', 'H3A Calcium, ppm Ca',
    'Soil Health Score'
]

key_metrics_v2 = [
    '1:1 Soil pH', '1:1 Soluble Salt', 'Organic Matter',
    'CO2-C', 'H3A Nitrate', 'H3A Total Phosphorus',
    'H3A ICAP Potassium', 'H3A ICAP Calcium',
    'Soil Health Calculation'
]

# Determine which version of columns exists
available_metrics = []
for col in key_metrics_v1:
    if col in data.columns:
        available_metrics.append(col)
for col in key_metrics_v2:
    if col in data.columns and col not in available_metrics:
        available_metrics.append(col)

print(f"\n{'='*80}")
print(f"OUTLIER DETECTION")
print(f"{'='*80}")

outlier_summary = []
for col in available_metrics[:10]:  # Top 10 metrics
    if col in data.columns:
        values = pd.to_numeric(data[col], errors='coerce').dropna()
        if len(values) > 0:
            Q1 = values.quantile(0.25)
            Q3 = values.quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            outliers = ((values < lower_bound) | (values > upper_bound)).sum()

            outlier_summary.append({
                'Metric': col,
                'Count': len(values),
                'Outliers': outliers,
                'Outlier_%': (outliers/len(values)*100).round(2),
                'Min': values.min(),
                'Q1': Q1,
                'Median': values.median(),
                'Q3': Q3,
                'Max': values.max()
            })

outlier_df = pd.DataFrame(outlier_summary)
print(outlier_df.to_string(index=False))
outlier_df.to_csv('/Users/deyus-ex-machina/agwise/outlier_analysis.csv', index=False)
print(f"\n✓ Outlier analysis saved to: outlier_analysis.csv")

# Create visualizations
print(f"\n{'='*80}")
print(f"GENERATING VISUALIZATIONS")
print(f"{'='*80}")

# 1. Distribution plots for key metrics
fig, axes = plt.subplots(3, 3, figsize=(20, 16))
fig.suptitle('Distribution of Key Soil Health Metrics', fontsize=16, y=0.995)

for idx, col in enumerate(available_metrics[:9]):
    row = idx // 3
    col_idx = idx % 3
    ax = axes[row, col_idx]

    values = pd.to_numeric(data[col], errors='coerce').dropna()
    if len(values) > 0:
        ax.hist(values, bins=50, edgecolor='black', alpha=0.7)
        ax.set_xlabel(col, fontsize=10)
        ax.set_ylabel('Frequency', fontsize=10)
        ax.set_title(f'{col}\nMean: {values.mean():.2f}, Median: {values.median():.2f}',
                     fontsize=9)
        ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('/Users/deyus-ex-machina/agwise/distributions.png', dpi=300, bbox_inches='tight')
print("✓ Distribution plots saved to: distributions.png")
plt.close()

# 2. Box plots for outlier visualization
fig, axes = plt.subplots(3, 3, figsize=(20, 16))
fig.suptitle('Box Plots - Outlier Detection for Key Soil Metrics', fontsize=16, y=0.995)

for idx, col in enumerate(available_metrics[:9]):
    row = idx // 3
    col_idx = idx % 3
    ax = axes[row, col_idx]

    values = pd.to_numeric(data[col], errors='coerce').dropna()
    if len(values) > 0:
        ax.boxplot(values, vert=True)
        ax.set_ylabel(col, fontsize=10)
        ax.set_title(f'{col}', fontsize=10)
        ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('/Users/deyus-ex-machina/agwise/boxplots.png', dpi=300, bbox_inches='tight')
print("✓ Box plots saved to: boxplots.png")
plt.close()

# 3. Missing values heatmap
missing_cols = data.columns[data.isnull().any()].tolist()[:30]  # Top 30 columns with missing
missing_matrix = data[missing_cols].isnull().astype(int)

fig, ax = plt.subplots(figsize=(14, 10))
sns.heatmap(missing_matrix.iloc[:200], cmap='RdYlGn_r', cbar_kws={'label': 'Missing'},
            yticklabels=False, ax=ax)
ax.set_title('Missing Values Pattern (First 200 Samples, Top 30 Columns)', fontsize=14)
ax.set_xlabel('Columns', fontsize=12)
ax.set_ylabel('Samples', fontsize=12)
plt.xticks(rotation=45, ha='right', fontsize=8)
plt.tight_layout()
plt.savefig('/Users/deyus-ex-machina/agwise/missing_pattern.png', dpi=300, bbox_inches='tight')
print("✓ Missing values pattern saved to: missing_pattern.png")
plt.close()

print(f"\n{'='*80}")
print(f"DATA QUALITY ASSESSMENT COMPLETE")
print(f"{'='*80}")
