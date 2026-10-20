
import pandas as pd

# Load the sales dataset
df = pd.read_csv("sales_trend_dataset.csv")

# Display the first five records
print("FIRST FIVE RECORDS:")
print(df.head())

# Display the number of rows and columns
print("\nDATASET SHAPE:")
print(df.shape)

# Display column names
print("\nCOLUMN NAMES:")
print(df.columns.tolist())

# Check data types
print("\nDATA TYPES:")
print(df.dtypes)

# Check missing values
print("\nMISSING VALUES:")
print(df.isnull().sum())

# Check duplicate records
print("\nDUPLICATE ROWS:")
print(df.duplicated().sum())

# Display summary statistics
print("\nSUMMARY STATISTICS:")
print(df.describe())
