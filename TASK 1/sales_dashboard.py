
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from pathlib import Path

# ==========================================
# SALES TREND VISUALIZATION - FINAL PROJECT
# ==========================================

# Create output folder
output_dir = Path("project_outputs")
output_dir.mkdir(exist_ok=True)

# Load cleaned dataset
df = pd.read_csv("cleaned_sales_data.csv")
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# Ensure numeric columns have correct types
numeric_columns = [
    "Sales_Amount", "Profit", "Cost", "Quantity"
]

for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df = df.dropna(subset=["Order_Date"] + numeric_columns)

# ==========================================
# 1. CALCULATE KEY PERFORMANCE INDICATORS
# ==========================================

total_revenue = df["Sales_Amount"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order_ID"].nunique()
total_units = df["Quantity"].sum()
average_order_value = total_revenue / total_orders if total_orders else 0

print("\n========== SALES PERFORMANCE ==========")
print(f"Total Revenue:       {total_revenue:,.2f}")
print(f"Total Profit:        {total_profit:,.2f}")
print(f"Total Orders:        {total_orders:,}")
print(f"Units Sold:          {total_units:,}")
print(f"Average Order Value: {average_order_value:,.2f}")

# ==========================================
# 2. MONTHLY SALES AND PROFIT ANALYSIS
# ==========================================

monthly = (
    df.set_index("Order_Date")
      .resample("MS")
      .agg(
          Total_Revenue=("Sales_Amount", "sum"),
          Total_Profit=("Profit", "sum"),
          Units_Sold=("Quantity", "sum"),
          Total_Orders=("Order_ID", "nunique")
      )
      .reset_index()
)

monthly["Revenue_Growth_Percent"] = (
    monthly["Total_Revenue"].pct_change() * 100
).round(2)

monthly.to_csv(
    output_dir / "monthly_sales_analysis.csv", index=False
)

# ==========================================
# 3. CATEGORY AND REGION ANALYSIS
# ==========================================

category = (
    df.groupby("Category")
      .agg(
          Total_Revenue=("Sales_Amount", "sum"),
          Total_Profit=("Profit", "sum"),
          Units_Sold=("Quantity", "sum")
      )
      .sort_values("Total_Revenue", ascending=False)
      .reset_index()
)

region = (
    df.groupby("Region")
      .agg(
          Total_Revenue=("Sales_Amount", "sum"),
          Total_Profit=("Profit", "sum"),
          Total_Orders=("Order_ID", "nunique")
      )
      .sort_values("Total_Revenue", ascending=False)
      .reset_index()
)

category.to_csv(
    output_dir / "category_analysis.csv", index=False
)
region.to_csv(
    output_dir / "region_analysis.csv", index=False
)

# ==========================================
# 4. SALES CHANNEL ANALYSIS
# ==========================================

channel = (
    df.groupby("Sales_Channel")["Sales_Amount"]
      .sum()
      .sort_values(ascending=False)
      .reset_index()
)

channel.columns = ["Sales_Channel", "Total_Revenue"]

channel.to_csv(
    output_dir / "channel_analysis.csv", index=False
)

# ==========================================
# 5. CREATE PROFESSIONAL DASHBOARD
# ==========================================

fig = plt.figure(figsize=(16, 11))
fig.patch.set_facecolor("#F3F6FA")

fig.suptitle(
    "SALES TREND ANALYTICS DASHBOARD",
    fontsize=22,
    fontweight="bold",
    color="#17365D",
    y=0.98
)

fig.text(
    0.5, 0.945,
    "Revenue | Profit | Product Categories | Regional Performance",
    ha="center", fontsize=11, color="#52657A"
)

# KPI cards
kpis = [
    ("TOTAL REVENUE", f"{total_revenue:,.0f}"),
    ("TOTAL PROFIT", f"{total_profit:,.0f}"),
    ("TOTAL ORDERS", f"{total_orders:,}"),
    ("UNITS SOLD", f"{total_units:,}")
]

card_positions = [0.055, 0.29, 0.525, 0.76]

for x, (label, value) in zip(card_positions, kpis):
    fig.text(
        x, 0.875, label,
        fontsize=10, color="#52657A",
        fontweight="bold",
        bbox=dict(
            boxstyle="round,pad=0.8",
            facecolor="white",
            edgecolor="#D9E2EF"
        )
    )
    fig.text(
        x, 0.825, value,
        fontsize=17, color="#17365D",
        fontweight="bold"
    )

# Four dashboard charts
gs = fig.add_gridspec(
    2, 2,
    left=0.08, right=0.96,
    bottom=0.09, top=0.75,
    hspace=0.40, wspace=0.28
)

# Chart 1: Monthly revenue trend
ax1 = fig.add_subplot(gs[0, 0])

ax1.plot(
    monthly["Order_Date"],
    monthly["Total_Revenue"],
    marker="o", linewidth=2.5,
    label="Revenue"
)

ax1.set_title("Monthly Revenue Trend", fontweight="bold")
ax1.set_xlabel("Month")
ax1.set_ylabel("Revenue")
ax1.xaxis.set_major_locator(mdates.MonthLocator(interval=3))
ax1.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
ax1.tick_params(axis="x", rotation=35)
ax1.grid(axis="y", linestyle="--", alpha=0.3)

# Chart 2: Category revenue
ax2 = fig.add_subplot(gs[0, 1])

ax2.barh(
    category["Category"],
    category["Total_Revenue"]
)

ax2.set_title("Revenue by Product Category", fontweight="bold")
ax2.set_xlabel("Revenue")
ax2.invert_yaxis()
ax2.grid(axis="x", linestyle="--", alpha=0.3)

# Chart 3: Regional revenue
ax3 = fig.add_subplot(gs[1, 0])

ax3.bar(
    region["Region"],
    region["Total_Revenue"]
)

ax3.set_title("Revenue by Region", fontweight="bold")
ax3.set_xlabel("Region")
ax3.set_ylabel("Revenue")
ax3.tick_params(axis="x", rotation=20)
ax3.grid(axis="y", linestyle="--", alpha=0.3)

# Chart 4: Monthly profit trend
ax4 = fig.add_subplot(gs[1, 1])

ax4.plot(
    monthly["Order_Date"],
    monthly["Total_Profit"],
    marker="o", linewidth=2.5,
    label="Profit"
)

ax4.set_title("Monthly Profit Trend", fontweight="bold")
ax4.set_xlabel("Month")
ax4.set_ylabel("Profit")
ax4.xaxis.set_major_locator(mdates.MonthLocator(interval=3))
ax4.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
ax4.tick_params(axis="x", rotation=35)
ax4.grid(axis="y", linestyle="--", alpha=0.3)

# Improve chart appearance
for ax in [ax1, ax2, ax3, ax4]:
    ax.set_facecolor("white")
    for spine in ax.spines.values():
        spine.set_color("#D9E2EF")

fig.savefig(
    output_dir / "sales_analytics_dashboard.png",
    dpi=300,
    bbox_inches="tight",
    facecolor=fig.get_facecolor()
)

plt.show()

# ==========================================
# 6. GENERATE BUSINESS INSIGHTS REPORT
# ==========================================

best_month = monthly.loc[monthly["Total_Revenue"].idxmax()]
lowest_month = monthly.loc[monthly["Total_Revenue"].idxmin()]
best_category = category.iloc[0]
best_region = region.iloc[0]
best_channel = channel.iloc[0]

report = f"""
SALES TREND VISUALIZATION - BUSINESS INSIGHTS
================================================

DATASET SUMMARY
Total records analyzed: {len(df)}
Date range: {df['Order_Date'].min().date()} to
            {df['Order_Date'].max().date()}

KEY PERFORMANCE INDICATORS
Total Revenue: {total_revenue:,.2f}
Total Profit: {total_profit:,.2f}
Total Orders: {total_orders:,}
Units Sold: {total_units:,}
Average Order Value: {average_order_value:,.2f}

MONTHLY PERFORMANCE
Highest revenue month: {best_month['Order_Date'].strftime('%B %Y')}
Revenue: {best_month['Total_Revenue']:,.2f}

Lowest revenue month: {lowest_month['Order_Date'].strftime('%B %Y')}
Revenue: {lowest_month['Total_Revenue']:,.2f}

CATEGORY PERFORMANCE
Top category: {best_category['Category']}
Revenue: {best_category['Total_Revenue']:,.2f}
Profit: {best_category['Total_Profit']:,.2f}

REGIONAL PERFORMANCE
Top region: {best_region['Region']}
Revenue: {best_region['Total_Revenue']:,.2f}

SALES CHANNEL PERFORMANCE
Top channel: {best_channel['Sales_Channel']}
Revenue: {best_channel['Total_Revenue']:,.2f}

BUSINESS RECOMMENDATIONS
1. Investigate high-performing months to identify possible
   seasonal patterns and repeat successful campaigns.
2. Evaluate category-level revenue and profit before
   deciding which products to promote.
3. Compare regional performance and investigate weaker
   regions for potential improvement opportunities.
4. Review sales channel performance to understand where
   revenue is concentrated.
5. Monitor monthly revenue and profit together rather
   than judging performance by revenue alone.

Note: This project uses synthetic practice data.
Findings describe this dataset, not a real company.
"""

report_path = output_dir / "business_insights_report.txt"
report_path.write_text(report, encoding="utf-8")

print("\n========== TOP CATEGORIES ==========")
print(category.head(3).to_string(index=False))

print("\n========== TOP REGIONS ==========")
print(region.head(3).to_string(index=False))

print("\n========== BUSINESS INSIGHTS ==========")
print(report)

print("\nPROJECT COMPLETED SUCCESSFULLY!")
print(f"Check your output files in: {output_dir.resolve()}")
