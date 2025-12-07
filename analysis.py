# analysis.py
# Author: 22f2001145@ds.study.iitm.ac.in
# Healthcare Quarterly Satisfaction Analysis

import matplotlib.pyplot as plt

# Quarterly patient satisfaction scores
quarters = ["Q1", "Q2", "Q3", "Q4"]
scores = [4.72, 5.71, 1.27, 4.68]
industry_target = 4.5

# Compute the average
average_score = sum(scores) / len(scores)
print("Average satisfaction score:", round(average_score, 1))

# Line chart with benchmark
plt.figure(figsize=(8, 4))
plt.plot(quarters, scores, marker="o", linewidth=2, label="Patient Satisfaction Score")
plt.axhline(industry_target, color="red", linestyle="--", label="Industry Target (4.5)")
plt.title("2024 Quarterly Patient Satisfaction Trend")
plt.xlabel("Quarter")
plt.ylabel("Satisfaction Score")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig("visualization.png")
print("Saved chart as visualization.png")
