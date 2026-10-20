
import pandas as pd

# Load the cleaned dataset
df = pd.read_csv("cleaned_sales_data.csv")

# Convert Order_Date into datetime format
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# Create a monthly period column
df["Month"] = df["Order_Date"].dt.to_period("M")

# Calculate monthly sales trends
monthly_sales = df.groupby("Month").agg(
    Total_Revenue=("Sales_Amount", "sum"),
    Total_Profit=("Profit", "sum"),
    Units_Sold=("Quantity", "sum"),
    Total_Orders=("Order_ID", "nunique")
).reset_index()

# Calculate month-over-month revenue growth
monthly_sales["Revenue_Growth_Percent"] = (
    monthly_sales["Total_Revenue"].pct_change() * 100
).round(2)

# Round financial values
monthly_sales["Total_Revenue"] = monthly_sales["Total_Revenue"].round(2)
monthly_sales["Total_Profit"] = monthly_sales["Total_Profit"].round(2)

# Display the results
print("MONTHLY SALES TREND")
print(monthly_sales.to_string(index=False))

# Identify the highest and lowest revenue months
highest_month = monthly_sales.loc[
    monthly_sales["Total_Revenue"].idxmax()
]

lowest_month = monthly_sales.loc[
    monthly_sales["Total_Revenue"].idxmin()
]

print("\nHIGHEST REVENUE MONTH")
print(highest_month.to_string())

print("\nLOWEST REVENUE MONTH")
print(lowest_month.to_string())

# Save the monthly analysis
monthly_sales.to_csv("monthly_sales_trends.csv", index=False)

print("\nMonthly analysis saved to monthly_sales_trends.csv")
