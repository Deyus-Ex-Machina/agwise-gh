# Agricultural Soil Health Data Dictionary
**Dataset:** Combined Soil Health Analysis - All 4 Batches
**Total Samples:** 37,310
**Total Variables:** 211
**Last Updated:** October 6, 2025

---

## Table of Contents
1. [Dataset Overview](#dataset-overview)
2. [Variable Categories](#variable-categories)
3. [Complete Variable Reference](#complete-variable-reference)
4. [Data Quality Notes](#data-quality-notes)

---

## Dataset Overview

This dataset combines soil health test results from four separate data batches, 
containing comprehensive soil analysis data including:

- Physical and chemical soil properties
- Nutrient content and availability
- Soil health indicators (Haney Test metrics)
- Biological activity measurements
- Crop recommendations and economic analysis
- Cover crop information

---

## Variable Categories

### Identification & Metadata
**Count:** 51 variables

### pH & Electrical Conductivity
**Count:** 8 variables

### Organic Matter & Carbon
**Count:** 10 variables

### Nitrogen (N) Measurements
**Count:** 27 variables

### Phosphorus (P) Measurements
**Count:** 10 variables

### Potassium (K) Measurements
**Count:** 8 variables

### Secondary Macronutrients (Ca, Mg, S)
**Count:** 19 variables

### Micronutrients (Zn, Fe, Mn, Cu, B)
**Count:** 23 variables

### Soil Health Metrics
**Count:** 7 variables

### Enzyme Activity
**Count:** 6 variables

### Nutrient Recommendations
**Count:** 9 variables

### Economic Calculations
**Count:** 2 variables

### Crop Information
**Count:** 7 variables

### Cover Crop Data
**Count:** 3 variables

### CEC & Base Saturation
**Count:** 4 variables

### Regenerative Metrics
**Count:** 8 variables

### Internal Tracking
**Count:** 9 variables

---

## Complete Variable Reference

### Identification & Metadata

#### `Zip`
- **Data Type:** object
- **Non-Null Count:** 14,857 (39.8% complete)
- **Missing:** 60.2%
- **Unique Values:** 781
- **Sample Values:** 57234, 76571, 62471, 68848, 85040

#### `Date Recd`
- **Data Type:** object
- **Non-Null Count:** 19,435 (52.1% complete)
- **Missing:** 47.9%
- **Unique Values:** 634
- **Sample Values:** 12/19/2023, 10/12/2020, 11/9/2023, 6/21/2023, 7/29/2022

#### `Date Rept`
- **Data Type:** object
- **Non-Null Count:** 19,435 (52.1% complete)
- **Missing:** 47.9%
- **Unique Values:** 645
- **Sample Values:** 12/21/2023, 10/17/2020, 11/13/2023, 6/23/2023, 8/2/2022

#### `Lab No`
- **Data Type:** object
- **Non-Null Count:** 19,359 (51.9% complete)
- **Missing:** 48.1%
- **Unique Values:** 16,118
- **Sample Values:** 1, 2, 3, 4, 6

#### `WDRF Buffer`
- **Data Type:** float64
- **Non-Null Count:** 4,597 (12.3% complete)
- **Missing:** 87.7%
- **Unique Values:** 113
- **Range:** 4.70 to 665.00
- **Mean:** 6.72
- **Median:** 6.60

#### `Excess Lime`
- **Data Type:** object
- **Non-Null Count:** 19,322 (51.8% complete)
- **Missing:** 48.2%
- **Unique Values:** 11
- **Sample Values:** NONE, HIGH, LOW, 1, 3

#### `H2O Total N`
- **Data Type:** float64
- **Non-Null Count:** 14,869 (39.9% complete)
- **Missing:** 60.1%
- **Unique Values:** 4,772
- **Range:** 1.00 to 2109.30
- **Mean:** 29.81
- **Median:** 24.72

#### `H2O Organic N`
- **Data Type:** float64
- **Non-Null Count:** 14,865 (39.8% complete)
- **Missing:** 60.2%
- **Unique Values:** 2,709
- **Range:** -1.01 to 1628.00
- **Mean:** 15.04
- **Median:** 13.98

#### `H3A ICAP Aluminum`
- **Data Type:** float64
- **Non-Null Count:** 14,863 (39.8% complete)
- **Missing:** 60.2%
- **Unique Values:** 10,125
- **Range:** -2.76 to 879.75
- **Mean:** 125.60
- **Median:** 126.41

#### `H3A ICAP Sodium`
- **Data Type:** float64
- **Non-Null Count:** 14,863 (39.8% complete)
- **Missing:** 60.2%
- **Unique Values:** 6,049
- **Range:** 1.00 to 5509.43
- **Mean:** 53.32
- **Median:** 19.64

#### `Organic N:Inorganic N`
- **Data Type:** float64
- **Non-Null Count:** 14,865 (39.8% complete)
- **Missing:** 60.2%
- **Unique Values:** 821
- **Range:** -0.50 to 22.29
- **Mean:** 1.84
- **Median:** 1.43

#### `Organic N Release`
- **Data Type:** float64
- **Non-Null Count:** 14,805 (39.7% complete)
- **Missing:** 60.3%
- **Unique Values:** 2,750
- **Range:** -4.04 to 1159.80
- **Mean:** 12.95
- **Median:** 12.00

#### `Organic N Reserve`
- **Data Type:** float64
- **Non-Null Count:** 14,805 (39.7% complete)
- **Missing:** 60.3%
- **Unique Values:** 1,353
- **Range:** 0.00 to 1228.17
- **Mean:** 2.10
- **Median:** 0.00

#### `Organic P Release`
- **Data Type:** float64
- **Non-Null Count:** 14,803 (39.7% complete)
- **Missing:** 60.3%
- **Unique Values:** 1,535
- **Range:** -1.41 to 399.60
- **Mean:** 4.15
- **Median:** 3.03

#### `Organic P Reserve`
- **Data Type:** float64
- **Non-Null Count:** 14,803 (39.7% complete)
- **Missing:** 60.3%
- **Unique Values:** 1,000
- **Range:** 0.00 to 855.70
- **Mean:** 1.38
- **Median:** 0.07

#### `Beta Glucosaminidase ppm pNP g-1 soil h-1`
- **Data Type:** float64
- **Non-Null Count:** 0 (0.0% complete)
- **Missing:** 100.0%
- **Unique Values:** 0

#### `Test ID`
- **Data Type:** object
- **Non-Null Count:** 152 (0.4% complete)
- **Missing:** 99.6%
- **Unique Values:** 4
- **Sample Values:** 100, N/A , 100.0, Company

#### `Wdrf Buffer`
- **Data Type:** object
- **Non-Null Count:** 1,606 (4.3% complete)
- **Missing:** 95.7%
- **Unique Values:** 69
- **Sample Values:** 0.0, 6.7, 6.8, 6.6, 6.5

#### `H2O Total Org. C, ppm C`
- **Data Type:** object
- **Non-Null Count:** 4,538 (12.2% complete)
- **Missing:** 87.8%
- **Unique Values:** 3,842
- **Sample Values:** 42, 41, 44, 51, 52

#### `H3A Sodium, ppm Na`
- **Data Type:** object
- **Non-Null Count:** 4,438 (11.9% complete)
- **Missing:** 88.1%
- **Unique Values:** 2,923
- **Sample Values:** 8, 8.0, 15.0, 7.0, 13.0

#### `H3A Aluminum, ppm Al`
- **Data Type:** object
- **Non-Null Count:** 4,438 (11.9% complete)
- **Missing:** 88.1%
- **Unique Values:** 3,781
- **Sample Values:** 5.8, 10.8, 9.0, 12.7, 10.9

#### `Microbially Active C, %`
- **Data Type:** object
- **Non-Null Count:** 4,438 (11.9% complete)
- **Missing:** 88.1%
- **Unique Values:** 3,147
- **Sample Values:** 9.7, 12.4, 9.4, 18.7, 18.6

#### `H2O Org. C:Org. N `
- **Data Type:** float64
- **Non-Null Count:** 3,510 (9.4% complete)
- **Missing:** 90.6%
- **Unique Values:** 1,050
- **Range:** 2.16 to 181.92
- **Mean:** 12.47
- **Median:** 12.27

#### `H2O Org. N:H3A Inorg. N`
- **Data Type:** object
- **Non-Null Count:** 4,438 (11.9% complete)
- **Missing:** 88.1%
- **Unique Values:** 576
- **Sample Values:** 0.6, 1.44, 1.21, 0.81, 0.54

#### `Organic N Release, ppm N`
- **Data Type:** object
- **Non-Null Count:** 4,438 (11.9% complete)
- **Missing:** 88.1%
- **Unique Values:** 2,145
- **Sample Values:** 10.82, 13.99, 11.6, 11.87, 14.14

#### `Organic N Reserve, ppm N`
- **Data Type:** object
- **Non-Null Count:** 4,438 (11.9% complete)
- **Missing:** 88.1%
- **Unique Values:** 992
- **Sample Values:** 0.0, 0, 2.13, 2.46, 1.3

#### `Organic P Release, ppm P`
- **Data Type:** object
- **Non-Null Count:** 4,438 (11.9% complete)
- **Missing:** 88.1%
- **Unique Values:** 1,141
- **Sample Values:** 0.26, 2.0, 1.2, 2.43, 2.3

#### `Organic P Reserve, ppm P`
- **Data Type:** object
- **Non-Null Count:** 4,438 (11.9% complete)
- **Missing:** 88.1%
- **Unique Values:** 746
- **Sample Values:** 0.0, 0, 0.6, 0.8, 0.43

#### `Available K, lbs/A`
- **Data Type:** object
- **Non-Null Count:** 4,438 (11.9% complete)
- **Missing:** 88.1%
- **Unique Values:** 3,966
- **Sample Values:** 61.9, 58.7, 62.3, 69.6, 96.52

#### `Lab ID`
- **Data Type:** float64
- **Non-Null Count:** 76 (0.2% complete)
- **Missing:** 99.8%
- **Unique Values:** 76
- **Range:** 144.00 to 243.00
- **Mean:** 187.82
- **Median:** 181.50

#### `H1`
- **Data Type:** object
- **Non-Null Count:** 51 (0.1% complete)
- **Missing:** 99.9%
- **Unique Values:** 51
- **Sample Values:** Lab No, C6N13F, C6N135, C6N136, C6N137

#### `H2O Org. C:Org. N`
- **Data Type:** object
- **Non-Null Count:** 928 (2.5% complete)
- **Missing:** 97.5%
- **Unique Values:** 568
- **Sample Values:** 13.42, 12.96, 13.75, 13.74, 10.23

#### `NH4OAc-Sodium, ppm Na `
- **Data Type:** float64
- **Non-Null Count:** 2 (0.0% complete)
- **Missing:** 100.0%
- **Unique Values:** 2
- **Range:** 22.26 to 22.32
- **Mean:** 22.29
- **Median:** 22.29

#### `CaNO3-Chloride, ppm Cl`
- **Data Type:** float64
- **Non-Null Count:** 0 (0.0% complete)
- **Missing:** 100.0%
- **Unique Values:** 0

#### `Bulk Density, g/cm3`
- **Data Type:** float64
- **Non-Null Count:** 0 (0.0% complete)
- **Missing:** 100.0%
- **Unique Values:** 0

#### `MODUS ID's`
- **Data Type:** object
- **Non-Null Count:** 25 (0.1% complete)
- **Missing:** 99.9%
- **Unique Values:** 2
- **Sample Values:** SOIL HEALTH, Sample Type

#### `H2`
- **Data Type:** object
- **Non-Null Count:** 1 (0.0% complete)
- **Missing:** 100.0%
- **Unique Values:** 1
- **Sample Values:** Test ID

#### `H3`
- **Data Type:** object
- **Non-Null Count:** 25 (0.1% complete)
- **Missing:** 99.9%
- **Unique Values:** 2
- **Sample Values:** 3/30/2022, Date Recd

#### `H4`
- **Data Type:** object
- **Non-Null Count:** 25 (0.1% complete)
- **Missing:** 99.9%
- **Unique Values:** 2
- **Sample Values:** 4/1/2022, Date Rept

#### `H5`
- **Data Type:** object
- **Non-Null Count:** 25 (0.1% complete)
- **Missing:** 99.9%
- **Unique Values:** 2
- **Sample Values:** 117, Cust ID

#### `H6`
- **Data Type:** object
- **Non-Null Count:** 25 (0.1% complete)
- **Missing:** 99.9%
- **Unique Values:** 2
- **Sample Values:** TRISH JACKSON, Name

#### `H7`
- **Data Type:** object
- **Non-Null Count:** 25 (0.1% complete)
- **Missing:** 99.9%
- **Unique Values:** 2
- **Sample Values:** PRAIRIECHAR INC., Company

#### `H8`
- **Data Type:** object
- **Non-Null Count:** 25 (0.1% complete)
- **Missing:** 99.9%
- **Unique Values:** 3
- **Sample Values:** Hunnicutt Farms , Hunnicutt Farms, Grower

#### `H9`
- **Data Type:** object
- **Non-Null Count:** 25 (0.1% complete)
- **Missing:** 99.9%
- **Unique Values:** 25
- **Sample Values:** Field ID, hunn0011d-2, hunn0023-2, hunn0023-1, hunn0021-2

#### `H10`
- **Data Type:** object
- **Non-Null Count:** 25 (0.1% complete)
- **Missing:** 99.9%
- **Unique Values:** 2
- **Sample Values:** 3/28/2022, Sample ID 1

#### `H11`
- **Data Type:** object
- **Non-Null Count:** 1 (0.0% complete)
- **Missing:** 100.0%
- **Unique Values:** 1
- **Sample Values:** Sample ID 2

#### `H12`
- **Data Type:** object
- **Non-Null Count:** 1 (0.0% complete)
- **Missing:** 100.0%
- **Unique Values:** 1
- **Sample Values:** Sample ID 3

#### `H13`
- **Data Type:** object
- **Non-Null Count:** 25 (0.1% complete)
- **Missing:** 99.9%
- **Unique Values:** 2
- **Sample Values:** 0, Beginning Depth

#### `H14`
- **Data Type:** object
- **Non-Null Count:** 25 (0.1% complete)
- **Missing:** 99.9%
- **Unique Values:** 2
- **Sample Values:** 6, Ending Depth

#### `v`
- **Data Type:** float64
- **Non-Null Count:** 2 (0.0% complete)
- **Missing:** 100.0%
- **Unique Values:** 1
- **Range:** 105.00 to 105.00
- **Mean:** 105.00
- **Median:** 105.00

#### `Score`
- **Data Type:** float64
- **Non-Null Count:** 142 (0.4% complete)
- **Missing:** 99.6%
- **Unique Values:** 138
- **Range:** -1.00 to 37.77
- **Mean:** 9.98
- **Median:** 9.36

### pH & Electrical Conductivity

#### `1:1 Soil pH`
- **Data Type:** float64
- **Non-Null Count:** 14,789 (39.6% complete)
- **Missing:** 60.4%
- **Unique Values:** 333
- **Range:** 3.90 to 9.70
- **Mean:** 6.98
- **Median:** 7.00

#### `1:1 Soluble Salt`
- **Data Type:** float64
- **Non-Null Count:** 14,789 (39.6% complete)
- **Missing:** 60.4%
- **Unique Values:** 277
- **Range:** 0.01 to 40.80
- **Mean:** 0.29
- **Median:** 0.17

#### `Soil pH 1:1`
- **Data Type:** object
- **Non-Null Count:** 4,454 (11.9% complete)
- **Missing:** 88.1%
- **Unique Values:** 222
- **Sample Values:** 7.5, 7.4, 7.2, 7.3, 7.7

#### `1:1 Electrical Conductivity, mmho/cm`
- **Data Type:** object
- **Non-Null Count:** 4,530 (12.1% complete)
- **Missing:** 87.9%
- **Unique Values:** 182
- **Sample Values:** 0.13, 0.1, 0.14, 0.16, 0.15

#### `1:1 pH`
- **Data Type:** float64
- **Non-Null Count:** 76 (0.2% complete)
- **Missing:** 99.8%
- **Unique Values:** 29
- **Range:** 4.70 to 8.30
- **Mean:** 6.95
- **Median:** 7.15

#### `Woodruff Buffer pH`
- **Data Type:** float64
- **Non-Null Count:** 20 (0.0% complete)
- **Missing:** 100.0%
- **Unique Values:** 8
- **Range:** 5.80 to 6.80
- **Mean:** 6.38
- **Median:** 6.40

#### `S-PH-1:1.02.07`
- **Data Type:** object
- **Non-Null Count:** 25 (0.1% complete)
- **Missing:** 99.9%
- **Unique Values:** 14
- **Sample Values:** 6, 5.9, 5.8, 6.5, 6.3

#### `S-BPH-MWB.02`
- **Data Type:** object
- **Non-Null Count:** 19 (0.0% complete)
- **Missing:** 100.0%
- **Unique Values:** 7
- **Sample Values:** 6.5, 6.8, 6.6, 6.4, Wdrf Buffer

### Organic Matter & Carbon

#### `Organic Matter`
- **Data Type:** object
- **Non-Null Count:** 14,802 (39.7% complete)
- **Missing:** 60.3%
- **Unique Values:** 414
- **Sample Values:** 2.8, 2.6, 2.3, 2.7, 2.4

#### `CO2-C`
- **Data Type:** float64
- **Non-Null Count:** 14,803 (39.7% complete)
- **Missing:** 60.3%
- **Unique Values:** 9,050
- **Range:** 1.00 to 1023.75
- **Mean:** 84.28
- **Median:** 52.10

#### `H2O Total Organic C`
- **Data Type:** float64
- **Non-Null Count:** 14,869 (39.9% complete)
- **Missing:** 60.1%
- **Unique Values:** 10,533
- **Range:** 1.00 to 27107.05
- **Mean:** 182.44
- **Median:** 167.77

#### `% MAC`
- **Data Type:** float64
- **Non-Null Count:** 14,803 (39.7% complete)
- **Missing:** 60.3%
- **Unique Values:** 7,306
- **Range:** 0.28 to 839.81
- **Mean:** 46.22
- **Median:** 32.02

#### `Organic C:N`
- **Data Type:** float64
- **Non-Null Count:** 14,865 (39.8% complete)
- **Missing:** 60.2%
- **Unique Values:** 1,328
- **Range:** -0.99 to 181.92
- **Mean:** 12.39
- **Median:** 12.23

#### `Organic Matter, % LOI`
- **Data Type:** object
- **Non-Null Count:** 4,540 (12.2% complete)
- **Missing:** 87.8%
- **Unique Values:** 273
- **Sample Values:** 0.6, 2.5, 2.8, 2.6, 2.7

#### `Soil Respiration, ppm CO2-C`
- **Data Type:** object
- **Non-Null Count:** 4,538 (12.2% complete)
- **Missing:** 87.8%
- **Unique Values:** 3,627
- **Sample Values:** 6.8, 6.2, 6.3, 4.9, 3.1

#### `Total Organic Carbon, % C`
- **Data Type:** float64
- **Non-Null Count:** 0 (0.0% complete)
- **Missing:** 100.0%
- **Unique Values:** 0

#### `Total Carbon, % C`
- **Data Type:** float64
- **Non-Null Count:** 0 (0.0% complete)
- **Missing:** 100.0%
- **Unique Values:** 0

#### `Microbial Carbon Capture, T/A`
- **Data Type:** float64
- **Non-Null Count:** 0 (0.0% complete)
- **Missing:** 100.0%
- **Unique Values:** 0

### Nitrogen (N) Measurements

#### `H3A Nitrate`
- **Data Type:** float64
- **Non-Null Count:** 14,882 (39.9% complete)
- **Missing:** 60.1%
- **Unique Values:** 1,997
- **Range:** 0.10 to 361.00
- **Mean:** 12.16
- **Median:** 7.13

#### `H3A Ammonium`
- **Data Type:** float64
- **Non-Null Count:** 14,865 (39.8% complete)
- **Missing:** 60.2%
- **Unique Values:** 1,147
- **Range:** -2.37 to 523.00
- **Mean:** 3.35
- **Median:** 2.26

#### `H3A Inorganic Nitrogen`
- **Data Type:** float64
- **Non-Null Count:** 14,865 (39.8% complete)
- **Missing:** 60.2%
- **Unique Values:** 3,873
- **Range:** 0.20 to 585.30
- **Mean:** 15.52
- **Median:** 9.80

#### `Lbs N Difference`
- **Data Type:** float64
- **Non-Null Count:** 14,803 (39.7% complete)
- **Missing:** 60.3%
- **Unique Values:** 5,225
- **Range:** -5.47 to 2214.78
- **Mean:** 33.04
- **Median:** 29.01

#### `N savings`
- **Data Type:** float64
- **Non-Null Count:** 14,803 (39.7% complete)
- **Missing:** 60.3%
- **Unique Values:** 5,399
- **Range:** -5.69 to 2303.37
- **Mean:** 32.57
- **Median:** 28.36

#### `Nitrogen Rec 1`
- **Data Type:** object
- **Non-Null Count:** 2,585 (6.9% complete)
- **Missing:** 93.1%
- **Unique Values:** 111
- **Sample Values:** 0, 0.0, 5, 45, 40

#### `Iron Rec 1`
- **Data Type:** object
- **Non-Null Count:** 2,583 (6.9% complete)
- **Missing:** 93.1%
- **Unique Values:** 7
- **Sample Values:** 0, 0.0, ***, -1, -1.0

#### `Nitrogen Rec 2`
- **Data Type:** object
- **Non-Null Count:** 928 (2.5% complete)
- **Missing:** 97.5%
- **Unique Values:** 107
- **Sample Values:** 0, 0.0, 5, 145, 130

#### `Iron Rec 2`
- **Data Type:** object
- **Non-Null Count:** 926 (2.5% complete)
- **Missing:** 97.5%
- **Unique Values:** 6
- **Sample Values:** 0, 0.0, ***, Iron Rec 2, -1.0

#### `Nitrogen Rec 3`
- **Data Type:** object
- **Non-Null Count:** 98 (0.3% complete)
- **Missing:** 99.7%
- **Unique Values:** 46
- **Sample Values:** 0.0, 0, 105, 240.0, 160

#### `Iron Rec 3`
- **Data Type:** object
- **Non-Null Count:** 98 (0.3% complete)
- **Missing:** 99.7%
- **Unique Values:** 4
- **Sample Values:** 0, 0.0, ***, Iron Rec 3

#### `H2O Total N, ppm N`
- **Data Type:** object
- **Non-Null Count:** 4,538 (12.2% complete)
- **Missing:** 87.8%
- **Unique Values:** 2,778
- **Sample Values:** 24.3, 13.6, 12.3, 12.8, 22.9

#### `H2O Org. N, ppm N`
- **Data Type:** object
- **Non-Null Count:** 4,538 (12.2% complete)
- **Missing:** 87.8%
- **Unique Values:** 1,962
- **Sample Values:** 3.9, 4.4, 4.7, 3.1, 4.0

#### `H3A Nitrate, ppm NO3-N`
- **Data Type:** object
- **Non-Null Count:** 4,538 (12.2% complete)
- **Missing:** 87.8%
- **Unique Values:** 1,438
- **Sample Values:** 10.1, 11.7, 10.6, 10.5, 11.1

#### `H3A Ammonium, ppm NH4-N`
- **Data Type:** object
- **Non-Null Count:** 4,538 (12.2% complete)
- **Missing:** 87.8%
- **Unique Values:** 798
- **Sample Values:** 1.2, 1.0, 1.3, 1.1, 0.9

#### `H3A Inorganic N, ppm N`
- **Data Type:** object
- **Non-Null Count:** 4,538 (12.2% complete)
- **Missing:** 87.8%
- **Unique Values:** 2,340
- **Sample Values:** 6.3, 8.9, 7.9, 7.0, 6.0

#### `Available N, lbs/A`
- **Data Type:** object
- **Non-Null Count:** 4,438 (11.9% complete)
- **Missing:** 88.1%
- **Unique Values:** 3,438
- **Sample Values:** 29.1, 37.6, 29.7, 40.5, 35.48

#### `Traditional Test N, lbs/A`
- **Data Type:** object
- **Non-Null Count:** 4,438 (11.9% complete)
- **Missing:** 88.1%
- **Unique Values:** 1,999
- **Sample Values:** 25.2, 18.9, 18.18, 19.08, 26.64

#### `Haney Test N, lbs/A`
- **Data Type:** object
- **Non-Null Count:** 4,438 (11.9% complete)
- **Missing:** 88.1%
- **Unique Values:** 3,438
- **Sample Values:** 29.1, 37.6, 29.7, 40.5, 35.48

#### `N Difference, lbs/A`
- **Data Type:** object
- **Non-Null Count:** 4,438 (11.9% complete)
- **Missing:** 88.1%
- **Unique Values:** 2,842
- **Sample Values:** 10.3, 7.7, 10.4, 10.9, 8.9

#### `N Savings, $`
- **Data Type:** object
- **Non-Null Count:** 4,438 (11.9% complete)
- **Missing:** 88.1%
- **Unique Values:** 3,074
- **Sample Values:** 36.39, 21.34, 7.86, 18.1, 19.74

#### `1N KCl-Nitrate, ppm NO3-N`
- **Data Type:** float64
- **Non-Null Count:** 2 (0.0% complete)
- **Missing:** 100.0%
- **Unique Values:** 2
- **Range:** 0.90 to 1.60
- **Mean:** 1.25
- **Median:** 1.25

#### `1N KCl-Nitrate, lbs/A N`
- **Data Type:** float64
- **Non-Null Count:** 2 (0.0% complete)
- **Missing:** 100.0%
- **Unique Values:** 2
- **Range:** 2.00 to 3.00
- **Mean:** 2.50
- **Median:** 2.50

#### `Total Nitrogen, % N`
- **Data Type:** float64
- **Non-Null Count:** 0 (0.0% complete)
- **Missing:** 100.0%
- **Unique Values:** 0

#### `Boron Rec 1`
- **Data Type:** float64
- **Non-Null Count:** 0 (0.0% complete)
- **Missing:** 100.0%
- **Unique Values:** 0

#### `Boron Rec 2`
- **Data Type:** float64
- **Non-Null Count:** 0 (0.0% complete)
- **Missing:** 100.0%
- **Unique Values:** 0

#### `Boron Rec 3`
- **Data Type:** float64
- **Non-Null Count:** 0 (0.0% complete)
- **Missing:** 100.0%
- **Unique Values:** 0

### Phosphorus (P) Measurements

#### `H3A Total Phosphorus`
- **Data Type:** float64
- **Non-Null Count:** 14,863 (39.8% complete)
- **Missing:** 60.2%
- **Unique Values:** 6,723
- **Range:** 0.41 to 1535.88
- **Mean:** 41.06
- **Median:** 23.66

#### `H3A Inorganic Phosphorus`
- **Data Type:** float64
- **Non-Null Count:** 14,863 (39.8% complete)
- **Missing:** 60.2%
- **Unique Values:** 2,535
- **Range:** 0.21 to 1090.00
- **Mean:** 35.53
- **Median:** 19.40

#### `H3A Organic Phosphorus`
- **Data Type:** float64
- **Non-Null Count:** 14,863 (39.8% complete)
- **Missing:** 60.2%
- **Unique Values:** 1,793
- **Range:** -1.38 to 881.49
- **Mean:** 5.53
- **Median:** 3.96

#### `Phosphodiesterase ppm pNP g-1 soil h-1`
- **Data Type:** float64
- **Non-Null Count:** 0 (0.0% complete)
- **Missing:** 100.0%
- **Unique Values:** 0

#### `Phosphomonoesterases (Acid) ppm pNP g-1 soil h-1`
- **Data Type:** float64
- **Non-Null Count:** 0 (0.0% complete)
- **Missing:** 100.0%
- **Unique Values:** 0

#### `Phosphomonoesterases (Alkaline) ppm pNP g-1 soil h-1`
- **Data Type:** float64
- **Non-Null Count:** 0 (0.0% complete)
- **Missing:** 100.0%
- **Unique Values:** 0

#### `H3A Total Phosphorus, ppm P`
- **Data Type:** object
- **Non-Null Count:** 4,538 (12.2% complete)
- **Missing:** 87.8%
- **Unique Values:** 3,247
- **Sample Values:** 3, 4, 10, 5, 13

#### `H3A Inorganic Phosphorus, ppm PO4-P`
- **Data Type:** object
- **Non-Null Count:** 4,538 (12.2% complete)
- **Missing:** 87.8%
- **Unique Values:** 1,698
- **Sample Values:** 11.3, 2.6, 17.4, 12.5, 11.0

#### `H3A Organic Phosphorus, ppm P`
- **Data Type:** object
- **Non-Null Count:** 4,538 (12.2% complete)
- **Missing:** 87.8%
- **Unique Values:** 1,333
- **Sample Values:** 0.9, 1.0, 0.8, 2.0, 2.5

#### `M3-Phosphate, ppm PO4-P`
- **Data Type:** float64
- **Non-Null Count:** 2 (0.0% complete)
- **Missing:** 100.0%
- **Unique Values:** 2
- **Range:** 176.40 to 200.10
- **Mean:** 188.25
- **Median:** 188.25

### Potassium (K) Measurements

#### `H3A ICAP Potassium`
- **Data Type:** float64
- **Non-Null Count:** 14,863 (39.8% complete)
- **Missing:** 60.2%
- **Unique Values:** 9,904
- **Range:** 1.00 to 18978.92
- **Mean:** 111.26
- **Median:** 77.11

#### `Available K`
- **Data Type:** float64
- **Non-Null Count:** 14,863 (39.8% complete)
- **Missing:** 60.2%
- **Unique Values:** 10,631
- **Range:** 1.20 to 22774.70
- **Mean:** 133.51
- **Median:** 92.54

#### `K2O Rec 1`
- **Data Type:** object
- **Non-Null Count:** 2,583 (6.9% complete)
- **Missing:** 93.1%
- **Unique Values:** 66
- **Sample Values:** 0, 0.0, 35, 30, 40

#### `K2O Rec 2`
- **Data Type:** object
- **Non-Null Count:** 926 (2.5% complete)
- **Missing:** 97.5%
- **Unique Values:** 51
- **Sample Values:** 0, 0.0, 25, 30, 20

#### `K2O Rec 3`
- **Data Type:** object
- **Non-Null Count:** 98 (0.3% complete)
- **Missing:** 99.7%
- **Unique Values:** 22
- **Sample Values:** 0.0, 0, 30.0, 20, 35.0

#### `H3A Potassium, ppm K`
- **Data Type:** object
- **Non-Null Count:** 4,538 (12.2% complete)
- **Missing:** 87.8%
- **Unique Values:** 3,828
- **Sample Values:** 52, 20, 49, 57, 33

#### `NH4OAc-Potassium, ppm K `
- **Data Type:** float64
- **Non-Null Count:** 2 (0.0% complete)
- **Missing:** 100.0%
- **Unique Values:** 2
- **Range:** 95.50 to 107.30
- **Mean:** 101.40
- **Median:** 101.40

#### `Potassium, % Sat`
- **Data Type:** float64
- **Non-Null Count:** 2 (0.0% complete)
- **Missing:** 100.0%
- **Unique Values:** 1
- **Range:** 2.00 to 2.00
- **Mean:** 2.00
- **Median:** 2.00

### Secondary Macronutrients (Ca, Mg, S)

#### `H3A ICAP Calcium`
- **Data Type:** float64
- **Non-Null Count:** 14,863 (39.8% complete)
- **Missing:** 60.2%
- **Unique Values:** 13,470
- **Range:** 1.00 to 10416.37
- **Mean:** 1041.25
- **Median:** 714.30

#### `H3A ICAP Sulfur`
- **Data Type:** float64
- **Non-Null Count:** 14,863 (39.8% complete)
- **Missing:** 60.2%
- **Unique Values:** 3,996
- **Range:** 0.69 to 7867.88
- **Mean:** 28.09
- **Median:** 6.69

#### `H3A ICAP Magnesium`
- **Data Type:** float64
- **Non-Null Count:** 14,863 (39.8% complete)
- **Missing:** 60.2%
- **Unique Values:** 10,928
- **Range:** 1.00 to 1675.87
- **Mean:** 164.59
- **Median:** 139.73

#### `Magnesium Rec 1`
- **Data Type:** object
- **Non-Null Count:** 2,583 (6.9% complete)
- **Missing:** 93.1%
- **Unique Values:** 11
- **Sample Values:** 0, 0.0, 15, 10, 25

#### `Sulfur Rec 1`
- **Data Type:** object
- **Non-Null Count:** 2,583 (6.9% complete)
- **Missing:** 93.1%
- **Unique Values:** 86
- **Sample Values:** 0, 0.0, 10, 13, 9

#### `Magnesium Rec 2`
- **Data Type:** object
- **Non-Null Count:** 926 (2.5% complete)
- **Missing:** 97.5%
- **Unique Values:** 9
- **Sample Values:** 0, 0.0, 10.0, 15, 15.0

#### `Sulfur Rec 2`
- **Data Type:** object
- **Non-Null Count:** 926 (2.5% complete)
- **Missing:** 97.5%
- **Unique Values:** 70
- **Sample Values:** 0, 0.0, 10, 6, 16

#### `Magnesium Rec 3`
- **Data Type:** object
- **Non-Null Count:** 98 (0.3% complete)
- **Missing:** 99.7%
- **Unique Values:** 4
- **Sample Values:** 0.0, 0, Magnesium Rec 3, 15.0

#### `Sulfur Rec 3`
- **Data Type:** object
- **Non-Null Count:** 98 (0.3% complete)
- **Missing:** 99.7%
- **Unique Values:** 37
- **Sample Values:** 0.0, 0, 20, 15, 32.0

#### `H3A Calcium, ppm Ca`
- **Data Type:** object
- **Non-Null Count:** 4,438 (11.9% complete)
- **Missing:** 88.1%
- **Unique Values:** 4,290
- **Sample Values:** 3051, 3080, 2861, 629.0, 3213

#### `H3A Magnesium, ppm Mg`
- **Data Type:** object
- **Non-Null Count:** 3,872 (10.4% complete)
- **Missing:** 89.6%
- **Unique Values:** 3,584
- **Sample Values:** 135.0, 109.85, 160, 167.0, 167.41

#### `H3A Sulfur, ppm S`
- **Data Type:** object
- **Non-Null Count:** 4,438 (11.9% complete)
- **Missing:** 88.1%
- **Unique Values:** 2,171
- **Sample Values:** 3.47, 3.6, 4.04, 3.67, 5.74

#### `H3A Magnessium, ppm Mg`
- **Data Type:** float64
- **Non-Null Count:** 566 (1.5% complete)
- **Missing:** 98.5%
- **Unique Values:** 307
- **Range:** 26.00 to 768.67
- **Mean:** 161.96
- **Median:** 138.00

#### `H2O Calcium, ppm Ca`
- **Data Type:** float64
- **Non-Null Count:** 2 (0.0% complete)
- **Missing:** 100.0%
- **Unique Values:** 2
- **Range:** 34.50 to 64.50
- **Mean:** 49.50
- **Median:** 49.50

#### `M3-Sulfur, ppm S`
- **Data Type:** float64
- **Non-Null Count:** 2 (0.0% complete)
- **Missing:** 100.0%
- **Unique Values:** 2
- **Range:** 14.20 to 17.50
- **Mean:** 15.85
- **Median:** 15.85

#### `NH4OAc-Calcium, ppm Ca `
- **Data Type:** float64
- **Non-Null Count:** 2 (0.0% complete)
- **Missing:** 100.0%
- **Unique Values:** 2
- **Range:** 972.00 to 1077.00
- **Mean:** 1024.50
- **Median:** 1024.50

#### `NH4OAc-Magnesium, ppm Mg`
- **Data Type:** float64
- **Non-Null Count:** 2 (0.0% complete)
- **Missing:** 100.0%
- **Unique Values:** 2
- **Range:** 174.17 to 200.50
- **Mean:** 187.33
- **Median:** 187.33

#### `Calcium, % Sat`
- **Data Type:** float64
- **Non-Null Count:** 2 (0.0% complete)
- **Missing:** 100.0%
- **Unique Values:** 2
- **Range:** 39.00 to 46.00
- **Mean:** 42.50
- **Median:** 42.50

#### `Magnesium, % Sat`
- **Data Type:** float64
- **Non-Null Count:** 2 (0.0% complete)
- **Missing:** 100.0%
- **Unique Values:** 2
- **Range:** 12.00 to 13.00
- **Mean:** 12.50
- **Median:** 12.50

### Micronutrients (Zn, Fe, Mn, Cu, B)

#### `H3A ICAP Iron`
- **Data Type:** float64
- **Non-Null Count:** 14,863 (39.8% complete)
- **Missing:** 60.2%
- **Unique Values:** 8,643
- **Range:** 0.79 to 692.63
- **Mean:** 61.93
- **Median:** 55.62

#### `H3A ICAP Zinc`
- **Data Type:** float64
- **Non-Null Count:** 14,863 (39.8% complete)
- **Missing:** 60.2%
- **Unique Values:** 834
- **Range:** 0.00 to 51.70
- **Mean:** 1.19
- **Median:** 0.66

#### `H3A ICAP Manganese`
- **Data Type:** float64
- **Non-Null Count:** 14,863 (39.8% complete)
- **Missing:** 60.2%
- **Unique Values:** 3,005
- **Range:** 0.07 to 398.70
- **Mean:** 9.12
- **Median:** 5.40

#### `H3A ICAP Copper`
- **Data Type:** float64
- **Non-Null Count:** 14,863 (39.8% complete)
- **Missing:** 60.2%
- **Unique Values:** 388
- **Range:** 0.00 to 64.55
- **Mean:** 0.37
- **Median:** 0.20

#### `Zinc Rec 1`
- **Data Type:** object
- **Non-Null Count:** 2,583 (6.9% complete)
- **Missing:** 93.1%
- **Unique Values:** 32
- **Sample Values:** 0, 0.0, 13, 2, 3.0

#### `Manganese Rec 1`
- **Data Type:** object
- **Non-Null Count:** 2,583 (6.9% complete)
- **Missing:** 93.1%
- **Unique Values:** 25
- **Sample Values:** 0, 0.0, 6, 7, 3

#### `Copper Rec 1`
- **Data Type:** object
- **Non-Null Count:** 2,583 (6.9% complete)
- **Missing:** 93.1%
- **Unique Values:** 15
- **Sample Values:** 0, 0.0, 0.6, 1.7, 2.8

#### `Zinc Rec 2`
- **Data Type:** object
- **Non-Null Count:** 926 (2.5% complete)
- **Missing:** 97.5%
- **Unique Values:** 31
- **Sample Values:** 0, 0.0, 14, 2, 2.0

#### `Manganese Rec 2`
- **Data Type:** object
- **Non-Null Count:** 926 (2.5% complete)
- **Missing:** 97.5%
- **Unique Values:** 24
- **Sample Values:** 0, 0.0, 7.0, 7, 2

#### `Copper Rec 2`
- **Data Type:** object
- **Non-Null Count:** 926 (2.5% complete)
- **Missing:** 97.5%
- **Unique Values:** 10
- **Sample Values:** 0, 0.0, 1.7, 2.8, 0.6

#### `Zinc Rec 3`
- **Data Type:** object
- **Non-Null Count:** 98 (0.3% complete)
- **Missing:** 99.7%
- **Unique Values:** 13
- **Sample Values:** 0.0, 0, 1, 5.0, 2.0

#### `Manganese Rec 3`
- **Data Type:** object
- **Non-Null Count:** 98 (0.3% complete)
- **Missing:** 99.7%
- **Unique Values:** 8
- **Sample Values:** 0.0, 0, Manganese Rec 3, 9.0, 3.0

#### `Copper Rec 3`
- **Data Type:** object
- **Non-Null Count:** 98 (0.3% complete)
- **Missing:** 99.7%
- **Unique Values:** 6
- **Sample Values:** 0.0, 0, Copper Rec 3, 1.7, 2.8

#### `H3A Zinc, ppm Zn`
- **Data Type:** object
- **Non-Null Count:** 4,438 (11.9% complete)
- **Missing:** 88.1%
- **Unique Values:** 723
- **Sample Values:** 0.01, 0.02, 0.03, 0.33, 0.51

#### `H3A Iron, ppm Fe`
- **Data Type:** object
- **Non-Null Count:** 4,438 (11.9% complete)
- **Missing:** 88.1%
- **Unique Values:** 3,443
- **Sample Values:** 1.5, 1.8, 2.8, 1.9, 2.3

#### `H3A Manganese, ppm Mn`
- **Data Type:** object
- **Non-Null Count:** 4,438 (11.9% complete)
- **Missing:** 88.1%
- **Unique Values:** 1,692
- **Sample Values:** 1.2, 3.6, 4.1, 2.1, 3.5

#### `H3A Copper, ppm Cu`
- **Data Type:** object
- **Non-Null Count:** 4,438 (11.9% complete)
- **Missing:** 88.1%
- **Unique Values:** 248
- **Sample Values:** 0.16, 0.08, 0.11, 0.13, 0.09

#### `DTPA-Zinc, ppm Zn`
- **Data Type:** float64
- **Non-Null Count:** 2 (0.0% complete)
- **Missing:** 100.0%
- **Unique Values:** 2
- **Range:** 0.56 to 1.19
- **Mean:** 0.88
- **Median:** 0.88

#### `DTPA-Iron, ppm Fe`
- **Data Type:** float64
- **Non-Null Count:** 2 (0.0% complete)
- **Missing:** 100.0%
- **Unique Values:** 2
- **Range:** 127.42 to 144.87
- **Mean:** 136.15
- **Median:** 136.15

#### `DTPA-Manganese, ppm Mn `
- **Data Type:** float64
- **Non-Null Count:** 2 (0.0% complete)
- **Missing:** 100.0%
- **Unique Values:** 2
- **Range:** 10.36 to 11.29
- **Mean:** 10.82
- **Median:** 10.82

#### `DTPA-Copper, ppm Cu`
- **Data Type:** float64
- **Non-Null Count:** 2 (0.0% complete)
- **Missing:** 100.0%
- **Unique Values:** 2
- **Range:** 0.25 to 0.49
- **Mean:** 0.37
- **Median:** 0.37

#### `H2O-Boron, ppm B`
- **Data Type:** float64
- **Non-Null Count:** 2 (0.0% complete)
- **Missing:** 100.0%
- **Unique Values:** 2
- **Range:** 0.87 to 0.92
- **Mean:** 0.90
- **Median:** 0.90

#### `M3 Boron, ppm B`
- **Data Type:** float64
- **Non-Null Count:** 1 (0.0% complete)
- **Missing:** 100.0%
- **Unique Values:** 1
- **Range:** 0.54 to 0.54
- **Mean:** 0.54
- **Median:** 0.54

### Soil Health Metrics

#### `Soil Health Calculation`
- **Data Type:** float64
- **Non-Null Count:** 14,803 (39.7% complete)
- **Missing:** 60.3%
- **Unique Values:** 2,839
- **Range:** 0.11 to 608.23
- **Mean:** 12.14
- **Median:** 10.29

#### `Available N`
- **Data Type:** float64
- **Non-Null Count:** 14,882 (39.9% complete)
- **Missing:** 60.1%
- **Unique Values:** 7,426
- **Range:** -3.65 to 2364.30
- **Mean:** 57.98
- **Median:** 46.46

#### `Available P`
- **Data Type:** float64
- **Non-Null Count:** 14,863 (39.8% complete)
- **Missing:** 60.2%
- **Unique Values:** 9,579
- **Range:** 0.94 to 3182.09
- **Mean:** 91.22
- **Median:** 52.46

#### `Traditional N`
- **Data Type:** float64
- **Non-Null Count:** 14,863 (39.8% complete)
- **Missing:** 60.2%
- **Unique Values:** 3,148
- **Range:** 0.18 to 684.00
- **Mean:** 25.05
- **Median:** 14.26

#### `Haney Test N`
- **Data Type:** float64
- **Non-Null Count:** 14,803 (39.7% complete)
- **Missing:** 60.3%
- **Unique Values:** 7,407
- **Range:** -3.65 to 2364.30
- **Mean:** 58.04
- **Median:** 46.47

#### `Soil Health Score`
- **Data Type:** object
- **Non-Null Count:** 4,438 (11.9% complete)
- **Missing:** 88.1%
- **Unique Values:** 1,996
- **Sample Values:** 6.3, 6.9, 6.1, 5.2, 4.8

#### `Available P, lbs/A`
- **Data Type:** object
- **Non-Null Count:** 4,438 (11.9% complete)
- **Missing:** 88.1%
- **Unique Values:** 3,818
- **Sample Values:** 6.2, 7.0, 6.3, 6.8, 7.2

### Enzyme Activity

#### `Beta Glucosidase ppm pNP g-1 soil h-1`
- **Data Type:** float64
- **Non-Null Count:** 0 (0.0% complete)
- **Missing:** 100.0%
- **Unique Values:** 0

#### `Urease ppm NH4-N g-1 soil h-1`
- **Data Type:** float64
- **Non-Null Count:** 0 (0.0% complete)
- **Missing:** 100.0%
- **Unique Values:** 0

#### `Dehydrogenase ppm INTF g-1 soil h-1`
- **Data Type:** float64
- **Non-Null Count:** 0 (0.0% complete)
- **Missing:** 100.0%
- **Unique Values:** 0

#### `Fluorescein Diacetate Hydrolysis ppm fluorescein g-1 soil 3h-1`
- **Data Type:** float64
- **Non-Null Count:** 0 (0.0% complete)
- **Missing:** 100.0%
- **Unique Values:** 0

#### `Arylsulfatase ppm pNP g-1 soil h-1`
- **Data Type:** float64
- **Non-Null Count:** 0 (0.0% complete)
- **Missing:** 100.0%
- **Unique Values:** 0

#### `Enzyme Soil Moisture %`
- **Data Type:** float64
- **Non-Null Count:** 52 (0.1% complete)
- **Missing:** 99.9%
- **Unique Values:** 2
- **Range:** 0.00 to 6.00
- **Mean:** 2.77
- **Median:** 0.00

### Nutrient Recommendations

#### `P205 Rec 1`
- **Data Type:** object
- **Non-Null Count:** 2,583 (6.9% complete)
- **Missing:** 93.1%
- **Unique Values:** 50
- **Sample Values:** 0, 0.0, 25, 20, 35

#### `Lime Rec 1`
- **Data Type:** object
- **Non-Null Count:** 1,496 (4.0% complete)
- **Missing:** 96.0%
- **Unique Values:** 20
- **Sample Values:** 0.0, 0, 3.2, 2.4, 2.0

#### `P205 Rec 2`
- **Data Type:** object
- **Non-Null Count:** 926 (2.5% complete)
- **Missing:** 97.5%
- **Unique Values:** 42
- **Sample Values:** 0, 0.0, 40, 30, 20

#### `Lime Rec 2`
- **Data Type:** object
- **Non-Null Count:** 555 (1.5% complete)
- **Missing:** 98.5%
- **Unique Values:** 20
- **Sample Values:** 0.0, 0, 2.4, 3.2, 2.0

#### `P205 Rec 3`
- **Data Type:** object
- **Non-Null Count:** 98 (0.3% complete)
- **Missing:** 99.7%
- **Unique Values:** 25
- **Sample Values:** 0.0, 25, 0, 35.0, 30

#### `Lime Rec 3`
- **Data Type:** object
- **Non-Null Count:** 75 (0.2% complete)
- **Missing:** 99.8%
- **Unique Values:** 6
- **Sample Values:** 0.0, 0, 4, Lime Rec 3, 3.2

#### `Chloride Rec 1`
- **Data Type:** float64
- **Non-Null Count:** 0 (0.0% complete)
- **Missing:** 100.0%
- **Unique Values:** 0

#### `Chloride Rec 2`
- **Data Type:** float64
- **Non-Null Count:** 0 (0.0% complete)
- **Missing:** 100.0%
- **Unique Values:** 0

#### `Chloride Rec 3`
- **Data Type:** float64
- **Non-Null Count:** 0 (0.0% complete)
- **Missing:** 100.0%
- **Unique Values:** 0

### Economic Calculations

#### `Nutrient Value`
- **Data Type:** float64
- **Non-Null Count:** 14,863 (39.8% complete)
- **Missing:** 60.2%
- **Unique Values:** 10,967
- **Range:** -2.04 to 14681.37
- **Mean:** 164.80
- **Median:** 129.31

#### `Nutrient Value, $`
- **Data Type:** object
- **Non-Null Count:** 4,438 (11.9% complete)
- **Missing:** 88.1%
- **Unique Values:** 4,109
- **Sample Values:** 85.77, 123.03, 57.68, 104.6, 91.3

### Crop Information

#### `Past Crop`
- **Data Type:** object
- **Non-Null Count:** 2,596 (7.0% complete)
- **Missing:** 93.0%
- **Unique Values:** 18
- **Sample Values:** ALL OTHER CROPS, SOYBEANS, COVER CROP MIX, Soybeans, ALFALFA

#### `Crop 1`
- **Data Type:** object
- **Non-Null Count:** 2,590 (6.9% complete)
- **Missing:** 93.1%
- **Unique Values:** 104
- **Sample Values:** CORN BU/A, SOYBEANS BU/A, WHEAT BU/A, GARDEN, FEED HAY T/A

#### `YG 1`
- **Data Type:** object
- **Non-Null Count:** 2,585 (6.9% complete)
- **Missing:** 93.1%
- **Unique Values:** 140
- **Sample Values:** 3, 250, 60, 1, 50

#### `Crop 2`
- **Data Type:** object
- **Non-Null Count:** 928 (2.5% complete)
- **Missing:** 97.5%
- **Unique Values:** 55
- **Sample Values:** SOYBEANS BU/A, CORN BU/A, WHEAT BU/A, BARLEY, FEED BU/A, SOYBEAN BU/A

#### `YG 2`
- **Data Type:** object
- **Non-Null Count:** 928 (2.5% complete)
- **Missing:** 97.5%
- **Unique Values:** 96
- **Sample Values:** 60, 60.0, 200, 50, 40

#### `Crop 3`
- **Data Type:** object
- **Non-Null Count:** 98 (0.3% complete)
- **Missing:** 99.7%
- **Unique Values:** 10
- **Sample Values:** WHEAT BU/A, CORN BU/A, SOYBEANS BU/A, POPCORN LBS/A, RASPBERRY

#### `YG 3`
- **Data Type:** object
- **Non-Null Count:** 98 (0.3% complete)
- **Missing:** 99.7%
- **Unique Values:** 24
- **Sample Values:** 320.0, 80.0, 90.0, 80, 200

### Cover Crop Data

#### `Cover Crop Mix`
- **Data Type:** object
- **Non-Null Count:** 11,968 (32.1% complete)
- **Missing:** 67.9%
- **Unique Values:** 8
- **Sample Values:** 50% Legume 50% Grass, 40% Legume 60% Grass, 20% Legume 80% Grass, 30% Legume 70% Grass, 10% Legume 90% Grass

#### `Cover crop mix`
- **Data Type:** object
- **Non-Null Count:** 6,164 (16.5% complete)
- **Missing:** 83.5%
- **Unique Values:** 7
- **Sample Values:** 50% Legume 50% Grass, 40% Legume 60% Grass, 60% Legume 40% Grass, 20% Legume 80% Grass, 30% Legume 70% Grass

#### `Cover Crop mix`
- **Data Type:** object
- **Non-Null Count:** 2 (0.0% complete)
- **Missing:** 100.0%
- **Unique Values:** 1
- **Sample Values:** 50% Legume 50% Grass

### CEC & Base Saturation

#### `CEC, meq/100g`
- **Data Type:** float64
- **Non-Null Count:** 2 (0.0% complete)
- **Missing:** 100.0%
- **Unique Values:** 2
- **Range:** 11.70 to 12.40
- **Mean:** 12.05
- **Median:** 12.05

#### `Base Saturation, %`
- **Data Type:** float64
- **Non-Null Count:** 2 (0.0% complete)
- **Missing:** 100.0%
- **Unique Values:** 2
- **Range:** 56.00 to 61.00
- **Mean:** 58.50
- **Median:** 58.50

#### `Hydrogen, % Sat`
- **Data Type:** float64
- **Non-Null Count:** 2 (0.0% complete)
- **Missing:** 100.0%
- **Unique Values:** 2
- **Range:** 39.00 to 44.00
- **Mean:** 41.50
- **Median:** 41.50

#### `Sodium, % Sat`
- **Data Type:** float64
- **Non-Null Count:** 2 (0.0% complete)
- **Missing:** 100.0%
- **Unique Values:** 1
- **Range:** 1.00 to 1.00
- **Mean:** 1.00
- **Median:** 1.00

### Regenerative Metrics

#### `Regen Certified 6.8 or >`
- **Data Type:** object
- **Non-Null Count:** 35 (0.1% complete)
- **Missing:** 99.9%
- **Unique Values:** 3
- **Sample Values:** NOT YET, YES, Yes

#### `Regen Certified`
- **Data Type:** object
- **Non-Null Count:** 88 (0.2% complete)
- **Missing:** 99.8%
- **Unique Values:** 4
- **Sample Values:** Yes, YES, NOT YET, No

#### `Regen Score`
- **Data Type:** float64
- **Non-Null Count:** 107 (0.3% complete)
- **Missing:** 99.7%
- **Unique Values:** 60
- **Range:** 5.70 to 38.40
- **Mean:** 17.81
- **Median:** 16.90

#### `Regen verified`
- **Data Type:** object
- **Non-Null Count:** 46 (0.1% complete)
- **Missing:** 99.9%
- **Unique Values:** 2
- **Sample Values:** Yes, No

#### `MCC tons per acre`
- **Data Type:** float64
- **Non-Null Count:** 46 (0.1% complete)
- **Missing:** 99.9%
- **Unique Values:** 33
- **Range:** 1.80 to 10.30
- **Mean:** 4.84
- **Median:** 4.45

#### `Regen verify >6.8 to pass`
- **Data Type:** object
- **Non-Null Count:** 1 (0.0% complete)
- **Missing:** 100.0%
- **Unique Values:** 1
- **Sample Values:** Yes

#### `Regen score`
- **Data Type:** float64
- **Non-Null Count:** 1 (0.0% complete)
- **Missing:** 100.0%
- **Unique Values:** 1
- **Range:** 29.70 to 29.70
- **Mean:** 29.70
- **Median:** 29.70

#### `Regenerative Certified`
- **Data Type:** object
- **Non-Null Count:** 80 (0.2% complete)
- **Missing:** 99.8%
- **Unique Values:** 2
- **Sample Values:** YES, NOT YET

### Internal Tracking

#### `Beginning Depth`
- **Data Type:** object
- **Non-Null Count:** 19,429 (52.1% complete)
- **Missing:** 47.9%
- **Unique Values:** 17
- **Sample Values:** 0, 0.0, 6, 12, 8

#### `Ending Depth`
- **Data Type:** object
- **Non-Null Count:** 19,427 (52.1% complete)
- **Missing:** 47.9%
- **Unique Values:** 41
- **Sample Values:** 6, 8, 6.0, 8.0, 12

#### `_source_batch`
- **Data Type:** object
- **Non-Null Count:** 37,310 (100.0% complete)
- **Missing:** 0.0%
- **Unique Values:** 4
- **Sample Values:** Batch_4, Batch_2, Batch_3, Batch_1

#### `_source_file`
- **Data Type:** object
- **Non-Null Count:** 37,310 (100.0% complete)
- **Missing:** 0.0%
- **Unique Values:** 2,500
- **Sample Values:** Processed File (1353).csv, Processed File (5019).csv, Processed File (4863).csv, Processed File (4862).csv, Processed File (4264).csv

#### `Sample Type`
- **Data Type:** object
- **Non-Null Count:** 4,545 (12.2% complete)
- **Missing:** 87.8%
- **Unique Values:** 3
- **Sample Values:** SOIL, SOIL HEALTH, Cust ID

#### `Beginning Depth `
- **Data Type:** float64
- **Non-Null Count:** 2 (0.0% complete)
- **Missing:** 100.0%
- **Unique Values:** 1
- **Range:** 0.00 to 0.00
- **Mean:** 0.00
- **Median:** 0.00

#### `S-EC-1:1.03`
- **Data Type:** object
- **Non-Null Count:** 25 (0.1% complete)
- **Missing:** 99.9%
- **Unique Values:** 11
- **Sample Values:** 0.18, 0.19, 0.15, 0.2, 0.25

#### `S-CACO3-1NHCL.24`
- **Data Type:** object
- **Non-Null Count:** 25 (0.1% complete)
- **Missing:** 99.9%
- **Unique Values:** 2
- **Sample Values:** NONE, Excess Lime

#### `S-SOM-LOI.15`
- **Data Type:** object
- **Non-Null Count:** 25 (0.1% complete)
- **Missing:** 99.9%
- **Unique Values:** 11
- **Sample Values:** 3.1, 3.2, 3.5, 3.3, 3.4

---

## Data Quality Notes

### Missing Data Patterns
- **Enzyme Activity:** 100% missing across all samples (not measured)
- **Some Nutrient Recommendations:** High missingness (>99%) for Crop 2 and Crop 3
- **Core Soil Metrics:** Generally good coverage (>60% complete)
- **Haney Test Metrics:** Available for ~40% of samples

### Duplicate Records
- **Total Duplicates:** 17,055 (45.7% of dataset)
- **Unique Samples:** 20,255
- Note: Duplicates may represent repeat testing or data entry issues

### Data Types
- **Numeric:** 94 variables (soil measurements, calculations)
- **Text/Categorical:** 117 variables (identifiers, crop types, classifications)
- **Mixed Types:** Several columns have mixed data types due to data entry variations

### Batch Tracking
- Variables `_source_batch` and `_source_file` track data provenance
- Batch 1: 300 files (OneDrive_1_10-5-2025)
- Batch 2: 570 files (OneDrive_2_10-6-2025)
- Batch 3: 691 files (loose CSV files)
- Batch 4: 943 files (OneDrive_4_10-6-2025)

---

## Glossary of Terms

- **H3A:** Haney Test extraction method using H3A solution
- **WDRF:** Woodruff Buffer (pH buffering capacity)
- **LOI:** Loss on Ignition (organic matter measurement method)
- **MAC:** Microbially Active Carbon
- **CEC:** Cation Exchange Capacity
- **DTPA:** Diethylenetriaminepentaacetic acid (micronutrient extraction)
- **M3:** Mehlich-3 extraction method
- **NH4OAc:** Ammonium Acetate extraction
- **ppm:** Parts per million
- **lbs/A:** Pounds per acre
- **meq/100g:** Milliequivalents per 100 grams

---

**Document Generated:** October 6, 2025  
**By:** Claude Code  
**For:** Agricultural Soil Health EDA Project