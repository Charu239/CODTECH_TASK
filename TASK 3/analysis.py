
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load dataset
df = pd.read_csv("customer_feedback.csv")

print("First 5 Customer Reviews:")
print(df.head())

# Step 2: Analyze customer feedback
print("\nRating Distribution:")
print(df["Rating"].value_counts().sort_index())

print("\nSentiment Distribution:")
print(df["Sentiment"].value_counts())

print("\nAverage Rating by Product:")
print(df.groupby("Product")["Rating"].mean().round(2))

print("\nSentiment by Product:")
print(pd.crosstab(df["Product"], df["Sentiment"]))

# Step 3: Create charts
df["Sentiment"].value_counts().plot(
    kind="bar", title="Customer Sentiment Distribution"
)
plt.xlabel("Sentiment")
plt.ylabel("Number of Reviews")
plt.tight_layout()
plt.savefig("sentiment_chart.png")
plt.show()

df.groupby("Product")["Rating"].mean().plot(
    kind="bar", title="Average Rating by Product"
)
plt.xlabel("Product")
plt.ylabel("Average Rating")
plt.ylim(0, 5)
plt.tight_layout()
plt.savefig("product_rating_chart.png")
plt.show()

# Step 4: Save sentiment summary
sentiment_summary = df["Sentiment"].value_counts().reset_index()
sentiment_summary.columns = ["Sentiment", "Number_of_Reviews"]
sentiment_summary.to_csv("sentiment_summary.csv", index=False)

# Step 5: Save product summary
product_summary = df.groupby("Product").agg(
    Total_Reviews=("Customer_ID", "count"),
    Average_Rating=("Rating", "mean")
).round(2)

product_summary.to_csv("product_summary.csv")

# Step 6: Generate report
with open("customer_feedback_report.txt", "w") as file:
    file.write("CUSTOMER FEEDBACK SENTIMENT ANALYSIS\n")
    file.write("=" * 40 + "\n\n")
    file.write(f"Total Reviews: {len(df)}\n")
    file.write(f"Average Rating: {df['Rating'].mean():.2f}/5\n")
    file.write(
        f"Positive Reviews: {(df['Sentiment'] == 'Positive').sum()}\n"
    )
    file.write(
        f"Negative Reviews: {(df['Sentiment'] == 'Negative').sum()}\n"
    )
    file.write(
        f"Neutral Reviews: {(df['Sentiment'] == 'Neutral').sum()}\n\n"
    )
    file.write("PRODUCT-WISE ANALYSIS\n")
    file.write(product_summary.to_string())

print("\nProject completed successfully!")
print("Analysis files, charts, and report have been saved.")

