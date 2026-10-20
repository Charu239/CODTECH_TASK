
import pandas as pd

# Load the original dataset
df = pd.read_csv("sales_trend_dataset.csv")

# 1. Check missing values
print("Missing values before cleaning:")
print(df.isnull().sum())

# 2. Remove duplicate rows
df = df.drop_duplicates()

# 3. Convert Order_Date to datetime format
df["Order_Date"] = pd.to_datetime(
    df["Order_Date"], errors="coerce"
)

# 4. Remove rows with missing essential values
df = df.dropna(subset=[
    "Order_ID",
    "Order_Date",
    "Product",
    "Category",
    "Sales_Amount"
])

# 5. Correct numeric data types
numeric_columns = [
    "Quantity",
    "Unit_Price",
    "Discount_Percent",
    "Sales_Amount",
    "Cost",
    "Profit"
]

for column in numeric_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")

# Remove rows with invalid essential numeric values
df = df.dropna(subset=numeric_columns)

# 6. Sort records by order date
df = df.sort_values("Order_Date")

# 7. Save the cleaned dataset
df.to_csv("cleaned_sales_data.csv", index=False)

# 8. Verify the cleaned data
print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("\nDuplicate rows after cleaning:")
print(df.duplicated().sum())

print("\nCleaned dataset shape:")
print(df.shape)

print("\nOrder date data type:")
print(df["Order_Date"].dtype)

print("\nCleaned dataset saved successfully!")
