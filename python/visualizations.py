import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import ast  # for converting string lists to actual lists
import os

# Ensure the charts folder exists
os.makedirs("charts", exist_ok=True)

# Load cleaned data
df = pd.read_csv(r"C:\Users\u23092\Desktop\job-market-analysis-germany\data\cleaned_job_listings.csv")

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

# -----------------------------
# Top Job Positions
# -----------------------------
job_counts = df['job_title'].value_counts()
plt.figure(figsize=(8,5))
job_counts.plot(kind='bar', color='skyblue')
plt.title("Top Job Titles")
plt.xlabel("Job Title")
plt.ylabel("Count")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("charts/top_job_titles.png")
plt.clf()

# -----------------------------
# Jobs by Location
# -----------------------------
location_counts = df['location'].value_counts()
plt.figure(figsize=(6,4))
location_counts.plot(kind='bar', color='green')
plt.title("Job Openings by Location")
plt.xlabel("City")
plt.ylabel("Count")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("charts/jobs_by_location.png")
plt.clf()
# -----------------------------
# Average Salary Per Job Title
# -----------------------------

salary_df = df[df['salary'] > 0]
if not salary_df.empty:
    avg_salary = salary_df.groupby('job_title')['salary'].mean().sort_values(ascending=False)
    plt.figure(figsize=(8,5))
    avg_salary.plot(kind='bar', color='purple')
    plt.title("Average Salary by Job Title")
    plt.ylabel("Salary (EUR)")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig("charts/average_salary.png")
    plt.clf()

print("All charts created successfully in the 'charts' folder!")