# CODTECH IT Solutions Internship

## Task 4: Predictive Sales Forecasting Using Python

### Internship Details

- **Intern Name:** Charu
- **Intern ID:** CITS9187
- **Organization:** CODTECH IT Solutions
- **Internship Duration:** 4 Weeks
- **Task Number:** Task 4
- **Project Name:** Predictive Sales Forecasting

---

## 1. Project Overview

Predictive Sales Forecasting is a data analytics and machine learning project developed using Python. The project uses historical sales data to identify trends and predict future sales.

A synthetic monthly sales dataset covering January 2023 to December 2025 was generated for this project. Linear Regression is used to learn the relationship between time and sales, then forecast sales for the next six months.

## 2. Project Scope

The scope of this project includes:

- Generating a monthly sales dataset containing 36 records.
- Loading and inspecting sales data using Pandas.
- Preparing time-based features for forecasting.
- Training a Linear Regression model using Scikit-learn.
- Predicting sales for the next six months.
- Evaluating the model using Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE).
- Visualizing historical sales and predicted sales using Matplotlib.
- Saving forecast results and a project report.

## 3. Project Objectives

- Understand historical sales trends.
- Learn the basic process of building a predictive model.
- Forecast future sales from historical data.
- Evaluate model fit using standard error metrics.
- Present forecast results through charts and reports.
- Gain practical experience with machine learning in Python.

## 4. Tools and Technologies

- **Programming Language:** Python
- **Libraries:** Pandas, NumPy, Matplotlib, Scikit-learn
- **Machine Learning Algorithm:** Linear Regression
- **Dataset Format:** CSV
- **Development Environment:** Python IDE or Visual Studio Code

## 5. Dataset Description

The project uses a synthetic monthly sales dataset containing 36 records with two main columns:

- `Date` — Month of the recorded sales.
- `Sales` — Sales value for that month.

The data covers January 2023 through December 2025 and includes an upward trend, seasonal variation, and random fluctuations.

## 6. Project Workflow

1. Generate the monthly sales dataset.
2. Load the dataset using Pandas.
3. Convert dates into a usable format.
4. Create a numerical time-based feature.
5. Train a Linear Regression model.
6. Forecast sales for the next six months.
7. Evaluate model fit using MAE and RMSE.
8. Plot historical and predicted sales.
9. Export forecast results and a text report.

## 7. Model Evaluation

The project calculates two evaluation metrics:

- **Mean Absolute Error (MAE):** Measures the average absolute difference between actual and predicted sales.
- **Root Mean Squared Error (RMSE):** Measures prediction errors while giving greater weight to larger errors.

In the current implementation, these metrics are calculated on the same historical data used to train the model. They measure how well the model fits the training data and do not provide a reliable estimate of future forecasting accuracy. A time-based holdout test would provide a stronger evaluation.

## 8. Project Output Files

- `generate_sales_data.py` — Generates the monthly sales dataset.
- `sales_forecast_data.csv` — Historical synthetic sales data.
- `task4_sales_forecast.py` — Trains the model, forecasts sales, evaluates fit, and creates outputs.
- `sales_forecast_results.csv` — Predicted sales for the next six months.
- `sales_forecast_chart.png` — Chart of historical and predicted sales.
- `sales_forecast_report.txt` — Forecast results and evaluation metrics.

## 9. Learning Outcomes

Through this project, I gained practical experience in:

- Preparing time-based data for analysis.
- Using Pandas to process sales datasets.
- Training a Linear Regression model.
- Generating future sales predictions.
- Calculating MAE and RMSE.
- Visualizing sales trends using Matplotlib.
- Saving forecasts and analytical reports.

## 10. Conclusion

This project demonstrates a basic approach to predictive sales forecasting using Python and Linear Regression. It combines data preparation, model training, prediction, evaluation, and visualization in one workflow.

The dataset is synthetic, and the forecast is intended for educational purposes. Real business forecasting would require actual sales data, stronger validation, and consideration of seasonal and other business factors.

---

**Organization:** CODTECH IT Solutions  
**Intern Name:** Charu  
**Intern ID:** CITS9187  
**Internship Duration:** 4 Weeks  
**Project Name:** Predictive Sales Forecasting Using Python
