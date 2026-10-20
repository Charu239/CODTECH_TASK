
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# =====================================
# EMPLOYEE PRODUCTIVITY STUDY
# =====================================

# Create output folder
output = Path("employee_productivity_outputs")
output.mkdir(exist_ok=True)

# Load dataset
df = pd.read_csv("employee_productivity_dataset.csv")

print("DATASET OVERVIEW")
print("Shape:", df.shape)
print("\nFirst five records:")
print(df.head())

# =====================================
# 1. DATA QUALITY CHECKS
# =====================================

print("\nMISSING VALUES")
print(df.isnull().sum())

print("\nDUPLICATE ROWS:", df.duplicated().sum())

# Remove duplicate records
df = df.drop_duplicates()

# Convert numeric columns
numeric_cols = [
    "Experience_Years",
    "Work_Hours_Per_Week",
    "Attendance_Rate",
    "Tasks_Assigned",
    "Tasks_Completed",
    "Overtime_Hours",
    "Training_Hours",
    "Productivity_Score",
    "Performance_Rating"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df = df.dropna(
    subset=["Employee_ID", "Department"] + numeric_cols
)

# Save cleaned data
df.to_csv(output / "cleaned_employee_data.csv", index=False)

# =====================================
# 2. KEY PERFORMANCE INDICATORS
# =====================================

total_employees = df["Employee_ID"].nunique()
avg_productivity = df["Productivity_Score"].mean()
avg_attendance = df["Attendance_Rate"].mean()
avg_work_hours = df["Work_Hours_Per_Week"].mean()
total_tasks_completed = df["Tasks_Completed"].sum()

print("\nKEY METRICS")
print(f"Total Employees: {total_employees}")
print(f"Average Productivity: {avg_productivity:.2f}/100")
print(f"Average Attendance: {avg_attendance:.2f}%")
print(f"Average Weekly Work Hours: {avg_work_hours:.2f}")
print(f"Total Tasks Completed: {total_tasks_completed:,}")

# =====================================
# 3. DEPARTMENT ANALYSIS
# =====================================

department_summary = df.groupby("Department").agg(
    Employee_Count=("Employee_ID", "nunique"),
    Average_Productivity=("Productivity_Score", "mean"),
    Average_Attendance=("Attendance_Rate", "mean"),
    Average_Work_Hours=("Work_Hours_Per_Week", "mean"),
    Total_Tasks_Completed=("Tasks_Completed", "sum")
).round(2).reset_index()

department_summary = department_summary.sort_values(
    "Average_Productivity", ascending=False
)

department_summary.to_csv(
    output / "department_productivity_summary.csv",
    index=False
)

print("\nDEPARTMENT PRODUCTIVITY")
print(department_summary.to_string(index=False))

# =====================================
# 4. RELATIONSHIP ANALYSIS
# =====================================

correlations = df[
    [
        "Productivity_Score",
        "Attendance_Rate",
        "Work_Hours_Per_Week",
        "Experience_Years",
        "Overtime_Hours",
        "Training_Hours",
        "Tasks_Completed"
    ]
].corr()

correlations.to_csv(output / "correlation_analysis.csv")

print("\nCORRELATION WITH PRODUCTIVITY")
print(
    correlations["Productivity_Score"]
    .sort_values(ascending=False)
    .round(3)
)

# =====================================
# 5. VISUALIZATIONS
# =====================================

# Chart 1: Average productivity by department
plt.figure(figsize=(10, 6))
plt.barh(
    department_summary["Department"],
    department_summary["Average_Productivity"]
)
plt.title("Average Productivity by Department")
plt.xlabel("Average Productivity Score")
plt.ylabel("Department")
plt.gca().invert_yaxis()
plt.grid(axis="x", linestyle="--", alpha=0.3)
plt.tight_layout()
plt.savefig(output / "productivity_by_department.png", dpi=300)
plt.close()

# Chart 2: Attendance vs productivity
plt.figure(figsize=(8, 6))
plt.scatter(
    df["Attendance_Rate"],
    df["Productivity_Score"],
    alpha=0.5
)
plt.title("Attendance Rate vs Productivity")
plt.xlabel("Attendance Rate (%)")
plt.ylabel("Productivity Score")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig(output / "attendance_vs_productivity.png", dpi=300)
plt.close()

# Chart 3: Work hours vs productivity
plt.figure(figsize=(8, 6))
plt.scatter(
    df["Work_Hours_Per_Week"],
    df["Productivity_Score"],
    alpha=0.5
)
plt.title("Weekly Work Hours vs Productivity")
plt.xlabel("Work Hours Per Week")
plt.ylabel("Productivity Score")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig(output / "work_hours_vs_productivity.png", dpi=300)
plt.close()

# Chart 4: Tasks completed by department
tasks_by_department = (
    df.groupby("Department")["Tasks_Completed"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))
plt.bar(
    tasks_by_department.index,
    tasks_by_department.values
)
plt.title("Total Tasks Completed by Department")
plt.xlabel("Department")
plt.ylabel("Tasks Completed")
plt.xticks(rotation=35, ha="right")
plt.grid(axis="y", linestyle="--", alpha=0.3)
plt.tight_layout()
plt.savefig(output / "tasks_by_department.png", dpi=300)
plt.close()

# =====================================
# 6. BUSINESS INSIGHTS REPORT
# =====================================

best_department = department_summary.iloc[0]
lowest_department = department_summary.iloc[-1]

attendance_corr = correlations.loc[
    "Attendance_Rate", "Productivity_Score"
]
hours_corr = correlations.loc[
    "Work_Hours_Per_Week", "Productivity_Score"
]
experience_corr = correlations.loc[
    "Experience_Years", "Productivity_Score"
]

report = f"""
EMPLOYEE PRODUCTIVITY STUDY
===========================

PROJECT SUMMARY
This project analyzes a synthetic dataset of employee
work patterns and productivity using Python and Pandas.

KEY METRICS
-----------
Employees analyzed: {total_employees}
Average productivity score: {avg_productivity:.2f}/100
Average attendance: {avg_attendance:.2f}%
Average weekly work hours: {avg_work_hours:.2f}
Total tasks completed: {total_tasks_completed:,}

DEPARTMENT FINDINGS
-------------------
Highest average productivity:
{best_department['Department']} -
{best_department['Average_Productivity']:.2f}/100

Lowest average productivity:
{lowest_department['Department']} -
{lowest_department['Average_Productivity']:.2f}/100

CORRELATION RESULTS
-------------------
Attendance vs productivity: {attendance_corr:.3f}
Work hours vs productivity: {hours_corr:.3f}
Experience vs productivity: {experience_corr:.3f}

BUSINESS RECOMMENDATIONS
------------------------
1. Compare productivity and workload across departments.
2. Review attendance patterns alongside other factors,
   without assuming attendance alone determines output.
3. Monitor overtime and workload to identify possible
   risks of excessive work.
4. Evaluate training opportunities using broader evidence.
5. Use these results for exploration, not as the sole
   basis for decisions about individual employees.

LIMITATIONS
-----------
The dataset is synthetic and does not represent a real
workforce. Correlation does not prove causation.
Productivity scores are practice metrics and should not
be treated as definitive measures of employee value.
"""

with open(output / "business_insights_report.txt", "w",
          encoding="utf-8") as file:
    file.write(report)

print("\nBUSINESS INSIGHTS REPORT")
print(report)

print("\nPROJECT COMPLETED SUCCESSFULLY!")
print("Check the folder:", output.resolve())
