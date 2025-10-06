#!/usr/bin/env python3
"""
Generate comprehensive PDF report for FULL DATASET analysis
Includes all 12 visualizations and executive summary

Author: Claude Code
Date: October 6, 2025
"""

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Image,
    Table, TableStyle, KeepTogether
)
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from pathlib import Path

# Paths
BASE_DIR = Path('/Users/deyus-ex-machina/agwise/agwise_eda')
VIZ_DIR = BASE_DIR / 'outputs' / 'visualizations'
OUTPUT_PDF = BASE_DIR / 'reports' / 'COMPREHENSIVE_EDA_REPORT_FULL_DATASET.pdf'

print("="*80)
print("GENERATING COMPREHENSIVE PDF - FULL DATASET")
print("="*80)

# Setup PDF
doc = SimpleDocTemplate(
    str(OUTPUT_PDF),
    pagesize=letter,
    rightMargin=0.5*inch,
    leftMargin=0.5*inch,
    topMargin=0.75*inch,
    bottomMargin=0.75*inch,
)

story = []
styles = getSampleStyleSheet()

# Custom styles
title_style = ParagraphStyle(
    'Title',
    fontName='Helvetica-Bold',
    fontSize=26,
    textColor=colors.HexColor('#2c5f2d'),
    alignment=TA_CENTER,
    spaceAfter=15
)

subtitle_style = ParagraphStyle(
    'Subtitle',
    fontName='Helvetica',
    fontSize=15,
    textColor=colors.HexColor('#555555'),
    alignment=TA_CENTER,
    spaceAfter=10
)

h1_style = ParagraphStyle(
    'Heading1',
    fontName='Helvetica-Bold',
    fontSize=16,
    textColor=colors.HexColor('#2c5f2d'),
    spaceBefore=18,
    spaceAfter=10
)

body_style = ParagraphStyle(
    'Body',
    fontName='Helvetica',
    fontSize=10,
    alignment=TA_JUSTIFY,
    spaceAfter=6
)

bullet_style = ParagraphStyle(
    'Bullet',
    fontName='Helvetica',
    fontSize=10,
    leftIndent=20,
    spaceAfter=4
)

caption_style = ParagraphStyle(
    'Caption',
    fontName='Helvetica-Oblique',
    fontSize=9,
    textColor=colors.HexColor('#666666'),
    alignment=TA_CENTER,
    spaceAfter=12
)

# Cover Page
print("\n1. Creating cover page...")
story.append(Spacer(1, 1.8*inch))
story.append(Paragraph("Agricultural Soil Health", title_style))
story.append(Paragraph("Exploratory Data Analysis", title_style))
story.append(Paragraph("FULL DATASET", subtitle_style))
story.append(Spacer(1, 0.4*inch))
story.append(Paragraph("12,684 Samples | 869 Files | 198 Variables", body_style))
story.append(Spacer(1, 0.15*inch))
story.append(Paragraph("Analysis Date: October 6, 2025", body_style))
story.append(Spacer(1, 0.8*inch))

# Key highlights table
highlights = [
    ["12,684 Samples Analyzed", "250% increase from initial batch"],
    ["12 High-Resolution Visualizations", "Professional statistical graphics"],
    ["$126K-138K Economic Impact", "Haney Test nitrogen savings potential"],
    ["Grass-Dominant Success CONFIRMED", "20-30% legume mixes achieve highest scores"]
]
data = [[Paragraph(f"<b>{h[0]}</b><br/>{h[1]}", body_style)] for h in highlights]
t = Table(data, colWidths=[6*inch])
t.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f9f9f9')),
    ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#2c5f2d')),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('TOPPADDING', (0,0), (-1,-1), 10),
    ('BOTTOMPADDING', (0,0), (-1,-1), 10),
]))
story.append(t)
story.append(PageBreak())

# Executive Summary
print("2. Adding executive summary...")
story.append(Paragraph("Executive Summary", h1_style))
story.append(Spacer(1, 0.15*inch))

