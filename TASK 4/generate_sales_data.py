
import pandas as pd
import random

random.seed(42)

dates = pd.date_range(
    start="2023-01-01",
    end="2025-12-01",
    freq="MS"
)

sales = []

for i, date in enumerate(dates):
    trend = 20000 + i * 500
    seasonal = 3000 * __import__("math").sin(
        2 * __import__("math").pi * date.month / 12
    )
    noise = random.randint(-2000, 2000)

    sales.append({
        "Date": date,
        "Sales": round(trend + seasonal + noise, 2)
    })

df = pd.DataFrame(sales)
df.to_csv("sales_forecast_data.csv", index=False)

print("Sales dataset created successfully!")
print("Total records:", len(df))
print(df.head())
