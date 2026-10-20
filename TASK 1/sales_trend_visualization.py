
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Load cleaned sales data
df = pd.read_csv("cleaned_sales_data.csv")

# Convert order dates
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# Group sales by month
monthly_sales = (
    df.set_index("Order_Date")
      .resample("MS")["Sales_Amount"]
      .sum()
      .reset_index()
)

# Create the line chart
plt.figure(figsize=(12, 6))

plt.plot(
    monthly_sales["Order_Date"],
    monthly_sales["Sales_Amount"],
    marker="o",
    linewidth=2.5,
    label="Monthly Revenue"
)

# Add chart title and labels
plt.title("Monthly Sales Trend (2025–2026)", fontsize=16, pad=15)
plt.xlabel("Month", fontsize=12)
plt.ylabel("Revenue", fontsize=12)

# Format the x-axis
ax = plt.gca()
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=2))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))

plt.xticks(rotation=45)
plt.grid(True, linestyle="--", alpha=0.4)
plt.legend()
plt.tight_layout()

# Save the chart
plt.savefig("monthly_sales_trend.png", dpi=300, bbox_inches="tight")

# Display the chart
plt.show()

print("Sales trend chart saved successfully!")
