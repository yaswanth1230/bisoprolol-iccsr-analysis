import pandas as pd

# Dataset path
file_path = "data/Bisoprolol_icsr_sample_1068rows.xlsx"

# Read Excel file
df = pd.read_excel(file_path)

print("Dataset loaded successfully!")
print("Rows:", len(df))
print("Columns:", len(df.columns))

print("\nColumn names:")
for column in df.columns:
    print("-", column)

# Count unique safety cases
if "safetyreportid" in df.columns:
    unique_cases = df["safetyreportid"].nunique()
    print("\nUnique cases:", unique_cases)

# Check reporting date range
if "receivedate" in df.columns:
    df["receivedate"] = pd.to_datetime(
    df["receivedate"].astype(str),
    format="%Y%m%d",
    errors="coerce"
)

    print("\nReporting period:")
    print("Start:", df["receivedate"].min())
    print("End:", df["receivedate"].max())

    print("\nRelevant analysis columns:")

keywords = [
    "serious",
    "severity",
    "age",
    "sex",
    "gender",
    "country",
    "reaction",
    "outcome",
    "receivedate"
]

for column in df.columns:
    column_lower = column.lower()

    if any(keyword in column_lower for keyword in keywords):
        print("-", column)

print("\nSerious field values:")
print(df["serious"].value_counts(dropna=False))

print("\nCase-level serious analysis:")

case_serious = (
    df.groupby("safetyreportid")["serious"]
    .agg(lambda x: (x.astype(str).str.lower() == "serious").any())
)

print("Total unique cases:", len(case_serious))
print("Serious cases:", case_serious.sum())
print("Non-serious cases:", (~case_serious).sum())

print("\nSeriousness reasons:")

reason_columns = [
    "seriousnessdeath",
    "seriousnesslifethreatening",
    "seriousnesshospitalization",
    "seriousnessdisabling",
    "seriousnesscongenitalanomali",
    "seriousnessother"
]

for column in reason_columns:
    print(f"\n{column}:")
    print(df[column].value_counts(dropna=False))

print("\nAge information:")

print("Age units:")
print(df["patient_patientonsetageunit"].value_counts(dropna=False))

print("\nAge summary:")
print(df["patient_patientonsetage"].describe())

print("\nAge group analysis:")

df["age_group"] = pd.cut(
    df["patient_patientonsetage"],
    bins=[0, 18, 40, 60, 80, 120],
    labels=["0-18", "19-40", "41-60", "61-80", "80+"]
)

print(df["age_group"].value_counts().sort_index())

print("\nAge group vs seriousness:")

age_serious = pd.crosstab(
    df["age_group"],
    df["serious"]
)

print(age_serious)
print("\nGender analysis:")

print(df["patient_patientsex"].value_counts(dropna=False))

print("\nGender vs seriousness:")

gender_serious = pd.crosstab(
    df["patient_patientsex"],
    df["serious"]
)

print(gender_serious)
print("\nCountry analysis:")

print(df["primarysourcecountry"].value_counts().head(15))
print("\nCountry vs seriousness:")

country_serious = pd.crosstab(
    df["primarysourcecountry"],
    df["serious"]
)

print(country_serious)
print("\nReaction outcome analysis:")

print(
    df["patient_reaction_reactionoutcome"]
    .value_counts(dropna=False)
)

print("\nClean reaction outcome analysis:")

reaction_outcomes = (
    df["patient_reaction_reactionoutcome"]
    .dropna()
    .astype(str)
    .str.split(",")
    .explode()
    .str.strip()
)

print(reaction_outcomes.value_counts())
print("\nReaction outcome vs seriousness:")

print("\nReaction outcome vs seriousness:")

reaction_series = df[
    ["patient_reaction_reactionoutcome", "serious"]
].dropna()

reaction_series = reaction_series.assign(
    reaction_outcome=reaction_series[
        "patient_reaction_reactionoutcome"
    ].str.split(",")
).explode("reaction_outcome")

reaction_series["reaction_outcome"] = (
    reaction_series["reaction_outcome"].str.strip()
)

reaction_series = reaction_series.reset_index(drop=True)

reaction_serious_table = pd.crosstab(
    reaction_series["reaction_outcome"],
    reaction_series["serious"]
)

print(reaction_serious_table)
print("\nKey insights:")

print("Total cases:", len(df))
print("Serious cases:", (df["serious"] == "serious").sum())
print("Non-serious cases:", (df["serious"] == "not serious").sum())

print("\nMost common age group:")
print(df["age_group"].value_counts().idxmax())

print("\nMost common gender:")
print(df["patient_patientsex"].value_counts().idxmax())

print("\nTop 5 countries:")
print(df["primarysourcecountry"].value_counts().head(5))

print("\nTop reaction outcomes:")
print(reaction_outcomes.value_counts().head(5))
print("\nMost common reactions:")

reaction_counts = (
    df["patient_reaction_reactionmeddrapt"]
    .dropna()
    .value_counts()
)

print(reaction_counts.head(10))


print("\nMost common serious reactions:")

serious_reactions = (
    df[df["serious"] == "serious"]
    ["patient_reaction_reactionmeddrapt"]
    .dropna()
    .value_counts()
)

print(serious_reactions.head(10))
print("\nTrend over time:")

df["receivedate"] = pd.to_datetime(
    df["receivedate"],
    errors="coerce"
)

monthly_cases = (
    df.groupby(df["receivedate"].dt.to_period("M"))
    .size()
)

print(monthly_cases)
print("\nSaving analysis results...")

analysis_results = {
    "total_cases": len(df),

    "seriousness": df["serious"].value_counts(dropna=False).to_dict(),

    "most_common_age_group": df["age_group"].value_counts().idxmax(),

    "most_common_gender": df["patient_patientsex"].value_counts(
        dropna=True
    ).idxmax(),

    "top_5_countries": df["primarysourcecountry"].value_counts().head(5).to_dict(),

    "top_reaction_outcomes": reaction_outcomes.value_counts().head(5).to_dict(),

    "most_common_reactions": reaction_counts.head(10).to_dict(),

    "most_common_serious_reactions": serious_reactions.head(10).to_dict(),

    "monthly_cases": {
    str(k): int(v)
    for k, v in monthly_cases.items()
}
}


import json

with open("data/analysis_results.json", "w") as f:
    json.dump(analysis_results, f, indent=4, default=str)

print("Analysis results saved to data/analysis_results.json")