import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_excel("data/Bisoprolol_icsr_sample_1068rows.xlsx")

# -------------------------------
# 1. Age Group Distribution
# -------------------------------

df["age_group"] = pd.cut(
    df["patient_patientonsetage"],
    bins=[0, 18, 40, 60, 80, 120],
    labels=["0-18", "19-40", "41-60", "61-80", "80+"]
)

df["age_group"].value_counts().sort_index().plot(kind="bar")

plt.title("Cases by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Number of Cases")
plt.tight_layout()
plt.savefig("data/age_group_distribution.png")
plt.close()


# -------------------------------
# 2. Gender Distribution
# -------------------------------

df["patient_patientsex"].value_counts(dropna=True).plot(kind="bar")

plt.title("Cases by Gender")
plt.xlabel("Gender")
plt.ylabel("Number of Cases")
plt.tight_layout()
plt.savefig("data/gender_distribution.png")
plt.close()


# -------------------------------
# 3. Top 10 Countries
# -------------------------------

df["primarysourcecountry"].value_counts().head(10).plot(kind="bar")

plt.title("Top 10 Countries by Cases")
plt.xlabel("Country")
plt.ylabel("Number of Cases")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("data/top_10_countries.png")
plt.close()

# ------------------------------
# 4. Cases Trend Over Time
# ------------------------------

import json

# Load analysis results
with open("data/analysis_results.json", "r") as f:
    analysis_results = json.load(f)

# Get monthly trend
monthly_cases = analysis_results["monthly_cases"]

months = list(monthly_cases.keys())
cases = list(monthly_cases.values())

plt.figure(figsize=(10, 5))

plt.plot(
    months,
    cases,
    marker="o"
)

plt.title("Cases Trend Over Time")
plt.xlabel("Month")
plt.ylabel("Number of Cases")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("data/cases_trend_over_time.png")
plt.close()