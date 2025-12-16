import pandas as pd

# Load raw job data
df = pd.read_csv("data/job_listings.csv")

# Standardize column names
df.columns = df.columns.str.lower()

# Handle missing salary values
df["salary"] = df["salary"].fillna(0)

# Clean whitespace
df["employment_type"] = df["employment_type"].str.strip()
df["location"] = df["location"].str.strip()

# Convert skills into lowercase list
df["skills"] = df["skills"].str.lower().str.split(",")

print("Cleaned data preview:")
print(df.head())

# Save cleaned data
df.to_csv("data/cleaned_job_listings.csv", index=False)