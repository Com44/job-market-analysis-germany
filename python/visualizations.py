import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# Load cleaned data
df = pd.read_csv("data/cleaned_job_listings.csv")

# Combine all skills into one list and clean whitespace
all_skills = df["skills"].dropna().str.cat(sep=",").split(",")
all_skills = [skill.strip() for skill in all_skills]  # remove extra spaces

# Count frequency of each unique skill
skill_counts = Counter(all_skills)

# Convert to pandas Series for plotting
skill_counts_series = pd.Series(skill_counts).sort_values(ascending=False)

# Plot
skill_counts_series.plot(kind="bar", figsize=(10,6))
plt.title("Most In-Demand Skills in Germany (Job Listings)")
plt.xlabel("Skill")
plt.ylabel("Number of Job Listings")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

# Save chart
plt.savefig("charts/skill_demand.png")
plt.show()