summary_points = [
    "Dataset expanded from 3,625 to 12,684 samples (869 CSV files, 198 variables), providing robust statistical power for comprehensive soil health analysis.",

    "Mean Soil Health Score: 10.96 (increased from 3.54), indicating new batch contains healthier soils or different management practices. Full range: 0.72-131.96.",

    "pH Distribution More Balanced: Mean pH 7.07 (down from 8.24), representing more diverse soil conditions. Alkaline soil percentage decreased from 90% to approximately 50%.",

    "Organic Matter Increased: Mean 3.11% (up from 0.99%), with 16.5% of samples in high category (>3%). Correlation with soil health: r=0.604.",

    "Biological Activity Paramount: CO2-C shows very strong correlation with soil health (r=0.931), validating biological activity as strongest predictor across full dataset.",

    "Cover Crop Finding VALIDATED: Grass-dominant mixes (20-30% legume) achieve highest health scores (mean=17.15-25.29) with statistically sufficient sample sizes (n=210-367 per group).",

    "Economic Impact Quantified: Haney Test shows +33 lbs/A nitrogen vs Traditional testing. Potential savings: $126,105-$137,894 across 3,942 samples (approximately $32-35 per sample).",

    "Data Quality: 52% duplication rate requires investigation. Core soil metrics have excellent coverage (n>3,900), but crop recommendations remain sparse (<5% of samples)."
]

for point in summary_points:
    story.append(Paragraph(f"• {point}", bullet_style))
    story.append(Spacer(1, 0.08*inch))

story.append(PageBreak())

# Visualizations
print("3. Adding visualizations...")

visualizations = [
    ("Dataset Overview & Distributions", [
        ("distributions_FULL.png", "Distribution histograms for 9 key soil health metrics across full 12,684-sample dataset."),
        ("boxplots_FULL.png", "Box plots revealing outlier patterns and quartile distributions for primary variables."),
        ("missing_pattern_FULL.png", "Heatmap showing missing data patterns across 500 samples and top 40 variables.")
    ]),

    ("Correlation Analysis", [
        ("correlation_heatmap_FULL.png", "Complete correlation matrix showing relationships between 9 key soil variables. Strongest: CO2-C vs Soil Health (r=0.931)."),
        ("scatter_correlations_FULL.png", "Top 4 strongest correlations with regression lines and sample distributions (sampled for clarity).")
    ]),

    ("Soil Health Analysis", [
        ("soil_health_distribution_FULL.png", "Histogram of Soil Health Calculation scores (n=3,942). Mean=10.96, Median=8.99, Range=0.72-131.96."),
        ("soil_health_factors_FULL.png", "Top 8 factors correlated with soil health: CO2-C (r=0.931) and Organic Matter (r=0.604) dominate.")
    ]),

    ("Cover Crop & Crop Analysis", [
        ("cover_crop_mix_distribution_FULL.png", "Distribution of cover crop mixes. 50% Legume/50% Grass most common (31.4%)."),
        ("soil_health_by_cover_boxplot_FULL.png", "Soil health scores by cover crop mix. Grass-dominant (20-30% legume) achieve highest scores."),
        ("crop_distribution_FULL.png", "Top 15 recommended crops. Corn dominant (30.8%), followed by soybeans (16.4%).")
    ]),

    ("Nutrient & Economic Analysis", [
        ("npk_comparison_FULL.png", "N-P-K nutrient availability distributions. High variability (CV >100%) across all three nutrients."),
        ("traditional_vs_haney_FULL.png", "Traditional vs Haney nitrogen test comparison. Haney averages 33 lbs/A higher (economic significance)."),
        ("om_vs_health_FULL.png", "Organic matter vs soil health relationship (r=0.604). Strong positive correlation across 3,942 samples.")
    ])
]

viz_count = 0
for section_title, viz_list in visualizations:
    story.append(Paragraph(section_title, h1_style))
    story.append(Spacer(1, 0.15*inch))

    for viz_file, caption_text in viz_list:
        viz_path = VIZ_DIR / viz_file
        if viz_path.exists():
            try:
                img = Image(str(viz_path))
                img.drawWidth = 7*inch
                img.drawHeight = 4.5*inch
                caption = Paragraph(f"<i>{caption_text}</i>", caption_style)
                story.append(KeepTogether([img, Spacer(1, 0.08*inch), caption]))
                story.append(Spacer(1, 0.25*inch))
                viz_count += 1
                print(f"   ✓ Added: {viz_file}")
            except Exception as e:
                print(f"   ✗ Error with {viz_file}: {e}")
        else:
            print(f"   ⚠ Not found: {viz_file}")

    story.append(PageBreak())

