import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv("data/cleaned_job_listings.csv")

# Combine all skills into one list
all_skills = df["skills"].dropna().str.cat(sep=",").split(",")

# Count skill frequency
skill_counts = pd.Series(all_skills).value_counts()

# Plot
skill_counts.plot(kind="bar")
plt.title("Most In-Demand Skills in Germany (Job Listings)")
plt.xlabel("Skill")
plt.ylabel("Number of Job Listings")
plt.tight_layout()

# Save chart
plt.savefig("charts/skill_demand.png")
plt.show()