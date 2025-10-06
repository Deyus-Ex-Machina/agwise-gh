import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Load data
data = pd.read_csv('/Users/deyus-ex-machina/agwise/combined_soil_data.csv')

print(f"{'='*80}")
print(f"CATEGORICAL ANALYSIS - CROPS AND COVER CROPS")
print(f"{'='*80}")

# Analyze crop recommendations
crop_cols = ['Crop 1', 'Crop 2', 'Crop 3', 'Past Crop']
crop_cols = [col for col in crop_cols if col in data.columns]

print("\nCrop Analysis:")
crop_summary = {}
for col in crop_cols:
    print(f"\n{col}:")
    value_counts = data[col].value_counts()
    print(f"  Unique values: {data[col].nunique()}")
    print(f"  Missing: {data[col].isnull().sum()} ({(data[col].isnull().sum()/len(data)*100):.1f}%)")
    print(f"  Top 5:")
    for crop, count in value_counts.head(5).items():
        print(f"    {crop}: {count} ({(count/len(data)*100):.1f}%)")
    crop_summary[col] = value_counts

# Cover Crop Mix Analysis
cover_crop_cols = ['Cover Crop Mix', 'Cover crop mix']
cover_crop_cols = [col for col in cover_crop_cols if col in data.columns]

print(f"\n{'='*80}")
print(f"COVER CROP MIX ANALYSIS")
print(f"{'='*80}")

for col in cover_crop_cols:
    if data[col].notna().sum() > 0:
        print(f"\n{col}:")
        value_counts = data[col].value_counts()
        print(f"  Unique values: {data[col].nunique()}")
        print(f"  Non-missing: {data[col].notna().sum()}")
        print(f"\n  Distribution:")
        for mix, count in value_counts.items():
            pct = (count / data[col].notna().sum() * 100)
            print(f"    {mix}: {count} ({pct:.1f}%)")

# Nutrient recommendations by crop
print(f"\n{'='*80}")
print(f"NUTRIENT RECOMMENDATIONS BY CROP TYPE")
print(f"{'='*80}")

# For Crop 1
if 'Crop 1' in data.columns:
    nutrient_cols = ['Nitrogen Rec 1', 'P205 Rec 1', 'K2O Rec 1']
    nutrient_cols = [col for col in nutrient_cols if col in data.columns]

    if nutrient_cols:
        crop1_data = data[['Crop 1'] + nutrient_cols].dropna()

        if len(crop1_data) > 0:
            print(f"\nNutrient recommendations for top crops (Crop 1):")
            top_crops = crop1_data['Crop 1'].value_counts().head(5).index

            rec_summary = []
            for crop in top_crops:
                crop_subset = crop1_data[crop1_data['Crop 1'] == crop]
                rec_dict = {'Crop': crop, 'Count': len(crop_subset)}

                for nutrient in nutrient_cols:
                    if nutrient in crop_subset.columns:
                        rec_dict[f'{nutrient}_Mean'] = crop_subset[nutrient].mean()
                        rec_dict[f'{nutrient}_Median'] = crop_subset[nutrient].median()

                rec_summary.append(rec_dict)

            rec_df = pd.DataFrame(rec_summary)
            print(rec_df.to_string(index=False))

            # Save recommendations summary
            rec_df.to_csv('/Users/deyus-ex-machina/agwise/crop_nutrient_recommendations.csv', index=False)
            print(f"\n✓ Crop nutrient recommendations saved to: crop_nutrient_recommendations.csv")

# Soil health by cover crop mix
print(f"\n{'='*80}")
print(f"SOIL HEALTH BY COVER CROP MIX")
print(f"{'='*80}")

health_col = 'Soil Health Score' if 'Soil Health Score' in data.columns else 'Soil Health Calculation'

for cover_col in cover_crop_cols:
    if cover_col in data.columns and health_col in data.columns:
        cover_health = data[[cover_col, health_col]].dropna()

        if len(cover_health) > 0:
            print(f"\n{health_col} by {cover_col}:")

            health_by_cover = cover_health.groupby(cover_col)[health_col].agg([
                'count', 'mean', 'median', 'std', 'min', 'max'
            ]).sort_values('mean', ascending=False)

            print(health_by_cover.round(2))

            # Save
            health_by_cover.to_csv('/Users/deyus-ex-machina/agwise/soil_health_by_cover_crop.csv')
            print(f"\n✓ Soil health by cover crop saved to: soil_health_by_cover_crop.csv")

# pH levels by past crop
print(f"\n{'='*80}")
print(f"SOIL pH BY PAST CROP")
print(f"{'='*80}")

ph_col = 'Soil pH 1:1' if 'Soil pH 1:1' in data.columns else '1:1 Soil pH'

