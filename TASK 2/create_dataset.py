
import pandas as pd
import numpy as np

np.random.seed(42)
n = 1000

departments = [
    "Sales", "Marketing", "IT", "HR",
    "Finance", "Operations", "Customer Support"
]

df = pd.DataFrame({
    "Employee_ID": [f"EMP{i:04d}" for i in range(1, n + 1)],
    "Department": np.random.choice(departments, n),
    "Experience_Years": np.random.randint(0, 21, n),
    "Work_Hours_Per_Week": np.random.randint(25, 61, n),
    "Attendance_Rate": np.round(np.random.uniform(70, 100, n), 1),
    "Tasks_Assigned": np.random.randint(20, 81, n),
    "Overtime_Hours": np.random.randint(0, 16, n),
    "Training_Hours": np.random.randint(0, 21, n)
})

# Generate tasks completed based on assigned tasks
df["Tasks_Completed"] = [
    np.random.randint(int(tasks * 0.50), tasks + 1)
    for tasks in df["Tasks_Assigned"]
]

# Calculate productivity score
df["Productivity_Score"] = np.round(
    (
        df["Tasks_Completed"] / df["Tasks_Assigned"] * 60
        + df["Attendance_Rate"] * 0.25
        + df["Experience_Years"] * 0.5
    ).clip(0, 100),
    1
)

df["Performance_Rating"] = pd.cut(
    df["Productivity_Score"],
    bins=[0, 40, 55, 70, 85, 100],
    labels=[1, 2, 3, 4, 5],
    include_lowest=True
).astype(int)

df.to_csv("employee_productivity_dataset.csv", index=False)

print("Dataset created successfully!")
print("Rows and columns:", df.shape)
print(df.head())
