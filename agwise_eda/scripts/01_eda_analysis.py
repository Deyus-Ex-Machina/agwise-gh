import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

# Set style for visualizations
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)

# Load all CSV files from ALL batches
data_base = Path('/Users/deyus-ex-machina/agwise/data')
batch_dirs = [
    data_base / 'OneDrive_1_10-5-2025',
    data_base / 'OneDrive_2_10-6-2025',
    data_base / 'OneDrive_4_10-6-2025'
]

# Also include loose CSV files in data directory (batch 3)
all_csv_files = []
for batch_dir in batch_dirs:
    if batch_dir.exists():
        all_csv_files.extend(list(batch_dir.glob('*.csv')))
        print(f"Batch {batch_dir.name}: {len(list(batch_dir.glob('*.csv')))} files")

# Add loose CSV files (batch 3)
loose_csvs = [f for f in data_base.glob('*.csv') if f.is_file()]
if loose_csvs:
    all_csv_files.extend(loose_csvs)
    print(f"Batch 3 (loose files): {len(loose_csvs)} files")

print(f"\nTotal CSV files found: {len(all_csv_files)}")
print("=" * 80)

# Load all data into a single dataframe
dfs = []
batch_tracker = []
for i, file in enumerate(all_csv_files):
    try:
        df = pd.read_csv(file)

        # Track which batch this came from
        if 'OneDrive_1' in str(file):
            batch = 'Batch_1'
        elif 'OneDrive_2' in str(file):
            batch = 'Batch_2'
        elif 'OneDrive_4' in str(file):
            batch = 'Batch_4'
        else:
            batch = 'Batch_3'

        df['_source_batch'] = batch
        df['_source_file'] = file.name

        dfs.append(df)
        if i == 0:
            print(f"Sample file: {file.name}")
            print(f"Columns: {len(df.columns)}")
            print(f"Rows per file: {len(df)}")
    except Exception as e:
        print(f"Error reading {file.name}: {e}")

# Combine all dataframes
data = pd.concat(dfs, ignore_index=True)
print(f"\n{'='*80}")
print(f"COMBINED DATASET OVERVIEW")
print(f"{'='*80}")
print(f"Total samples: {len(data)}")
print(f"Total columns: {len(data.columns)}")
print(f"\nColumn names:")
for i, col in enumerate(data.columns, 1):
    print(f"{i}. {col}")

# Save combined dataset
data.to_csv('/Users/deyus-ex-machina/agwise/combined_soil_data.csv', index=False)
print(f"\n✓ Combined dataset saved to: combined_soil_data.csv")

# Data shape and basic info
print(f"\n{'='*80}")
print(f"DATA STRUCTURE")
print(f"{'='*80}")
print(f"Shape: {data.shape}")
print(f"\nData types:")
print(data.dtypes.value_counts())

# Identify numeric and categorical columns
numeric_cols = data.select_dtypes(include=[np.number]).columns.tolist()
categorical_cols = data.select_dtypes(include=['object']).columns.tolist()

print(f"\n{'='*80}")
print(f"COLUMN CLASSIFICATION")
print(f"{'='*80}")
print(f"Numeric columns: {len(numeric_cols)}")
print(f"Categorical columns: {len(categorical_cols)}")

# Missing values analysis
print(f"\n{'='*80}")
print(f"MISSING VALUES ANALYSIS")
print(f"{'='*80}")
missing = pd.DataFrame({
    'Column': data.columns,
    'Missing_Count': data.isnull().sum(),
    'Missing_Percentage': (data.isnull().sum() / len(data) * 100).round(2)
})
missing = missing[missing['Missing_Count'] > 0].sort_values('Missing_Percentage', ascending=False)
print(f"\nColumns with missing values: {len(missing)}")
print(f"\nTop 20 columns with most missing values:")
print(missing.head(20).to_string(index=False))

# Save full missing values report
missing.to_csv('/Users/deyus-ex-machina/agwise/missing_values_report.csv', index=False)
print(f"\n✓ Full missing values report saved to: missing_values_report.csv")

# Check for duplicates
duplicates = data.duplicated().sum()
print(f"\n{'='*80}")
print(f"DUPLICATE ANALYSIS")
print(f"{'='*80}")
print(f"Duplicate rows: {duplicates} ({(duplicates/len(data)*100):.2f}%)")

# Descriptive statistics for key numeric columns
print(f"\n{'='*80}")
print(f"DESCRIPTIVE STATISTICS - KEY SOIL HEALTH METRICS")
print(f"{'='*80}")

key_metrics = [
    'Soil pH 1:1',
    '1:1 Electrical Conductivity, mmho/cm',
    'Organic Matter, % LOI',
    'Soil Respiration, ppm CO2-C',
    'H3A Nitrate, ppm NO3-N',
    'H3A Total Phosphorus, ppm P',
    'H3A Potassium, ppm K',
    'H3A Calcium, ppm Ca',
    'H3A Magnesium, ppm Mg',
    'Soil Health Score'
]

# Filter to metrics that exist in dataset
key_metrics = [col for col in key_metrics if col in data.columns]

if key_metrics:
    desc_stats = data[key_metrics].describe().T
    desc_stats['missing_%'] = missing.set_index('Column').loc[
        desc_stats.index.intersection(missing['Column']), 'Missing_Percentage'
    ].values if any(m in missing['Column'].values for m in key_metrics) else 0
    print(desc_stats.round(2))

    # Save descriptive statistics
    desc_stats.to_csv('/Users/deyus-ex-machina/agwise/descriptive_statistics.csv')
    print(f"\n✓ Descriptive statistics saved to: descriptive_statistics.csv")

# Categorical variables analysis
print(f"\n{'='*80}")
print(f"CATEGORICAL VARIABLES ANALYSIS")
print(f"{'='*80}")

key_categorical = ['Sample Type', 'Cover Crop Mix', 'Past Crop', 'Crop 1', 'Crop 2', 'Crop 3']
key_categorical = [col for col in key_categorical if col in data.columns]

cat_summary = []
for col in key_categorical:
    value_counts = data[col].value_counts()
    cat_summary.append({
        'Variable': col,
        'Unique_Values': data[col].nunique(),
        'Most_Common': value_counts.index[0] if len(value_counts) > 0 else 'N/A',
        'Most_Common_Count': value_counts.values[0] if len(value_counts) > 0 else 0,
        'Missing_%': (data[col].isnull().sum() / len(data) * 100).round(2)
    })

cat_summary_df = pd.DataFrame(cat_summary)
print(cat_summary_df.to_string(index=False))

# Detailed categorical analysis
for col in key_categorical[:3]:  # Top 3 categorical variables
    print(f"\n{col} - Top 10 values:")
    print(data[col].value_counts().head(10))

# Save categorical summary
cat_summary_df.to_csv('/Users/deyus-ex-machina/agwise/categorical_summary.csv', index=False)
print(f"\n✓ Categorical summary saved to: categorical_summary.csv")

print(f"\n{'='*80}")
print(f"DATA LOADING AND INITIAL ANALYSIS COMPLETE")
print(f"{'='*80}")
