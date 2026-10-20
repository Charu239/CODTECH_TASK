
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

# 1. Load the dataset
df = pd.read_csv("sales_forecast_data.csv")
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date").reset_index(drop=True)

print("Dataset loaded successfully!")
print(df.head())

# 2. Prepare data for forecasting
df["Month_Number"] = range(len(df))

X = df[["Month_Number"]]
y = df["Sales"]

# 3. Train the Linear Regression model
model = LinearRegression()
model.fit(X, y)

print("\nModel trained successfully!")

# 4. Evaluate the model on historical data
historical_predictions = model.predict(X)

mae = mean_absolute_error(y, historical_predictions)
rmse = np.sqrt(mean_squared_error(y, historical_predictions))

print("\nModel Evaluation:")
print("MAE:", round(mae, 2))
print("RMSE:", round(rmse, 2))

# 5. Forecast the next 6 months
future_dates = pd.date_range(
    start=df["Date"].max() + pd.DateOffset(months=1),
    periods=6,
    freq="MS"
)

future_X = pd.DataFrame({
    "Month_Number": range(len(df), len(df) + 6)
})

predictions = model.predict(future_X)

forecast = pd.DataFrame({
    "Date": future_dates,
    "Predicted_Sales": predictions.round(2)
})

print("\nSales Forecast for the Next 6 Months:")
print(forecast.to_string(index=False))

# 6. Save forecast results
forecast.to_csv("sales_forecast_results.csv", index=False)

# 7. Create and save the forecast chart
plt.figure(figsize=(10, 5))

plt.plot(
    df["Date"], df["Sales"],
    marker="o", label="Historical Sales"
)

plt.plot(
    forecast["Date"], forecast["Predicted_Sales"],
    marker="o", linestyle="--", label="Predicted Sales"
)

plt.title("Predictive Sales Forecast - Next 6 Months")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("sales_forecast_chart.png")
plt.show()

# 8. Generate the project report
with open("sales_forecast_report.txt", "w") as file:
    file.write("PREDICTIVE SALES FORECASTING REPORT\n")
    file.write("=" * 40 + "\n\n")

    file.write(f"Historical Records: {len(df)}\n")
    file.write("Forecast Period: Next 6 Months\n")
    file.write("Model: Linear Regression\n")
    file.write(f"MAE: {mae:.2f}\n")
    file.write(f"RMSE: {rmse:.2f}\n\n")

    file.write("PREDICTED SALES\n")
    file.write(forecast.to_string(index=False))

print("\nProject completed successfully!")
print("Files created:")
print("1. sales_forecast_results.csv")
print("2. sales_forecast_chart.png")
print("3. sales_forecast_report.txt")
