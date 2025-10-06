# EDA Methodology Documentation

## Overview

This document details the analytical methods, statistical techniques, and decisions made during the exploratory data analysis of agricultural soil health data.

---

## 1. Data Collection & Preprocessing

### 1.1 Data Sources
- **Format**: 300 CSV files from soil testing laboratory
- **Structure**: Varying column names across files (two versions identified)
- **Encoding**: UTF-8
- **Date Range**: March 2021+

### 1.2 Data Loading Process
```python
# Iterative loading with error handling
for file in csv_files:
    df = pd.read_csv(file)
    dfs.append(df)

# Concatenation with index reset
combined_data = pd.concat(dfs, ignore_index=True)
```

**Decisions Made:**
- Preserved all columns from all files (union of schemas)
- No column filtering at load time
- Maintained original data types
- Reset indices to create continuous row numbers

### 1.3 Data Cleaning Decisions

**Duplicates:**
- Identified but NOT removed (46% duplication rate)
- Rationale: Unknown if duplicates are temporal, spatial, or artifacts
- Recommendation: Investigate before removal

**Missing Data:**
- No imputation performed
- Complete case analysis used (listwise deletion)
- Rationale: High missing rates (>50%) make imputation unreliable

**Outliers:**
- Identified using IQR method (Q1-1.5×IQR, Q3+1.5×IQR)
- Retained in analysis (not removed)
- Rationale: Many outliers appear to be legitimate high-performers

---

## 2. Descriptive Statistics

### 2.1 Measures Computed

**Central Tendency:**
- Mean: `np.mean()`
- Median: `np.median()` or `df.quantile(0.5)`

**Dispersion:**
- Standard Deviation: `np.std()`
- Interquartile Range: Q3 - Q1
- Range: Max - Min
- Coefficient of Variation: (Std / Mean) × 100

**Distribution Shape:**
- Quartiles: 25th, 50th, 75th percentiles
- Min/Max values
- Skewness assessment (visual)

### 2.2 Categorical Analysis

**Frequency Analysis:**
```python
value_counts = df[column].value_counts()
proportions = value_counts / len(df)
```

**Cross-Tabulations:**
- Cover crop mix × Soil health score
- Past crop × pH levels
- Crop type × Nutrient recommendations

---

## 3. Missing Data Analysis

### 3.1 Missing Data Classification

**Patterns Identified:**
- **MCAR** (Missing Completely At Random): Test ID (99.94% missing)
- **MAR** (Missing At Random): Crop recommendations (may depend on test type)
- **MNAR** (Missing Not At Random): Enzyme tests (systematic non-collection)

### 3.2 Analysis Approach

**Missingness Quantification:**
```python
missing_count = df.isnull().sum()
missing_pct = (missing_count / len(df)) * 100
```

**Visualization:**
- Heatmap showing missing patterns across samples
- Bar chart of missingness by variable
- Pattern analysis (first 200 samples × top 30 variables)

**Thresholds Used:**
- <10% missing: Considered complete
- 10-30% missing: Usable with caution
- 30-70% missing: Limited analysis possible
- >70% missing: Exclude from primary analysis

---

## 4. Outlier Detection

### 4.1 Method: Interquartile Range (IQR)

**Formula:**
```
Lower Bound = Q1 - 1.5 × IQR
Upper Bound = Q3 + 1.5 × IQR
Outlier = value < Lower Bound OR value > Upper Bound
```

**Where:**
- Q1 = 25th percentile
- Q3 = 75th percentile
- IQR = Q3 - Q1

### 4.2 Interpretation

**Outlier Rates:**
- 0-5%: Typical distribution
- 5-10%: Moderate deviation
- 10-15%: High variability (common in environmental data)
- >15%: Investigate data quality

**Decision Rules:**
- Outliers retained if plausible (e.g., high organic matter)
- Flagged for investigation if implausible (e.g., negative values)
- Documented in outlier_analysis.csv

---

## 5. Correlation Analysis

### 5.1 Method: Pearson Correlation

