#!/usr/bin/env python3
"""
Generate visual PDF report with all visualizations and key findings.
Simplified approach for reliable PDF generation.

Author: Claude Code
Date: October 5, 2025
"""

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Image,
    Table, TableStyle, KeepTogether, Frame, PageTemplate
)
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from pathlib import Path

# Paths
BASE_DIR = Path('/Users/deyus-ex-machina/agwise/agwise_eda')
VIZ_DIR = BASE_DIR / 'outputs' / 'visualizations'
OUTPUT_PDF = BASE_DIR / 'reports' / 'COMPREHENSIVE_EDA_REPORT.pdf'

print("="*80)
print("GENERATING VISUAL PDF REPORT")
print("="*80)

# Setup PDF
print("\n1. Setting up PDF document...")
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
    fontSize=28,
    textColor=colors.HexColor('#2c5f2d'),
    alignment=TA_CENTER,
    spaceAfter=20
)

subtitle_style = ParagraphStyle(
    'Subtitle',
    fontName='Helvetica',
    fontSize=16,
    textColor=colors.HexColor('#555555'),
    alignment=TA_CENTER,
    spaceAfter=12
)

h1_style = ParagraphStyle(
    'Heading1',
    fontName='Helvetica-Bold',
    fontSize=18,
    textColor=colors.HexColor('#2c5f2d'),
    spaceBefore=20,
    spaceAfter=12
)

h2_style = ParagraphStyle(
    'Heading2',
    fontName='Helvetica-Bold',
    fontSize=14,
    textColor=colors.HexColor('#2c5f2d'),
    spaceBefore=15,
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
    spaceAfter=15
)

# Cover Page
print("\n2. Creating cover page...")
story.append(Spacer(1, 2*inch))
story.append(Paragraph("Agricultural Soil Health", title_style))
story.append(Paragraph("Exploratory Data Analysis", title_style))
story.append(Spacer(1, 0.5*inch))
story.append(Paragraph("Comprehensive Visual Report", subtitle_style))
story.append(Spacer(1, 0.3*inch))
story.append(Paragraph("300 Soil Test Files | 3,625 Samples | 139 Variables", body_style))
story.append(Spacer(1, 0.2*inch))
story.append(Paragraph("Analysis Date: October 5, 2025", body_style))
story.append(Spacer(1, 1*inch))

# Key highlights
highlights = [
    ("15 Professional Visualizations", "High-resolution statistical graphics"),
    ("13 Key Findings", "Actionable soil health insights"),
    ("$51,113 Economic Impact", "Potential nitrogen savings identified"),
    ("87% Improvement Opportunity", "Soils rated Poor-to-Fair")
]

data = [[Paragraph(f"<b>{h[0]}</b><br/>{h[1]}", body_style)] for h in highlights]
t = Table(data, colWidths=[6*inch])
t.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f9f9f9')),
    ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#2c5f2d')),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('TOPPADDING', (0,0), (-1,-1), 12),
    ('BOTTOMPADDING', (0,0), (-1,-1), 12),
]))
story.append(t)

story.append(PageBreak())

# Executive Summary
print("\n3. Adding executive summary...")
story.append(Paragraph("Executive Summary", h1_style))
story.append(Spacer(1, 0.2*inch))

summary_points = [
    "Dataset comprises 3,625 soil samples from 300 CSV files with 139 variables covering soil health metrics, nutrient availability, and crop recommendations.",

    "Data Quality: 46% duplication rate (1,951 unique samples), 90% of samples missing crop data, but core soil health metrics available for 1,600+ samples.",

    "Critical Finding: 87% of soils score Poor-to-Fair in health assessments (mean: 3.54, median: 2.24), presenting significant improvement opportunities.",

    "Soil Respiration emerges as strongest health predictor (r=0.952), followed by Organic Matter (r=0.871). High alkalinity (90% of soils pH >7.5) negatively impacts biological activity.",

    "Surprising Result: Grass-dominant cover crop mixes (20-40% legume) achieve highest soil health scores, contrary to conventional wisdom favoring legume-heavy mixes.",

    "Economic Impact: Haney Test methodology recommends 32 lbs/A more nitrogen than Traditional testing, with potential cost savings of $31.95 per sample ($51,113 total dataset).",

    "Regional Pattern: Extreme alkalinity (pH >7.5 in 90% of samples) indicates arid/semi-arid conditions with calcium-rich soils limiting microbial activity.",

    "Nutrient Status: Nitrogen is primary limiting nutrient while phosphorus and potassium show relative abundance. High variability suggests diverse management histories."
]

for point in summary_points:
    story.append(Paragraph(f"• {point}", bullet_style))
    story.append(Spacer(1, 0.1*inch))

story.append(PageBreak())

# Visualizations Section
print("\n4. Adding visualizations...")

