# Agricultural Soil Health EDA Project

Comprehensive exploratory data analysis of agricultural soil health testing data.

## Project Overview

- **Dataset**: 300 soil test CSV files, 3,625 samples
- **Analysis Date**: October 5, 2025
- **Variables**: 139 (125 numeric, 14 categorical)
- **Focus**: Soil health metrics, nutrient availability, cover crop impacts, testing methodology comparison

## Quick Start

```bash
# Navigate to project directory
cd agwise_eda

# Set up Python environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run analysis pipeline
cd scripts
python run_all_analyses.py
```

## Directory Structure

```
agwise_eda/
├── README.md                      # This file
├── requirements.txt               # Python dependencies
│
├── reports/                       # Main findings and documentation
│   └── COMPREHENSIVE_EDA_REPORT.md
│
├── docs/                          # Supporting documentation
│   ├── README_EDA_DELIVERABLES.md
│   ├── METHODOLOGY.md
│   └── DATA_DICTIONARY.md
│
├── data/
│   ├── raw/                       # Original 300 CSV files
│   │   └── OneDrive_1_10-5-2025/
│   └── processed/                 # Cleaned and combined data
│       └── combined_soil_data.csv
│
├── scripts/                       # Analysis code
│   ├── run_all_analyses.py       # Master script
│   ├── 01_eda_analysis.py
│   ├── 02_eda_visualizations.py
│   ├── 03_eda_correlations.py
│   ├── 04_eda_categorical_crops.py
│   └── 05_eda_advanced_insights.py
│
└── outputs/
    ├── visualizations/            # All plots (15 PNG files)
    │   ├── distributions.png
    │   ├── correlation_heatmap.png
    │   └── ...
    └── tables/                    # Summary statistics (10 CSV files)
        ├── descriptive_statistics.csv
        ├── correlation_matrix.csv
        └── ...
```

## Key Findings

### Soil Health Status
- **87% of soils** rate "Poor" to "Fair" in health scores
- Mean soil health score: 3.54 (median: 2.24)
- Only 13% achieve "Good" or "Excellent" ratings

### Critical Relationships
- **Soil respiration** is strongest health predictor (r=0.952)
- **Organic matter** strongly correlates with health (r=0.871)
- **Alkaline pH** negatively impacts health (r=-0.726)

### Cover Crop Insights
- Grass-dominant mixes (20-40% legume) show highest soil health scores
- Legume-dominant mixes (60-70%) show lowest scores
- Finding requires statistical validation

### Economic Impact
- Haney Test vs Traditional: +32 lbs/A nitrogen difference
- Potential savings: $31.95 per sample
- Total dataset savings potential: $51,113.57

### Soil Characteristics
- 90% of soils are alkaline (pH >7.5)
- High nutrient variability (nitrogen most limiting)
- 46% duplicate rate in samples

## Analysis Scripts

All scripts are self-contained and documented:

| Script | Purpose | Runtime |
|--------|---------|---------|
| `01_eda_analysis.py` | Data loading, merging, basic stats | ~30 sec |
| `02_eda_visualizations.py` | Distribution plots, outlier detection | ~45 sec |
| `03_eda_correlations.py` | Correlation analysis and plots | ~30 sec |
| `04_eda_categorical_crops.py` | Crop and cover crop analysis | ~30 sec |
| `05_eda_advanced_insights.py` | Advanced soil health insights | ~30 sec |

## Outputs Generated

### Reports (1)
- Comprehensive 13-section EDA report with findings and recommendations

### Visualizations (15)
- Distribution plots, box plots, correlation heatmaps
- Scatter plots, categorical analyses
- Traditional vs Haney comparison plots

### Data Tables (11)
- Descriptive statistics, correlation matrices
- Crop recommendations, soil health summaries
- Missing data reports, outlier analyses

## Dependencies

```
Python 3.13+
pandas 2.3.3
numpy 2.3.3
matplotlib 3.10.6
seaborn 0.13.2
scipy 1.16.2
```

See `requirements.txt` for full list.

## Next Steps for Data Scientists

### Immediate (Week 1-2)
- [ ] Resolve duplicate samples with laboratory
- [ ] Statistical significance testing of key findings
- [ ] Validate Traditional vs Haney comparison

### Short-term (Month 1)
- [ ] Predictive modeling for soil health scores
- [ ] Cluster analysis to identify soil management types
- [ ] Cover crop impact validation study

### Medium-term (Months 2-3)
- [ ] Stakeholder reporting and dashboards
- [ ] Recommendation tool development
- [ ] Plan additional data collection

### Long-term (3+ months)
- [ ] Temporal data collection protocol
- [ ] Geographic expansion of dataset
- [ ] Management intervention trials

## Data Quality Notes

### Strengths
- Large sample size (1,951 unique samples)
- Comprehensive soil health metrics
- Two testing methodology versions for comparison
- Rich nutrient availability data

### Limitations
- 46% duplicate rate (requires investigation)
- High missing data in crop recommendations (>95%)
- No geographic information
- Limited temporal data
- Enzyme measurements 100% missing

## Citation

If using this analysis, please cite:

```
Agricultural Soil Health EDA Project (2025)
Comprehensive Analysis of 300 Soil Test Files
Generated: October 5, 2025
```

## Contact & Support

### For Technical Questions
- Review script documentation in `scripts/` directory
- Consult output tables in `outputs/tables/`
- Reference visualizations in `outputs/visualizations/`

### For Data Questions
- Contact soil testing laboratory for methodology details
- Verify variable definitions in `docs/DATA_DICTIONARY.md`
- Check data quality notes in main report

### For Agricultural Interpretation
- Consult regional agronomists
- Review cover crop literature
- Engage with participating growers

## License

This analysis is provided for research and educational purposes.

## Version History

- **v1.0** (Oct 5, 2025) - Initial comprehensive EDA complete
  - 300 files analyzed
  - 15 visualizations generated
  - 11 summary tables created
  - Comprehensive report delivered

---

**Status**: ✅ Analysis complete and production-ready

**Last Updated**: October 5, 2025
