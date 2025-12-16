import pandas as pd

# Load cleaned data
df = pd.read_csv("data/cleaned_job_listings.csv")

total_jobs = len(df)

# Python & SQL demand
python_jobs = df[df["skills"].str.contains("python", case=False, na=False)]
sql_jobs = df[df["skills"].str.contains("sql", case=False, na=False)]

# Working student roles
working_student_jobs = df[df["employment_type"] == "Working Student"]

print("===== JOB MARKET ANALYSIS (GERMANY) =====")
print(f"Total job listings: {total_jobs}")
print(f"Jobs requiring Python: {len(python_jobs)} ({len(python_jobs)/total_jobs:.0%})")
print(f"Jobs requiring SQL: {len(sql_jobs)} ({len(sql_jobs)/total_jobs:.0%})")
print(f"Working student roles: {len(working_student_jobs)}")