if 'Past Crop' in data.columns and ph_col in data.columns:
    ph_by_crop = data[['Past Crop', ph_col]].dropna()

    if len(ph_by_crop) > 0:
        ph_summary = ph_by_crop.groupby('Past Crop')[ph_col].agg([
            'count', 'mean', 'median', 'std', 'min', 'max'
        ]).sort_values('mean', ascending=False)

        print(ph_summary.round(2))

        ph_summary.to_csv('/Users/deyus-ex-machina/agwise/ph_by_past_crop.csv')
        print(f"\n✓ pH by past crop saved to: ph_by_past_crop.csv")

# Visualizations
print(f"\n{'='*80}")
print(f"GENERATING CATEGORICAL VISUALIZATIONS")
print(f"{'='*80}")

# 1. Crop distribution
if 'Crop 1' in data.columns:
    fig, ax = plt.subplots(figsize=(14, 8))
    crop1_counts = data['Crop 1'].value_counts().head(15)
    crop1_counts.plot(kind='barh', ax=ax, color='steelblue')
    ax.set_xlabel('Count', fontsize=12)
    ax.set_ylabel('Crop Type', fontsize=12)
    ax.set_title('Top 15 Recommended Crops (Crop 1)', fontsize=14)
    ax.grid(axis='x', alpha=0.3)
    plt.tight_layout()
    plt.savefig('/Users/deyus-ex-machina/agwise/crop_distribution.png', dpi=300, bbox_inches='tight')
    print("✓ Crop distribution plot saved to: crop_distribution.png")
    plt.close()

# 2. Cover crop mix distribution
if cover_crop_cols:
    for col in cover_crop_cols:
        if data[col].notna().sum() > 0:
            fig, ax = plt.subplots(figsize=(12, 8))
            cover_counts = data[col].value_counts()
            cover_counts.plot(kind='bar', ax=ax, color='forestgreen')
            ax.set_xlabel('Cover Crop Mix', fontsize=12)
            ax.set_ylabel('Count', fontsize=12)
            ax.set_title(f'Distribution of {col}', fontsize=14)
            ax.grid(axis='y', alpha=0.3)
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            filename = col.lower().replace(' ', '_')
            plt.savefig(f'/Users/deyus-ex-machina/agwise/{filename}_distribution.png',
                       dpi=300, bbox_inches='tight')
            print(f"✓ {col} distribution plot saved")
            plt.close()

# 3. Soil health by cover crop box plot
if cover_crop_cols and health_col in data.columns:
    for cover_col in cover_crop_cols:
        if data[cover_col].notna().sum() > 50:
            plot_data = data[[cover_col, health_col]].dropna()

            if len(plot_data) > 0:
                fig, ax = plt.subplots(figsize=(14, 8))
                plot_data.boxplot(column=health_col, by=cover_col, ax=ax)
                ax.set_xlabel('Cover Crop Mix', fontsize=12)
                ax.set_ylabel(health_col, fontsize=12)
                ax.set_title(f'{health_col} by Cover Crop Mix', fontsize=14)
                plt.suptitle('')  # Remove default title
                plt.xticks(rotation=45, ha='right')
                plt.tight_layout()
                plt.savefig('/Users/deyus-ex-machina/agwise/soil_health_by_cover_boxplot.png',
                           dpi=300, bbox_inches='tight')
                print("✓ Soil health by cover crop boxplot saved")
                plt.close()
                break

# 4. Nutrient recommendations by crop
if 'Crop 1' in data.columns and nutrient_cols:
    top_5_crops = data['Crop 1'].value_counts().head(5).index
    plot_data = data[data['Crop 1'].isin(top_5_crops)][['Crop 1'] + nutrient_cols].dropna()

    if len(plot_data) > 0:
        fig, axes = plt.subplots(1, len(nutrient_cols), figsize=(18, 6))
        fig.suptitle('Nutrient Recommendations by Top 5 Crops', fontsize=16)

        for idx, nutrient in enumerate(nutrient_cols):
            ax = axes[idx] if len(nutrient_cols) > 1 else axes
            plot_data.boxplot(column=nutrient, by='Crop 1', ax=ax)
            ax.set_xlabel('Crop', fontsize=10)
            ax.set_ylabel(nutrient, fontsize=10)
            ax.set_title(nutrient, fontsize=11)
            plt.sca(ax)
            plt.xticks(rotation=45, ha='right', fontsize=8)

        plt.suptitle('Nutrient Recommendations by Top 5 Crops', fontsize=16)
        plt.tight_layout()
        plt.savefig('/Users/deyus-ex-machina/agwise/nutrient_recs_by_crop.png',
                   dpi=300, bbox_inches='tight')
        print("✓ Nutrient recommendations by crop plot saved")
        plt.close()

print(f"\n{'='*80}")
print(f"CATEGORICAL ANALYSIS COMPLETE")
print(f"{'='*80}")
