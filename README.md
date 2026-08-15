# Bisoprolol Adverse Reaction Analysis
## Project Overview

This project analyzes adverse reaction data related to Bisoprolol using Python and Pandas.

The analysis focuses on patient demographics, geographical distribution, reaction outcomes, serious reactions, and case trends over time.

## Dataset
The dataset used in this project is:

`Bisoprolol_iccsr_sample_1068rows.xlsx`

The dataset contains **1068 cases**.

## Technologies Used

- Python
- Pandas
- Matplotlib
- JSON
- Excel

## Project Structure
```text
bisoprolol-iccsr-analysis/
│
├── data/
│   ├── Bisoprolol_iccsr_sample_1068rows.xlsx
│   ├── analysis_results.json
│   ├── age_group_distribution.png
│   ├── gender_distribution.png
│   ├── top_10_countries.png
│   └── cases_trend_over_time.png
│
├── src/
│   ├── analyze_data.py
│   └── visualize_data.py
│
├── prompts/
│
├── version1/
│
├── README.md
└── requirements.txt
## Analysis Performed

The project performs the following analysis:

- Total number of adverse reaction cases
- Distribution of cases by age group
- Distribution of cases by gender
- Top 10 countries by number of cases
- Most common adverse reactions
- Most common serious reactions
- Case trends over time

## Visualizations

The following visualizations are generated:

1. Cases by Age Group
2. Cases by Gender
3. Top 10 Countries by Cases
4. Cases Trend Over Time

All generated charts are saved in the `data/` directory.

## How to Run

### 1. Create and activate virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate
### 2. Install dependencies

pip install -r requirements.txt

### 3. Run data analysis

python src/analyze_data.py

### 4. Generate visualizations

python src/visualize_data.py

## Output

The analysis generates the following files:

- analysis_results.json
- age_group_distribution.png
- gender_distribution.png
- top_10_countries.png
- cases_trend_over_time.png

## Conclusion

This project demonstrates the use of Python and Pandas for analyzing adverse reaction data.

The analysis provides insights into patient demographics, geographical distribution, common adverse reactions, serious reactions, and case trends over time.