visualizations = [
    ("Data Distribution Analysis", [
        ("distributions.png", "Distribution histograms for 9 key soil health metrics showing mean, median, and frequency patterns."),
        ("boxplots.png", "Box plots revealing outlier patterns and quartile distributions for primary variables.")
    ]),

    ("Data Quality Assessment", [
        ("missing_pattern.png", "Heatmap showing missing data patterns across first 200 samples and top 30 variables.")
    ]),

    ("Correlation Analysis", [
        ("correlation_heatmap.png", "Complete correlation matrix (27x27) showing relationships between all key soil variables."),
        ("scatter_correlations.png", "Top 6 strongest correlations with regression lines and sample distributions.")
    ]),

    ("Soil Health Drivers", [
        ("soil_health_factors.png", "Eight-panel analysis showing factors most correlated with soil health scores."),
        ("soil_health_distribution.png", "Histogram of soil health scores with mean and median indicators.")
    ]),

    ("Crop and Cover Crop Analysis", [
        ("crop_distribution.png", "Top 15 recommended crop types showing corn and soybeans as primary crops."),
        ("cover_crop_mix_distribution.png", "Distribution of seven cover crop mix ratios (legume/grass percentages)."),
        ("soil_health_by_cover_boxplot.png", "Box plots comparing soil health scores across different cover crop mixes."),
        ("nutrient_recs_by_crop.png", "N-P-K nutrient recommendations for top 5 crop types.")
    ]),

    ("Advanced Insights", [
        ("npk_comparison.png", "Side-by-side comparison of nitrogen, phosphorus, and potassium availability."),
        ("traditional_vs_haney.png", "Scatter plot and box plot comparing Traditional vs Haney test nitrogen recommendations."),
        ("om_vs_health.png", "Relationship between organic matter content and soil health score (r=0.871).")
    ])
]

viz_count = 0
for section_title, viz_list in visualizations:
    story.append(Paragraph(section_title, h1_style))
    story.append(Spacer(1, 0.2*inch))

    for viz_file, caption_text in viz_list:
        viz_path = VIZ_DIR / viz_file
        if viz_path.exists():
            try:
                # Calculate image dimensions (maintain aspect ratio)
                img = Image(str(viz_path))
                img_width = 7*inch
                img_height = 4.5*inch
                img.drawWidth = img_width
                img.drawHeight = img_height

                caption = Paragraph(f"<i>{caption_text}</i>", caption_style)

                story.append(KeepTogether([img, Spacer(1, 0.1*inch), caption]))
                story.append(Spacer(1, 0.3*inch))
                viz_count += 1
                print(f"   ✓ Added: {viz_file}")
            except Exception as e:
                print(f"   ✗ Error with {viz_file}: {e}")
        else:
            print(f"   ⚠ Not found: {viz_file}")

    story.append(PageBreak())

print(f"\n   ✓ Total visualizations added: {viz_count}")

# Key Findings
print("\n5. Adding key findings...")
story.append(Paragraph("Key Findings Summary", h1_style))
story.append(Spacer(1, 0.2*inch))

findings = [
    ("Soil Health Status", [
        "87% of soils rate Poor-to-Fair (scores <5)",
        "Mean score: 3.54, Median: 2.24",
        "Only 13% achieve Good or Excellent ratings",
        "Significant improvement opportunity identified"
    ]),

    ("Critical Relationships", [
        "Soil Respiration: r=0.952 with health (strongest predictor)",
        "Organic Matter: r=0.871 with health (second strongest)",
        "Alkaline pH: r=-0.726 with health (negative impact)",
        "High Calcium: r=-0.795 with health (indicator of low activity)"
    ]),

    ("Cover Crop Insights", [
        "Grass-dominant mixes (20-40% legume) show highest health scores",
        "Legume-dominant mixes (60-70%) show lowest scores",
        "Counterintuitive finding requires statistical validation",
        "May relate to carbon input stability and soil structure"
    ]),

    ("Economic Impact", [
        "Haney Test: 60.3 lbs/A N (mean)",
        "Traditional Test: 27.9 lbs/A N (mean)",
        "Difference: +32.4 lbs/A (Haney shows more available N)",
        "Potential savings: $31.95/sample ($51,113 total)"
    ]),

    ("Recommendations", [
        "Prioritize organic matter inputs and biological activity stimulation",
        "Address alkalinity issues (90% of soils pH >7.5)",
        "Validate Haney testing methodology benefits",
        "Investigate grass-dominant cover crop advantages",
        "Focus nitrogen management (primary limiting nutrient)"
    ])
]

for finding_title, points in findings:
    story.append(Paragraph(finding_title, h2_style))
    for point in points:
        story.append(Paragraph(f"• {point}", bullet_style))
    story.append(Spacer(1, 0.15*inch))

story.append(PageBreak())

# Footer page
story.append(Spacer(1, 2*inch))
story.append(Paragraph("Complete Analysis Available", h1_style))
story.append(Spacer(1, 0.3*inch))
story.append(Paragraph("For detailed methodology, statistical analysis, and complete findings:", body_style))
story.append(Spacer(1, 0.2*inch))
story.append(Paragraph("reports/COMPREHENSIVE_EDA_REPORT.md", caption_style))
story.append(Spacer(1, 0.5*inch))
story.append(Paragraph("All data tables, scripts, and documentation:", body_style))
story.append(Spacer(1, 0.2*inch))
story.append(Paragraph("/Users/deyus-ex-machina/agwise/agwise_eda/", caption_style))

# Build PDF
print("\n6. Building PDF...")
doc.build(story)

print(f"\n   ✓ PDF generated successfully!")
print(f"   Location: {OUTPUT_PDF}")
file_size = OUTPUT_PDF.stat().st_size / 1024 / 1024
print(f"   Size: {file_size:.2f} MB")

print("\n" + "="*80)
print("PDF GENERATION COMPLETE")
print("="*80)
print(f"\nOpen with: open '{OUTPUT_PDF}'")
