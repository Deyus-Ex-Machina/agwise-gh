#!/usr/bin/env python3
"""
COMPREHENSIVE EDA PIPELINE - FULL DATASET ANALYSIS
Complete re-analysis with all 870 CSV files

This script performs:
1. Data loading from all batches
2. Comprehensive data quality assessment
3. Descriptive statistics
4. Distribution analysis
5. Correlation analysis
6. Categorical analysis
7. Advanced insights
8. Complete visualization suite

Author: Claude Code
Date: October 6, 2025 (Updated)
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

# Configuration
sns.set_style("whitegrid")
sns.set_palette("husl")
plt.rcParams['figure.figsize'] = (14, 10)

# Paths
BASE_DIR = Path('/Users/deyus-ex-machina/agwise')
DATA_DIR = BASE_DIR / 'data'
OUTPUT_DIR = BASE_DIR / 'agwise_eda'
VIZ_DIR = OUTPUT_DIR / 'outputs' / 'visualizations'
TABLE_DIR = OUTPUT_DIR / 'outputs' / 'tables'

# Create directories
VIZ_DIR.mkdir(parents=True, exist_ok=True)
TABLE_DIR.mkdir(parents=True, exist_ok=True)

print("="*80)
print("COMPREHENSIVE EDA PIPELINE - FULL DATASET")
print("="*80)
print(f"Start Time: {pd.Timestamp.now()}")
print("="*80)

# ============================================================================
# SECTION 1: DATA LOADING
# ============================================================================
print("\n" + "="*80)
print("SECTION 1: DATA LOADING AND INTEGRATION")
print("="*80)

# Find all CSV files
csv_files = list(DATA_DIR.glob('**/*.csv'))
print(f"\nTotal CSV files found: {len(csv_files)}")

# Group by batch
batches = {}
for file in csv_files:
    batch_name = file.parent.name
    if batch_name not in batches:
        batches[batch_name] = []
    batches[batch_name].append(file)

print(f"\nBatches identified:")
for batch_name, files in batches.items():
    print(f"  - {batch_name}: {len(files)} files")

# Load all data
print(f"\nLoading all {len(csv_files)} CSV files...")
dfs = []
load_errors = []

for i, file in enumerate(csv_files, 1):
    if i % 100 == 0:
        print(f"  Loading file {i}/{len(csv_files)}...")
    try:
        df = pd.read_csv(file)
        df['_source_file'] = file.name
        df['_source_batch'] = file.parent.name
        dfs.append(df)
    except Exception as e:
        load_errors.append((file.name, str(e)))

print(f"\n✓ Successfully loaded: {len(dfs)} files")
if load_errors:
    print(f"✗ Failed to load: {len(load_errors)} files")
    for fname, error in load_errors[:5]:
        print(f"    {fname}: {error}")

# Combine all dataframes
print(f"\nMerging all dataframes...")
data = pd.concat(dfs, ignore_index=True)

print(f"\n" + "="*80)
print(f"COMBINED DATASET OVERVIEW")
print(f"="*80)
print(f"Total Samples: {len(data):,}")
print(f"Total Variables: {len(data.columns)}")
print(f"Memory Usage: {data.memory_usage(deep=True).sum() / 1024**2:.2f} MB")

# Save combined dataset
combined_path = OUTPUT_DIR / 'data' / 'processed' / 'combined_soil_data_FULL.csv'
combined_path.parent.mkdir(parents=True, exist_ok=True)
data.to_csv(combined_path, index=False)
print(f"\n✓ Saved combined dataset: {combined_path}")

# ============================================================================
# SECTION 2: DATA QUALITY ASSESSMENT
# ============================================================================
print("\n" + "="*80)
print("SECTION 2: DATA QUALITY ASSESSMENT")
print("="*80)

# Basic structure
print(f"\nDataset Shape: {data.shape}")
print(f"\nData Types:")
print(data.dtypes.value_counts())

# Identify column types
numeric_cols = data.select_dtypes(include=[np.number]).columns.tolist()
categorical_cols = data.select_dtypes(include=['object']).columns.tolist()

# Remove metadata columns
metadata_cols = ['_source_file', '_source_batch']
categorical_cols = [col for col in categorical_cols if col not in metadata_cols]

print(f"\nColumn Classification:")
print(f"  Numeric: {len(numeric_cols)}")
print(f"  Categorical: {len(categorical_cols)}")
print(f"  Metadata: {len(metadata_cols)}")

# Missing values analysis
print(f"\n" + "-"*80)
print("MISSING VALUES ANALYSIS")
print("-"*80)

missing_summary = pd.DataFrame({
    'Column': data.columns,
    'Missing_Count': data.isnull().sum(),
    'Missing_Percentage': (data.isnull().sum() / len(data) * 100).round(2),
    'Data_Type': data.dtypes.astype(str)
})
missing_summary = missing_summary[missing_summary['Missing_Count'] > 0].sort_values(
    'Missing_Percentage', ascending=False
)

print(f"\nColumns with missing values: {len(missing_summary)}/{len(data.columns)}")
print(f"\nTop 20 columns with most missing data:")
print(missing_summary.head(20).to_string(index=False))

# Save missing values report
missing_summary.to_csv(TABLE_DIR / 'missing_values_report_FULL.csv', index=False)
print(f"\n✓ Saved: missing_values_report_FULL.csv")

# Duplicate analysis
duplicates = data.duplicated().sum()
print(f"\n" + "-"*80)
print("DUPLICATE ANALYSIS")
print("-"*80)
print(f"Duplicate rows: {duplicates:,} ({(duplicates/len(data)*100):.2f}%)")
print(f"Unique rows: {len(data) - duplicates:,}")

# Check key identifier duplicates
key_cols = ['Lab No', 'Date Recd', 'Date Rept']
existing_keys = [col for col in key_cols if col in data.columns]
if existing_keys:
    key_duplicates = data[existing_keys].duplicated().sum()
    print(f"Duplicates by {existing_keys}: {key_duplicates:,}")

# Batch-level statistics
print(f"\n" + "-"*80)
print("BATCH-LEVEL STATISTICS")
print("-"*80)
batch_stats = data.groupby('_source_batch').size().sort_index()
print(batch_stats)

# ============================================================================
# SECTION 3: DESCRIPTIVE STATISTICS
# ============================================================================
print("\n" + "="*80)
print("SECTION 3: DESCRIPTIVE STATISTICS")
print("="*80)

# Key soil health metrics (identify which naming convention exists)
key_metrics_v1 = [
    'Soil pH 1:1', '1:1 Electrical Conductivity, mmho/cm',
    'Organic Matter, % LOI', 'Soil Respiration, ppm CO2-C',
    'H3A Nitrate, ppm NO3-N', 'H3A Total Phosphorus, ppm P',
    'H3A Potassium, ppm K', 'H3A Calcium, ppm Ca',
    'H3A Magnesium, ppm Mg', 'Soil Health Score'
]

key_metrics_v2 = [
    '1:1 Soil pH', '1:1 Soluble Salt',
    'Organic Matter', 'CO2-C',
    'H3A Nitrate', 'H3A Total Phosphorus',
    'H3A ICAP Potassium', 'H3A ICAP Calcium',
    'H3A ICAP Magnesium', 'Soil Health Calculation'
]

# Find available metrics
available_metrics = []
for col in key_metrics_v1 + key_metrics_v2:
    if col in data.columns and col not in available_metrics:
        non_null = data[col].notna().sum()
        if non_null > 50:  # Only include if sufficient data
            available_metrics.append(col)

print(f"\nAvailable key metrics: {len(available_metrics)}")
for i, col in enumerate(available_metrics, 1):
    print(f"{i:2d}. {col:50s} (n={data[col].notna().sum():,})")

# Compute descriptive statistics
desc_stats = data[available_metrics].describe().T
desc_stats['missing_count'] = len(data) - data[available_metrics].notna().sum()
desc_stats['missing_pct'] = (desc_stats['missing_count'] / len(data) * 100).round(2)
desc_stats['cv'] = (desc_stats['std'] / desc_stats['mean'] * 100).round(2)

print(f"\nDescriptive Statistics (Key Metrics):")
print(desc_stats[['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max', 'cv']].round(2))

# Save descriptive statistics
desc_stats.to_csv(TABLE_DIR / 'descriptive_statistics_FULL.csv')
print(f"\n✓ Saved: descriptive_statistics_FULL.csv")

# ============================================================================
# SECTION 4: OUTLIER DETECTION
# ============================================================================
print("\n" + "="*80)
print("SECTION 4: OUTLIER DETECTION")
print("="*80)

outlier_summary = []
for col in available_metrics[:15]:  # Top 15 metrics
    try:
        values = data[col].dropna()
        # Ensure numeric type
        values = pd.to_numeric(values, errors='coerce').dropna()
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
                'Lower_Bound': lower_bound,
                'Upper_Bound': upper_bound,
                'Min': values.min(),
                'Q1': Q1,
                'Median': values.median(),
                'Q3': Q3,
                'Max': values.max()
            })
    except Exception as e:
        print(f"  ⚠ Skipping {col}: {str(e)}")
        continue

outlier_df = pd.DataFrame(outlier_summary)
print(f"\nOutlier Analysis (IQR Method, 1.5×IQR):")
print(outlier_df[['Metric', 'Count', 'Outliers', 'Outlier_%', 'Min', 'Median', 'Max']].to_string(index=False))

# Save outlier analysis
outlier_df.to_csv(TABLE_DIR / 'outlier_analysis_FULL.csv', index=False)
print(f"\n✓ Saved: outlier_analysis_FULL.csv")

print(f"\n{'='*80}")
print("SECTION 1-4 COMPLETE - Data Loading and Quality Assessment Done")
print(f"{'='*80}")
print(f"\nNext: Run correlation and visualization analysis...")
print(f"Time elapsed: {pd.Timestamp.now()}")