**Formula:**
```
r = Σ[(xi - x̄)(yi - ȳ)] / √[Σ(xi - x̄)² × Σ(yi - ȳ)²]
```

**Properties:**
- Range: -1 to +1
- Measures linear relationships only
- Sensitive to outliers (but outliers retained)

### 5.2 Interpretation Thresholds

| |r| Range | Interpretation | Symbol |
|-----------|----------------|--------|
| 0.0-0.1 | Negligible | ~ |
| 0.1-0.3 | Weak | ± |
| 0.3-0.5 | Moderate | ±± |
| 0.5-0.7 | Strong | ±±± |
| 0.7-0.9 | Very Strong | ±±±± |
| 0.9-1.0 | Near Perfect | ±±±±± |

**Sign Interpretation:**
- Positive (+): Variables increase together
- Negative (-): One increases as other decreases

### 5.3 Multiple Comparisons

**Issue:** Testing 27 variables = 351 correlation pairs
**Risk:** False positives (Type I errors)
**Approach:**
- Report effect sizes (correlation coefficients)
- Focus on |r| > 0.5 for primary findings
- Flag |r| > 0.7 as "very strong"
- No formal p-value correction applied (exploratory analysis)

**Rationale:** EDA prioritizes discovery over hypothesis testing

---

## 6. Visualization Methods

### 6.1 Distribution Plots

