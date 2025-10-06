#!/usr/bin/env python3
"""
CATEGORICAL & ADVANCED ANALYSIS - FULL DATASET
Crop analysis, cover crop patterns, N-P-K analysis, and economic insights

Author: Claude Code
Date: October 6, 2025
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

# Configuration
sns.set_style("whitegrid")
plt.rcParams['figure.dpi'] = 300

# Paths
BASE_DIR = Path('/Users/deyus-ex-machina/agwise/agwise_eda')
DATA_FILE = BASE_DIR / 'data' / 'processed' / 'combined_soil_data_FULL.csv'
VIZ_DIR = BASE_DIR / 'outputs' / 'visualizations'
TABLE_DIR = BASE_DIR / 'outputs' / 'tables'

print("="*80)
print("CATEGORICAL & ADVANCED ANALYSIS - FULL DATASET")
print("="*80)

# Load data
print("\nLoading data...")
data = pd.read_csv(DATA_FILE)
print(f"✓ Loaded {len(data):,} samples")

# ============================================================================
# SECTION 1: CATEGORICAL ANALYSIS
# ============================================================================
print("\n" + "="*80)
print("SECTION 1: CROP AND COVER CROP ANALYSIS")
print("="*80)

# Analyze cover crop mixes
cover_cols = ['Cover Crop Mix', 'Cover crop mix']
for col in cover_cols:
    if col in data.columns and data[col].notna().sum() > 50:
        print(f"\n{col} Distribution:")
        value_counts = data[col].value_counts()
        print(f"  Unique values: {len(value_counts)}")
        print(f"  Non-missing: {data[col].notna().sum():,}")
        print("\n  Top 10:")
        for mix, count in value_counts.head(10).items():
            pct = (count / data[col].notna().sum() * 100)
            print(f"    {mix}: {count:,} ({pct:.1f}%)")

        # Visualize
        if len(value_counts) < 15:
            fig, ax = plt.subplots(figsize=(12, 8))
            value_counts.plot(kind='bar', ax=ax, color='forestgreen')
            ax.set_xlabel('Cover Crop Mix', fontsize=12, fontweight='bold')
            ax.set_ylabel('Count', fontsize=12)
            ax.set_title(f'Distribution of {col} (n={data[col].notna().sum():,})',
                        fontsize=14, fontweight='bold')
            ax.grid(axis='y', alpha=0.3)
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            filename = col.lower().replace(' ', '_')
            plt.savefig(VIZ_DIR / f'{filename}_distribution_FULL.png', dpi=300, bbox_inches='tight')
            print(f"  ✓ Saved: {filename}_distribution_FULL.png")
            plt.close()

# Analyze crops
crop_cols = ['Crop 1', 'Crop 2', 'Crop 3', 'Past Crop']
crop_summary = []
for col in crop_cols:
    if col in data.columns:
        value_counts = data[col].value_counts()
        if len(value_counts) > 0:
            crop_summary.append({
                'Variable': col,
                'Unique_Values': len(value_counts),
                'Most_Common': value_counts.index[0],
                'Most_Common_Count': value_counts.values[0],
                'Non_Missing': data[col].notna().sum(),
                'Missing_%': (data[col].isnull().sum() / len(data) * 100).round(2)
            })

if crop_summary:
    crop_df = pd.DataFrame(crop_summary)
    print(f"\n\nCrop Variables Summary:")
    print(crop_df.to_string(index=False))
    crop_df.to_csv(TABLE_DIR / 'crop_summary_FULL.csv', index=False)
    print(f"\n✓ Saved: crop_summary_FULL.csv")

# Crop 1 distribution
if 'Crop 1' in data.columns and data['Crop 1'].notna().sum() > 20:
    crop1_counts = data['Crop 1'].value_counts().head(15)
    fig, ax = plt.subplots(figsize=(14, 8))
    crop1_counts.plot(kind='barh', ax=ax, color='steelblue')
    ax.set_xlabel('Count', fontsize=12, fontweight='bold')
    ax.set_ylabel('Crop Type', fontsize=12)
    ax.set_title(f'Top 15 Recommended Crops (n={data["Crop 1"].notna().sum():,})',
                fontsize=14, fontweight='bold')
    ax.grid(axis='x', alpha=0.3)
    plt.tight_layout()
    plt.savefig(VIZ_DIR / 'crop_distribution_FULL.png', dpi=300, bbox_inches='tight')
    print("✓ Saved: crop_distribution_FULL.png")
    plt.close()

# ============================================================================
# SECTION 2: SOIL HEALTH BY COVER CROP
# ============================================================================
print("\n" + "="*80)
print("SECTION 2: SOIL HEALTH BY COVER CROP MIX")
print("="*80)

health_col = 'Soil Health Calculation' if 'Soil Health Calculation' in data.columns else 'Soil Health Score'

for cover_col in cover_cols:
    if cover_col in data.columns and health_col in data.columns:
        cover_health = data[[cover_col, health_col]].copy()
        cover_health[health_col] = pd.to_numeric(cover_health[health_col], errors='coerce')
        cover_health = cover_health.dropna()

        if len(cover_health) > 50:
            print(f"\n{health_col} by {cover_col}:")

            health_by_cover = cover_health.groupby(cover_col)[health_col].agg([
                'count', 'mean', 'median', 'std', 'min', 'max'
            ]).sort_values('mean', ascending=False)

            print(health_by_cover.round(2))

            # Save
            health_by_cover.to_csv(TABLE_DIR / f'soil_health_by_{cover_col.lower().replace(" ", "_")}_FULL.csv')
            print(f"✓ Saved: soil_health_by_{cover_col.lower().replace(' ', '_')}_FULL.csv")

            # Visualize
            if len(health_by_cover) < 15:
                fig, ax = plt.subplots(figsize=(14, 8))
                cover_health.boxplot(column=health_col, by=cover_col, ax=ax)
                ax.set_xlabel('Cover Crop Mix', fontsize=12, fontweight='bold')
                ax.set_ylabel(health_col, fontsize=12)
                ax.set_title(f'{health_col} by Cover Crop Mix (n={len(cover_health):,})',
                            fontsize=14, fontweight='bold')
                plt.suptitle('')
                plt.xticks(rotation=45, ha='right')
                plt.tight_layout()
                plt.savefig(VIZ_DIR / 'soil_health_by_cover_boxplot_FULL.png', dpi=300, bbox_inches='tight')
                print("✓ Saved: soil_health_by_cover_boxplot_FULL.png")
                plt.close()

# ============================================================================
# SECTION 3: NUTRIENT AVAILABILITY ANALYSIS
# ============================================================================
print("\n" + "="*80)
print("SECTION 3: N-P-K NUTRIENT AVAILABILITY")
print("="*80)

# Find N, P, K columns
nutrient_cols = {
    'Nitrogen': ['Available N', 'H3A Nitrate'],
    'Phosphorus': ['Available P', 'H3A Total Phosphorus'],
    'Potassium': ['Available K', 'H3A ICAP Potassium']
}

npk_cols = []
for nutrient, possible_cols in nutrient_cols.items():
    for col in possible_cols:
        if col in data.columns and data[col].notna().sum() > 500:
            npk_cols.append(col)
            values = pd.to_numeric(data[col], errors='coerce').dropna()
            print(f"\n{col}:")
            print(f"  Count: {len(values):,}")
            print(f"  Mean: {values.mean():.2f}")
            print(f"  Median: {values.median():.2f}")
            print(f"  Std: {values.std():.2f}")
            print(f"  Range: {values.min():.2f} - {values.max():.2f}")
            break

# N-P-K comparison visualization
if len(npk_cols) >= 3:
    npk_compare = data[npk_cols].apply(pd.to_numeric, errors='coerce').dropna()
    if len(npk_compare) > 0:
        fig, ax = plt.subplots(figsize=(12, 8))
        npk_compare.boxplot(ax=ax)
        ax.set_ylabel('Availability', fontsize=12, fontweight='bold')
        ax.set_title(f'N-P-K Nutrient Availability Distribution (n={len(npk_compare):,})',
                    fontsize=14, fontweight='bold')
        ax.grid(axis='y', alpha=0.3)
        plt.xticks(rotation=0, fontsize=10)
        plt.tight_layout()
        plt.savefig(VIZ_DIR / 'npk_comparison_FULL.png', dpi=300, bbox_inches='tight')
        print("\n✓ Saved: npk_comparison_FULL.png")
        plt.close()

# ============================================================================
# SECTION 4: TRADITIONAL VS HANEY TEST
# ============================================================================
print("\n" + "="*80)
print("SECTION 4: TRADITIONAL VS HANEY TEST COMPARISON")
print("="*80)

trad_cols = ['Traditional N', 'Traditional Test N, lbs/A']
haney_cols = ['Haney Test N', 'Haney Test N, lbs/A']

trad_col = next((col for col in trad_cols if col in data.columns and data[col].notna().sum() > 100), None)
haney_col = next((col for col in haney_cols if col in data.columns and data[col].notna().sum() > 100), None)

if trad_col and haney_col:
    comparison_data = data[[trad_col, haney_col]].apply(pd.to_numeric, errors='coerce').dropna()

    if len(comparison_data) > 0:
        print(f"\nSamples with both tests: {len(comparison_data):,}")
        print(f"\nTraditional Test N:")
        print(f"  Mean: {comparison_data[trad_col].mean():.2f} lbs/A")
        print(f"  Median: {comparison_data[trad_col].median():.2f} lbs/A")

        print(f"\nHaney Test N:")
        print(f"  Mean: {comparison_data[haney_col].mean():.2f} lbs/A")
        print(f"  Median: {comparison_data[haney_col].median():.2f} lbs/A")

        diff = comparison_data[haney_col] - comparison_data[trad_col]
        print(f"\nDifference (Haney - Traditional):")
        print(f"  Mean: {diff.mean():.2f} lbs/A")
        print(f"  Median: {diff.median():.2f} lbs/A")

        # Visualization
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

        # Scatter plot
        ax1.scatter(comparison_data[trad_col], comparison_data[haney_col],
                   alpha=0.4, s=20)
        max_val = max(comparison_data[trad_col].max(), comparison_data[haney_col].max())
        ax1.plot([0, max_val], [0, max_val], 'r--', linewidth=2, label='1:1 Line')
        ax1.set_xlabel(trad_col, fontsize=11, fontweight='bold')
        ax1.set_ylabel(haney_col, fontsize=11)
        ax1.set_title(f'Traditional vs Haney Test (n={len(comparison_data):,})', fontsize=12)
        ax1.legend()
        ax1.grid(True, alpha=0.3)

        # Box plot
        comparison_data.boxplot(ax=ax2)
        ax2.set_ylabel('N Recommendation (lbs/A)', fontsize=11, fontweight='bold')
        ax2.set_title('Distribution Comparison', fontsize=12)
        ax2.grid(axis='y', alpha=0.3)

        plt.tight_layout()
        plt.savefig(VIZ_DIR / 'traditional_vs_haney_FULL.png', dpi=300, bbox_inches='tight')
        print("\n✓ Saved: traditional_vs_haney_FULL.png")
        plt.close()

# ============================================================================
# SECTION 5: ORGANIC MATTER VS SOIL HEALTH
# ============================================================================
print("\n" + "="*80)
print("SECTION 5: ORGANIC MATTER VS SOIL HEALTH")
print("="*80)

om_col = 'Organic Matter' if 'Organic Matter' in data.columns else 'Organic Matter, % LOI'

if om_col in data.columns and health_col in data.columns:
    om_health = data[[om_col, health_col]].apply(pd.to_numeric, errors='coerce').dropna()

    if len(om_health) > 0:
        corr = om_health[om_col].corr(om_health[health_col])
        print(f"\nCorrelation: {corr:.3f}")
        print(f"Sample size: {len(om_health):,}")

        # Visualization
        fig, ax = plt.subplots(figsize=(12, 8))
        # Sample if too many points
        if len(om_health) > 2000:
            plot_data = om_health.sample(2000, random_state=42)
        else:
            plot_data = om_health

        ax.scatter(plot_data[om_col], plot_data[health_col], alpha=0.4, s=20)
        ax.set_xlabel(om_col, fontsize=12, fontweight='bold')
        ax.set_ylabel(health_col, fontsize=12, fontweight='bold')
        ax.set_title(f'{health_col} vs {om_col} (r={corr:.3f}, n={len(om_health):,})',
                    fontsize=14, fontweight='bold')
        ax.grid(True, alpha=0.3)

        # Add regression line
        z = np.polyfit(plot_data[om_col], plot_data[health_col], 1)
        p = np.poly1d(z)
        x_line = np.linspace(plot_data[om_col].min(), plot_data[om_col].max(), 100)
        ax.plot(x_line, p(x_line), "r--", alpha=0.8, linewidth=2)

        plt.tight_layout()
        plt.savefig(VIZ_DIR / 'om_vs_health_FULL.png', dpi=300, bbox_inches='tight')
        print("✓ Saved: om_vs_health_FULL.png")
        plt.close()

print("\n" + "="*80)
print("CATEGORICAL & ADVANCED ANALYSIS COMPLETE")
print("="*80)
print(f"\nTime: {pd.Timestamp.now()}")
