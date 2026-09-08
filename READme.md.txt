# Demand Forecasting with Machine Learning

## Overview

This project develops and evaluates machine learning models for weekly demand forecasting of a product. The objective is to investigate whether machine learning can improve demand forecasts compared with traditional baseline forecasting methods.

The project follows an end-to-end forecasting workflow, including data preprocessing, exploratory analysis, feature engineering, baseline forecasting, machine learning, model evaluation, feature importance analysis and forecast error analysis.

The final Random Forest model achieved a **MAE of 17.77** and a **MAPE of 8.95%**, representing a **31.9% improvement in MAE compared with the naive forecasting baseline**.

---

## Business Problem

Accurate demand forecasts are important for supply chain planning. Forecasting demand can support decisions related to:

- Inventory planning
- Capacity planning
- Procurement
- Production planning
- Resource allocation
- Promotion planning

The goal of this project was to build a forecasting model capable of predicting weekly demand while investigating which variables contribute most to forecast accuracy.

---

## Dataset

The dataset contains weekly demand observations for multiple products together with additional explanatory variables.

For this project, **Product_001** was selected for analysis.

The dataset contains:

- Date
- Product
- Demand
- Price
- Promotion

The selected product contains approximately two years of weekly observations.

The data was sorted chronologically and divided into training and test periods using a time-based split to avoid using future observations when training the models.

### Train/Test Split

**Training period:**
January 2024 – August 2025

**Test period:**
August 2025 – December 2025

---

## Methodology

The project was developed in several stages.

### 1. Data Preparation

The dataset was:

- Loaded using pandas
- Converted to a datetime format
- Sorted chronologically
- Filtered to Product_001
- Split into training and test periods

A chronological split was used instead of a random train/test split because demand forecasting is a time-series problem.

---

### 2. Baseline Forecasting

Three traditional forecasting approaches were evaluated:

#### Naive Forecast

The previous week's demand was used as the forecast.

#### Moving Average

A four-week moving average was used to predict future demand.

#### Exponential Moving Average

An exponential moving average with a span of four weeks was used.

These models provide simple benchmarks against which the machine learning models can be compared.

---

## 3. Feature Engineering

Several time-series features were created to provide the machine learning model with information about historical demand and seasonality.

### Lag Features

Historical demand was incorporated using:

- Lag 1
- Lag 2
- Lag 3
- Lag 4
- Lag 5
- Lag 8

These features represent demand from previous weeks.

### Rolling Features

Rolling averages were created using:

- Four-week rolling mean
- Eight-week rolling mean

The rolling averages were shifted to ensure that future demand information was not used when predicting the current observation.

### Seasonal Feature

The ISO calendar week was included as the `Week` feature to capture recurring seasonal patterns throughout the year.

### Demand Change

A one-week demand change variable was also created:

`Demand_Change_1`

### Other Variables

The model also included:

- Price
- Promotion

---

## 4. Random Forest Models

Three Random Forest models were developed incrementally.

### Random Forest v1

The first model used historical demand, rolling demand, price and promotion features.

### Random Forest v2

The `Week` feature was added to capture seasonal effects.

### Random Forest v3

The final model included additional lag variables, an eight-week rolling average and demand change.

The final model used:

- Lag_1
- Lag_2
- Lag_3
- Lag_4
- Lag_5
- Lag_8
- Rolling_Mean_4
- Rolling_Mean_8
- Price
- Promotion
- Week
- Demand_Change_1

The final Random Forest consisted of **300 trees**.

---

# Results

## Model Comparison

| Model | Test MAE |
|---|---:|
| Naive Forecast | 26.10 |
| Moving Average (4 weeks) | 22.68 |
| EMA (4 weeks) | 22.03 |
| Random Forest v1 | 20.83 |
| Random Forest v2 | 18.98 |
| **Random Forest v3** | **17.77** |

The final Random Forest v3 model achieved the lowest test MAE.

Compared with the naive forecast:

**MAE improvement: 31.9%**

---

## Final Model Performance

| Metric | Result |
|---|---:|
| MAE | **17.77** |
| RMSE | **21.97** |
| MAPE | **8.95%** |
| Bias | **+5.41** |
| Average Actual Demand | **193.95** |
| Average Forecast | **188.54** |