print(f"\n   Total visualizations added: {viz_count}")

# Key Findings Summary
print("4. Adding key findings...")
story.append(Paragraph("Key Findings - Full Dataset", h1_style))
story.append(Spacer(1, 0.15*inch))

findings = [
    ("Dataset Scale", [
        "12,684 total samples from 869 files (99.9% load success)",
        "6,049 unique samples (52.31% duplication rate)",
        "198 total variables (59 new vs original batch)",
        "Two batches: 3,625 + 9,059 samples"
    ]),

    ("Soil Health Patterns", [
        "Mean health score: 10.96 (210% increase from original)",
        "CO2-C strongest predictor (r=0.931)",
        "Organic matter second strongest (r=0.604)",
        "pH negatively correlated (r=-0.308)"
    ]),

    ("Cover Crop Validation", [
        "20% Legume/80% Grass: Mean health = 25.29 (highest)",
        "30% Legume/70% Grass: Mean health = 17.15 (2nd)",
        "70% Legume/30% Grass: Mean health = 2.06 (lowest)",
        "Sample sizes: 167-1,018 per group (statistically robust)"
    ]),

    ("Economic Impact", [
        "Haney Test N: 60.03 lbs/A (mean)",
        "Traditional Test N: 26.86 lbs/A (mean)",
        "Difference: +33.17 lbs/A with Haney",
        "Total potential savings: $126,105-$137,894"
    ]),

    ("Data Quality Insights", [
        "Core metrics: Excellent coverage (n>3,900)",
        "Cover crop data: Good (n=1,813-3,239)",
        "Crop recommendations: Limited (n<500, 4% of samples)",
        "Enzyme tests: 100% missing (not performed)"
    ])
]

for finding_title, points in findings:
    story.append(Paragraph(finding_title, h1_style))
    for point in points:
        story.append(Paragraph(f"• {point}", bullet_style))
    story.append(Spacer(1, 0.12*inch))

story.append(PageBreak())

# Recommendations
story.append(Paragraph("Recommendations", h1_style))
story.append(Spacer(1, 0.15*inch))

recs = [
    "Validate Haney Test economic benefits ($126K-138K potential)",
    "Investigate grass-dominant cover crop success mechanisms",
    "Clarify duplication: temporal, spatial, or data artifacts",
    "Increase crop recommendation documentation (<5% currently)",
    "Prioritize organic matter inputs (r=0.604 with health)",
    "Stimulate biological activity (r=0.931 with health)",
    "Consider 20-30% legume cover crop mixes (25.29 mean health)",
    "Study top 5% performers (health score >20) as case studies"
]

for rec in recs:
    story.append(Paragraph(f"• {rec}", bullet_style))

story.append(Spacer(1, 1*inch))
story.append(Paragraph("Complete Documentation Available", h1_style))
story.append(Spacer(1, 0.2*inch))
story.append(Paragraph("Executive Summary: reports/EXECUTIVE_SUMMARY_FULL_DATASET.md", caption_style))
story.append(Paragraph("All Analysis Scripts: scripts/full_eda_*.py", caption_style))
story.append(Paragraph("Data Tables: outputs/tables/", caption_style))
story.append(Paragraph("Project Directory: /Users/deyus-ex-machina/agwise/agwise_eda/", caption_style))

# Build PDF
print("\n5. Building PDF...")
doc.build(story)

print(f"\n   ✓ PDF generated successfully!")
print(f"   Location: {OUTPUT_PDF}")
file_size = OUTPUT_PDF.stat().st_size / 1024 / 1024
print(f"   Size: {file_size:.2f} MB")

print("\n" + "="*80)
print("PDF GENERATION COMPLETE")
print("="*80)
print(f"\nOpen with: open '{OUTPUT_PDF}'")
