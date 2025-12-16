import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import ast  # for converting string lists to actual lists
import os

# Ensure the charts folder exists
os.makedirs("charts", exist_ok=True)

# Load cleaned data
df = pd.read_csv("data/cleaned_job_listings.csv")

# Convert string representation of lists to actual lists
def parse_skills(s):
    try:
        skills = ast.literal_eval(s)  # converts "['python','sql']" -> ['python','sql']
        if isinstance(skills, list):
            return skills
        return [s]
    except:
        return [s]

# Extract all skills
all_skills = []
for val in df["skills"].dropna():
    all_skills.extend(parse_skills(val))

# Clean whitespace
all_skills = [skill.strip() for skill in all_skills]

# Count frequency of each unique skill
skill_counts = Counter(all_skills)

# Convert to pandas Series for plotting
skill_counts_series = pd.Series(skill_counts).sort_values(ascending=False)

# -----------------------------
# Top 3 Most In-Demand Skills
# -----------------------------
top_3_skills = skill_counts_series.head(3)

plt.figure(figsize=(6,4))
top_3_skills.plot(kind="bar", color='orange')
plt.title("Top 3 In-Demand Skills in Germany")
plt.xlabel("Skill")
plt.ylabel("Number of Job Listings")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("charts/top_3_skills.png")
plt.show()

# -----------------------------
# (Top 5 + Other)
# -----------------------------
top_5 = skill_counts_series.head(5)
other = skill_counts_series[5:].sum()
pie_data = pd.concat([top_5, pd.Series({'Other': other})])

plt.figure(figsize=(6,6))
pie_data.plot(kind="pie", autopct='%1.1f%%', startangle=140)
plt.title("Skill Demand Distribution (Top 5 + Other)")
plt.ylabel("")  # remove y-label
plt.tight_layout()
plt.savefig("charts/skill_distribution.png")
plt.show()