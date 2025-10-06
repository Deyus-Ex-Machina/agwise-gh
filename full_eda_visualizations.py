#!/usr/bin/env python3
"""
COMPREHENSIVE VISUALIZATIONS - FULL DATASET
Generates all distribution plots, correlations, and advanced visualizations

Author: Claude Code
Date: October 6, 2025
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
plt.rcParams['figure.dpi'] = 300

# Paths
BASE_DIR = Path('/Users/deyus-ex-machina/agwise/agwise_eda')
DATA_FILE = BASE_DIR / 'data' / 'processed' / 'combined_soil_data_FULL.csv'
VIZ_DIR = BASE_DIR / 'outputs' / 'visualizations'
TABLE_DIR = BASE_DIR / 'outputs' / 'tables'

print("="*80)
print("COMPREHENSIVE VISUALIZATIONS - FULL DATASET (12,684 samples)")
print("="*80)

# Load data
print("\nLoading combined dataset...")
data = pd.read_csv(DATA_FILE)
print(f"✓ Loaded {len(data):,} samples with {len(data.columns)} variables")

# ============================================================================
# SECTION 1: DISTRIBUTIONS
# ============================================================================
print("\n" + "="*80)
print("SECTION 1: DISTRIBUTION VISUALIZATIONS")
print("="*80)

# Key metrics for visualization
key_viz_metrics = [
    '1:1 Soil pH', '1:1 Soluble Salt', 'Organic Matter', 'CO2-C',
    'H3A Nitrate', 'H3A Total Phosphorus', 'H3A ICAP Potassium',
    'H3A ICAP Calcium', 'Soil Health Calculation'
]

# Filter to available
available_viz = [col for col in key_viz_metrics if col in data.columns
                 and data[col].notna().sum() > 100]

print(f"\nGenerating distribution plots for {len(available_viz)} metrics...")

# 1. Histograms
fig, axes = plt.subplots(3, 3, figsize=(20, 16))
fig.suptitle('Distribution of Key Soil Health Metrics (Full Dataset: n=12,684)',
             fontsize=18, y=0.995, fontweight='bold')

for idx, col in enumerate(available_viz[:9]):
    row = idx // 3
    col_idx = idx % 3
    ax = axes[row, col_idx]

    values = pd.to_numeric(data[col], errors='coerce').dropna()

    if len(values) > 0:
        ax.hist(values, bins=60, edgecolor='black', alpha=0.7, color='steelblue')

        # Add statistics
        mean_val = values.mean()
        median_val = values.median()
        ax.axvline(mean_val, color='red', linestyle='--', linewidth=2,
                  label=f'Mean: {mean_val:.2f}')
        ax.axvline(median_val, color='green', linestyle='--', linewidth=2,
                  label=f'Median: {median_val:.2f}')

        ax.set_xlabel(col, fontsize=11, fontweight='bold')
        ax.set_ylabel('Frequency', fontsize=11)
        ax.set_title(f'{col}\n(n={len(values):,})', fontsize=10)
        ax.legend(fontsize=9)
        ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(VIZ_DIR / 'distributions_FULL.png', dpi=300, bbox_inches='tight')
print("✓ Saved: distributions_FULL.png")
plt.close()

# 2. Box plots
fig, axes = plt.subplots(3, 3, figsize=(20, 16))
fig.suptitle('Box Plots - Outlier Detection (Full Dataset: n=12,684)',
             fontsize=18, y=0.995, fontweight='bold')

for idx, col in enumerate(available_viz[:9]):
    row = idx // 3
    col_idx = idx % 3
    ax = axes[row, col_idx]

    values = pd.to_numeric(data[col], errors='coerce').dropna()

    if len(values) > 0:
        bp = ax.boxplot(values, vert=True, patch_artist=True,
                       boxprops=dict(facecolor='lightblue', alpha=0.7),
                       medianprops=dict(color='red', linewidth=2))
        ax.set_ylabel(col, fontsize=11, fontweight='bold')
        ax.set_title(f'{col}\n(n={len(values):,})', fontsize=10)
        ax.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig(VIZ_DIR / 'boxplots_FULL.png', dpi=300, bbox_inches='tight')
print("✓ Saved: boxplots_FULL.png")
plt.close()

# 3. Missing data heatmap
print("\nGenerating missing data pattern...")
missing_cols = data.columns[data.isnull().any()].tolist()[:40]  # Top 40
missing_matrix = data[missing_cols].isnull().astype(int)

fig, ax = plt.subplots(figsize=(16, 12))
sns.heatmap(missing_matrix.iloc[:500], cmap='RdYlGn_r', cbar_kws={'label': 'Missing'},
            yticklabels=False, ax=ax)
ax.set_title('Missing Values Pattern (First 500 Samples, Top 40 Variables)',
            fontsize=14, fontweight='bold')
ax.set_xlabel('Variables', fontsize=12)
ax.set_ylabel('Samples (n=12,684)', fontsize=12)
plt.xticks(rotation=90, ha='right', fontsize=8)
plt.tight_layout()
plt.savefig(VIZ_DIR / 'missing_pattern_FULL.png', dpi=300, bbox_inches='tight')
print("✓ Saved: missing_pattern_FULL.png")
plt.close()

# ============================================================================
# SECTION 2: CORRELATIONS
# ============================================================================
print("\n" + "="*80)
print("SECTION 2: CORRELATION ANALYSIS")
print("="*80)

# Select metrics with sufficient data
corr_metrics = []
for col in available_viz:
    if data[col].notna().sum() > 1000:
        corr_metrics.append(col)

print(f"\nAnalyzing correlations for {len(corr_metrics)} metrics...")

# Compute correlation matrix
corr_data = data[corr_metrics].apply(pd.to_numeric, errors='coerce')
corr_matrix = corr_data.corr()

# Save correlation matrix
corr_matrix.to_csv(TABLE_DIR / 'correlation_matrix_FULL.csv')
print("✓ Saved: correlation_matrix_FULL.csv")

# 4. Correlation heatmap
fig, ax = plt.subplots(figsize=(14, 12))
sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm', center=0,
            square=True, linewidths=0.5, cbar_kws={"shrink": 0.8},
            vmin=-1, vmax=1, ax=ax, annot_kws={'size': 8})
ax.set_title('Correlation Matrix - Key Soil Metrics (Full Dataset)',
            fontsize=14, fontweight='bold')
plt.xticks(rotation=45, ha='right', fontsize=9)
plt.yticks(rotation=0, fontsize=9)
plt.tight_layout()
plt.savefig(VIZ_DIR / 'correlation_heatmap_FULL.png', dpi=300, bbox_inches='tight')
print("✓ Saved: correlation_heatmap_FULL.png")
plt.close()

# Find strong correlations
mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
corr_pairs = corr_matrix.where(~mask).stack().sort_values(ascending=False)
strong_corr = corr_pairs[(abs(corr_pairs) > 0.5) & (abs(corr_pairs) < 1.0)]

print(f"\nFound {len(strong_corr)} strong correlations (|r| > 0.5)")
print("\nTop 10 strongest correlations:")
for idx, ((v1, v2), r) in enumerate(strong_corr.head(10).items(), 1):
    print(f"  {idx:2d}. {v1[:35]:35s} <-> {v2[:35]:35s}: {r:6.3f}")

# Save strong correlations
strong_corr_df = pd.DataFrame({
    'Variable_1': [pair[0] for pair in strong_corr.index],
    'Variable_2': [pair[1] for pair in strong_corr.index],
    'Correlation': strong_corr.values
})
strong_corr_df.to_csv(TABLE_DIR / 'strong_correlations_FULL.csv', index=False)
print("\n✓ Saved: strong_correlations_FULL.csv")

# 5. Scatter plots for top correlations
if len(strong_corr) >= 6:
    fig, axes = plt.subplots(2, 3, figsize=(18, 12))
    fig.suptitle('Top 6 Strongest Correlations (Full Dataset)',
                fontsize=16, fontweight='bold')

    for idx, ((var1, var2), corr_val) in enumerate(strong_corr.head(6).items()):
        row = idx // 3
        col = idx % 3
        ax = axes[row, col]

        plot_data = data[[var1, var2]].apply(pd.to_numeric, errors='coerce').dropna()

        if len(plot_data) > 0:
            # Sample if too many points
            if len(plot_data) > 2000:
                plot_data = plot_data.sample(2000, random_state=42)

            ax.scatter(plot_data[var1], plot_data[var2], alpha=0.4, s=20)
            ax.set_xlabel(var1, fontsize=9)
            ax.set_ylabel(var2, fontsize=9)
            ax.set_title(f'r = {corr_val:.3f} (n={len(plot_data):,})', fontsize=10)
            ax.grid(True, alpha=0.3)

            # Regression line
            if len(plot_data) > 10:
                z = np.polyfit(plot_data[var1], plot_data[var2], 1)
                p = np.poly1d(z)
                x_line = np.linspace(plot_data[var1].min(), plot_data[var1].max(), 100)
                ax.plot(x_line, p(x_line), "r--", alpha=0.8, linewidth=2)

    plt.tight_layout()
    plt.savefig(VIZ_DIR / 'scatter_correlations_FULL.png', dpi=300, bbox_inches='tight')
    print("✓ Saved: scatter_correlations_FULL.png")
    plt.close()

# ============================================================================
# SECTION 3: SOIL HEALTH ANALYSIS
# ============================================================================
print("\n" + "="*80)
print("SECTION 3: SOIL HEALTH SCORE ANALYSIS")
print("="*80)

health_col = 'Soil Health Calculation' if 'Soil Health Calculation' in data.columns else 'Soil Health Score'

if health_col in data.columns:
    health_data = pd.to_numeric(data[health_col], errors='coerce').dropna()
    print(f"\n{health_col} Statistics (n={len(health_data):,}):")
    print(f"  Mean: {health_data.mean():.2f}")
    print(f"  Median: {health_data.median():.2f}")
    print(f"  Std: {health_data.std():.2f}")
    print(f"  Range: {health_data.min():.2f} - {health_data.max():.2f}")

    # Get correlations with health
    health_correlations = corr_data.corrwith(corr_data[health_col]).sort_values(ascending=False)

    print(f"\nTop factors correlated with {health_col}:")
    for var, corr in health_correlations.items():
        if var != health_col and abs(corr) > 0.3:
            print(f"  {var[:50]:50s}: {corr:6.3f}")

    # Save
    health_corr_df = pd.DataFrame({
        'Variable': health_correlations.index,
        'Correlation': health_correlations.values
    })
    health_corr_df.to_csv(TABLE_DIR / 'soil_health_correlations_FULL.csv', index=False)
    print("\n✓ Saved: soil_health_correlations_FULL.csv")

    # 6. Soil health distribution
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.hist(health_data, bins=60, edgecolor='black', alpha=0.7, color='forestgreen')
    ax.axvline(health_data.median(), color='red', linestyle='--', linewidth=2,
              label=f'Median: {health_data.median():.2f}')
    ax.axvline(health_data.mean(), color='blue', linestyle='--', linewidth=2,
              label=f'Mean: {health_data.mean():.2f}')
    ax.set_xlabel(health_col, fontsize=12, fontweight='bold')
    ax.set_ylabel('Frequency', fontsize=12)
    ax.set_title(f'Distribution of {health_col} (n={len(health_data):,})',
                fontsize=14, fontweight='bold')
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(VIZ_DIR / 'soil_health_distribution_FULL.png', dpi=300, bbox_inches='tight')
    print("✓ Saved: soil_health_distribution_FULL.png")
    plt.close()

    # 7. Soil health factors scatter
    top_factors = health_correlations[health_correlations.index != health_col].head(8)

    fig, axes = plt.subplots(2, 4, figsize=(20, 10))
    fig.suptitle(f'Top 8 Factors Correlated with {health_col} (Full Dataset)',
                fontsize=16, fontweight='bold')

    for idx, (var, corr) in enumerate(top_factors.items()):
        row = idx // 4
        col = idx % 4
        ax = axes[row, col]

        plot_data = data[[health_col, var]].apply(pd.to_numeric, errors='coerce').dropna()

        if len(plot_data) > 0:
            # Sample if needed
            if len(plot_data) > 1500:
                plot_data = plot_data.sample(1500, random_state=42)

            ax.scatter(plot_data[var], plot_data[health_col], alpha=0.4, s=15)
            ax.set_xlabel(var, fontsize=9)
            ax.set_ylabel(health_col, fontsize=9)
            ax.set_title(f'r = {corr:.3f}', fontsize=10)
            ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(VIZ_DIR / 'soil_health_factors_FULL.png', dpi=300, bbox_inches='tight')
    print("✓ Saved: soil_health_factors_FULL.png")
    plt.close()

print("\n" + "="*80)
print("VISUALIZATION GENERATION COMPLETE")
print("="*80)
print(f"\nAll visualizations saved to: {VIZ_DIR}")
print(f"All tables saved to: {TABLE_DIR}")
