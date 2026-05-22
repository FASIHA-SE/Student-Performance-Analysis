import pandas as pd
import matplotlib.pyplot as plt
import os

# create charts folder
if not os.path.exists("charts"):
    os.makedirs("charts")

# load dataset
df = pd.read_csv("students.csv")

# calculate overall average
df["Average"] = (df["Math"] + df["English"] + df["Science"]) / 3

print("\nStudent Data:\n")
print(df)

# -----------------------------
# 1. Subject-wise averages
# -----------------------------
subjects = ["Math", "English", "Science"]
subject_avg = df[subjects].mean()

print("\nSubject Averages:")
print(subject_avg)

# bar chart
subject_avg.plot(kind="bar")
plt.title("Subject Wise Average Marks")
plt.ylabel("Marks")
plt.savefig("charts/subject_average.png")
plt.close()

# -----------------------------
# 2. Attendance vs Performance
# -----------------------------
plt.scatter(df["Attendance"], df["Average"])
plt.title("Attendance vs Performance")
plt.xlabel("Attendance")
plt.ylabel("Average Marks")
plt.savefig("charts/attendance_vs_performance.png")
plt.close()

# -----------------------------
# 3. Study Hours vs Performance
# -----------------------------
plt.plot(df["StudyHours"], df["Average"], marker='o')
plt.title("Study Hours vs Performance")
plt.xlabel("Study Hours")
plt.ylabel("Average Marks")
plt.savefig("charts/study_vs_performance.png")
plt.close()

# -----------------------------
# 4. Class comparison
# -----------------------------
class_avg = df.groupby("Class")["Average"].mean()

class_avg.plot(kind="pie", autopct='%1.1f%%')
plt.title("Class Performance Comparison")
plt.ylabel("")
plt.savefig("charts/class_comparison.png")
plt.close()

# -----------------------------
# 5. Insights
# -----------------------------
top_student = df.loc[df["Average"].idxmax()]

insights = f"""
STUDENT PERFORMANCE ANALYSIS REPORT

1. Best Performing Student:
{top_student['Name']} with average marks {top_student['Average']:.2f}

2. Subject-wise Average:
{subject_avg}

3. Observation:
- Higher attendance improves performance.
- More study hours generally increase marks.
- Class comparison shows performance differences.

4. Conclusion:
Students with better attendance and study habits
perform better academically.
"""

print(insights)

# save report
with open("report.txt", "w") as file:
    file.write(insights)

print("\nProject completed successfully!")