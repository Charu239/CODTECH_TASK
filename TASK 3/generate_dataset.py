
import pandas as pd
import random
from datetime import date, timedelta

random.seed(42)

positive_reviews = [
    "Excellent product, very satisfied!",
    "Amazing quality and fast delivery.",
    "Good value for money.",
    "I love this product.",
    "Great experience, highly recommended.",
    "Works perfectly and looks great."
]

negative_reviews = [
    "Very poor quality and disappointing.",
    "Delivery was late and packaging was damaged.",
    "Not worth the money.",
    "The product stopped working quickly.",
    "Very bad experience, not recommended.",
    "Poor customer service."
]

neutral_reviews = [
    "The product is okay.",
    "Average quality for the price.",
    "It works as expected.",
    "Delivery was on time.",
    "Nothing special about this product.",
    "An ordinary purchase."
]

products = ["Electronics", "Clothing", "Home", "Beauty", "Sports"]
data = []

for i in range(1, 1001):
    rating = random.randint(1, 5)

    if rating >= 4:
        sentiment = "Positive"
        review = random.choice(positive_reviews)
    elif rating <= 2:
        sentiment = "Negative"
        review = random.choice(negative_reviews)
    else:
        sentiment = "Neutral"
        review = random.choice(neutral_reviews)

    review_date = date(2025, 1, 1) + timedelta(
        days=random.randint(0, 364)
    )

    data.append([
        i,
        random.choice(products),
        rating,
        review,
        review_date,
        sentiment
    ])

df = pd.DataFrame(data, columns=[
    "Customer_ID", "Product", "Rating",
    "Review_Text", "Review_Date", "Sentiment"
])

df.to_csv("customer_feedback.csv", index=False)

print("Dataset created successfully!")
print("Total reviews:", len(df))
print(df.head())