**Histograms:**
- Bins: 50 (Sturges' rule override for large n)
- Purpose: Assess normality, skewness, multimodality
- Added: Mean and median lines

**Box Plots:**
- Purpose: Visualize quartiles and outliers
- Whiskers: 1.5 × IQR (consistent with outlier detection)
- Shows: Min, Q1, Median, Q3, Max, Outliers

### 6.2 Correlation Visualizations

**Heatmap:**
- Color scale: Red (negative) → White (zero) → Blue (positive)
- Range: -1 to +1 (symmetric)
- Annotations: Correlation coefficients (2 decimal places)

**Scatter Plots:**
- Purpose: Verify linear relationships
- Added: Regression line (OLS)
- Sample transparency: Alpha=0.5 (handle overplotting)

### 6.3 Categorical Plots

**Bar Charts:**
- Ordered by frequency (descending)
- Horizontal orientation for long labels
- Shows: Count or percentage

**Box Plots by Group:**
- Purpose: Compare distributions across categories
- Groups: Cover crop mix, Past crop, etc.
- Highlights: Median differences

---

## 7. Statistical Assumptions & Limitations

### 7.1 Assumptions Made

**Pearson Correlation:**
- ✓ Continuous variables (soil metrics)
- ✓ Linear relationships (verified with scatter plots)
- ✗ Normal distribution (not verified - robust with n>30)
- ✗ Homoscedasticity (not tested)
- ⚠ Independence (duplicates may violate)

**Descriptive Statistics:**
- ✓ Random sampling (assumed)
- ⚠ Independence (duplicates questionable)
- ✓ Measurement accuracy (trusted lab data)

### 7.2 Limitations Acknowledged

**Sample Independence:**
- 46% duplication violates independence assumption
- May inflate correlation strengths
- Recommendation: Reanalyze after deduplication

**Missing Data:**
- Complete case analysis may introduce bias
- Results apply to samples with complete data only
- May not generalize to full population

**Outliers:**
- Retained outliers may influence correlations
- Means more sensitive than medians
- Recommendation: Compare with robust statistics

**No Hypothesis Testing:**
- No p-values computed
- No confidence intervals
- Correlations are descriptive, not inferential
- Rationale: Exploratory phase precedes confirmatory analysis

---

## 8. Analysis Pipeline

### 8.1 Script Execution Order

```
01_eda_analysis.py
    ↓ (creates combined_soil_data.csv)
02_eda_visualizations.py
    ↓ (uses combined_soil_data.csv)
03_eda_correlations.py
    ↓ (uses combined_soil_data.csv)
04_eda_categorical_crops.py
    ↓ (uses combined_soil_data.csv)
05_eda_advanced_insights.py
    ↓ (uses combined_soil_data.csv)
```

**Dependencies:**
- All scripts require `combined_soil_data.csv`
- Scripts 2-5 are independent (can run in parallel)
- Script 1 must run first

### 8.2 Reproducibility

**Random Seeds:** Not applicable (no stochastic methods)

**Software Versions:**
- Python 3.13.7
- pandas 2.3.3
- numpy 2.3.3
- matplotlib 3.10.6
- seaborn 0.13.2
- scipy 1.16.2

**Data Versioning:**
- Raw data: `data/raw/OneDrive_1_10-5-2025/`
- Processed data: `data/processed/combined_soil_data.csv`
- Analysis date: October 5, 2025

---

## 9. Quality Control Measures

### 9.1 Data Validation

**Range Checks:**
```python
# pH: 0-14 scale
assert df['pH'].between(0, 14).all()

# Percentages: 0-100
assert df['Organic Matter'].between(0, 100).all()
```

**Logical Consistency:**
- Available N should correlate with H3A Nitrate
- Sum of nutrients should not exceed total
- Dates: Received before Reported

### 9.2 Result Validation

**Internal Consistency:**
- V1 and V2 variables show similar patterns
- Correlations symmetric (r(X,Y) = r(Y,X))
- Perfect correlations (r=1.0) verified as unit conversions

**Expected Relationships:**
- ✓ pH and Calcium positively correlated (confirmed)
- ✓ Organic Matter and Soil Health positively correlated (confirmed)
- ✓ Respiration and Health strongly correlated (confirmed)

**Sanity Checks:**
- Means > 0 for all non-negative variables
- Standard deviations > 0 (no constants)
- Outliers visually inspected (plausible)

---

## 10. Future Analytical Recommendations

### 10.1 Statistical Testing

**Recommended Tests:**
1. **Normality:** Shapiro-Wilk, Anderson-Darling
2. **Group Differences:**
   - ANOVA (if normal) or Kruskal-Wallis (if not)
   - Post-hoc: Tukey HSD or Dunn's test
3. **Correlation Significance:**
   - Test H₀: ρ = 0 with t-test
   - Bonferroni correction for multiple comparisons
4. **Regression Analysis:**
   - Multiple linear regression for Soil Health Score
   - Check assumptions (residual normality, homoscedasticity)

### 10.2 Advanced Methods

**Machine Learning:**
- Random Forest for feature importance
- Gradient Boosting for prediction accuracy
- Cross-validation (10-fold recommended)

**Causal Inference:**
- Propensity Score Matching (cover crop effects)
- Instrumental Variables (if natural experiments exist)
- Directed Acyclic Graphs (DAGs) for causal structure

**Spatial Analysis:**
- Requires geographic coordinates (not available)
- Kriging for spatial interpolation
- Spatial autocorrelation testing

**Time Series:**
- Requires temporal data (limited availability)
- Mixed-effects models for repeated measures
- Growth curve analysis for soil health trends

---

## 11. Ethical Considerations

### 11.1 Data Privacy
- No personal information in dataset (lab codes only)
- Farm locations anonymized
- Results reported in aggregate

### 11.2 Interpretation Responsibility
- Findings are descriptive, not prescriptive
- Agronomic recommendations require expert validation
- Regional context essential for application

### 11.3 Transparency
- All methods documented
- All code available for review
- Limitations clearly stated

---

## 12. References

### Statistical Methods
- Tukey, J.W. (1977). *Exploratory Data Analysis*. Addison-Wesley.
- Wilkinson, L. (1999). *The Grammar of Graphics*. Springer.

### Soil Science
- Haney, R.L. et al. (2012). The Soil Health Tool—Theory and Initial Broad-Scale Application. *Applied Soil Ecology*.
- Doran, J.W. & Parkin, T.B. (1994). Defining and Assessing Soil Quality. *SSSA Special Publication*.

### Data Analysis
- Wickham, H. (2014). Tidy Data. *Journal of Statistical Software*.
- VanderPlas, J. (2016). *Python Data Science Handbook*. O'Reilly.

---

**Document Version:** 1.0
**Last Updated:** October 5, 2025
**Author:** Claude Code