The model's average forecast was approximately 5.4 units below the average actual demand, indicating a moderate tendency to under-forecast.

---

## Feature Importance

The Random Forest feature importance analysis showed the following ranking:

| Feature | Importance |
|---|---:|
| Promotion | 22.77% |
| Week | 19.27% |
| Rolling_Mean_4 | 11.36% |
| Lag_1 | 8.24% |
| Lag_8 | 8.22% |
| Rolling_Mean_8 | 7.03% |
| Lag_2 | 5.05% |
| Lag_3 | 4.47% |
| Lag_5 | 4.45% |
| Lag_4 | 4.06% |
| Demand_Change_1 | 3.04% |
| Price | 2.04% |

Promotion and Week were the two most important features in the final model.

The importance scores describe how heavily the Random Forest relies on each variable for prediction. They should not be interpreted as causal effects.

---

## Error Analysis

Forecast errors were analyzed to understand when the model struggled.

The largest errors included:

| Date | Actual | Forecast | Error |
|---|---:|---:|---:|
| 2025-11-30 | 235 | 187.57 | +47.43 |
| 2025-11-23 | 226 | 183.22 | +42.78 |
| 2025-08-31 | 251 | 214.39 | +36.61 |
| 2025-12-07 | 221 | 194.82 | +26.18 |
| 2025-09-28 | 156 | 181.46 | -25.46 |

The analysis indicates that the model generally captures the overall demand level but has more difficulty when demand changes rapidly or deviates substantially from recent historical patterns.

Only one observation in the test period was marked as a promotion week, so the available test data is insufficient to draw conclusions about whether promotions systematically increase forecast error.

---

## Actual vs Forecast

The final model was evaluated by comparing predicted demand with actual demand throughout the test period.

The forecast generally follows the overall demand pattern, while larger differences occur during sudden demand spikes and drops.

---

## Business Interpretation

The results indicate that machine learning can improve demand forecasting compared with simple historical forecasting approaches for the product examined.

The improvement from a MAE of **26.10 to 17.77** means that the average absolute forecasting error was reduced by approximately **32%** compared with the naive benchmark.

From a supply chain perspective, a more accurate demand forecast can potentially support better:

- Inventory decisions
- Procurement planning
- Production planning
- Capacity allocation
- Resource planning

However, the positive bias of **5.41 units** indicates that the model tends to underestimate demand slightly. In an operational environment, systematic under-forecasting could increase the risk of insufficient inventory or capacity.

---

## Limitations

Several limitations should be considered when interpreting the results.

### Limited Dataset

The analysis focuses on a single product with approximately two years of weekly observations. A larger dataset containing more products and historical periods would provide a stronger basis for model evaluation.

### Limited Promotion Observations

There was only one promotion observation in the test period. Therefore, the importance assigned to promotion should be interpreted carefully.

### Sudden Demand Changes

The model struggles with unexpected demand fluctuations. Additional explanatory variables could potentially help explain these changes.

### Random Forest

Random Forest is effective at learning relationships within the available data but may have limitations when forecasting demand patterns that differ substantially from those observed during training.

---

## Future Improvements

Potential future improvements include:

- Testing additional products
- Increasing the historical dataset
- Adding more external variables
- Incorporating holidays and calendar events
- Creating improved seasonal features
- Hyperparameter optimization
- Cross-validation designed specifically for time series
- Comparing Random Forest with gradient boosting models
- Testing models such as XGBoost or LightGBM
- Evaluating the forecast at different planning horizons
- Translating forecast errors into inventory and financial costs

---

## Technologies

The project was developed using Python.

### Python Libraries

- **Pandas** – data manipulation and preprocessing
- **NumPy** – numerical calculations
- **Matplotlib** – data visualization
- **Scikit-learn** – machine learning and model evaluation

### Machine Learning

- Random Forest Regression
- Time-series feature engineering
- Model evaluation using MAE, RMSE and MAPE

---

## Project Structure

```text
Demand_Forecasting/
│
├── dataset/
│   └── raw/
│       └── demand_data.csv
│
├── notebooks/
│   └── demand_forecasting.ipynb
│
├── src/
│   └── forecasting.py
│
├── outputs/
│   ├── actual_vs_forecast.png
│   └── model_results.csv
│
└── README.md