# Bisoprolol ICSR Analysis

## Project Overview

This project analyzes adverse drug reaction data related to Bisoprolol using Python and Pandas.

The system processes Individual Case Safety Reports (ICSRs), performs case-level and reaction-level analysis, generates visualizations, and produces a structured safety analysis report.

The analysis separates deterministic numerical calculations from AI-assisted reasoning and narrative generation.

## Dataset

The supplied Bisoprolol ICSR dataset contains:

- 1,068 rows
- 1,024 unique safety cases
- 1,023 serious cases
- 1 non-serious case
- Reporting period: 2024-12-27 to 2025-12-26

The dataset contains multiple reaction rows for some safety reports. Therefore, case-level metrics are calculated using the unique `safetyreportid`, while reaction and outcome metrics are calculated at the reaction level.

## Technologies Used

- Python
- Pandas
- Matplotlib
- JSON
- Excel
- Git
- GitHub

## Project Structure

```text
bisoprolol-icsr-analysis/
│
├── data/
│   ├── analysis_results.json
│   ├── case_index.csv
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
│   └── analysis_prompt.txt
│
├── version1/
│   ├── README.md
│   └── generate_report.py
│
├── README.md
├── report_output.md
└── requirements.txt
```

## Analysis Performed

The project performs the following analysis:

### Case-Level Analysis

- Total unique safety cases
- Serious and non-serious cases
- Age-group distribution
- Gender distribution
- Geographic distribution
- Monthly case trends
- 15-Day Alert / expedited cases

### Reaction-Level Analysis

- Most common adverse reactions
- Most common serious reactions
- Reaction outcomes
- Reaction outcome distribution

### Case Index

A structured case index is generated with:

- Safety report ID
- Reaction / adverse event
- Seriousness
- Reporting date
- Country
- Outcome

The case index is stored in:

`data/case_index.csv`

This allows aggregate results to be traced back to individual safety cases.

## Visualizations

The project generates the following visualizations:

1. Cases by Age Group
2. Cases by Gender
3. Top 10 Countries by Cases
4. Cases Trend Over Time

All generated charts are stored in the `data/` directory.

## How to Run

### 1. Create a virtual environment

```bash
python -m venv .venv
```

### 2. Activate the virtual environment

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run data analysis

```bash
python src/analyze_data.py
```

This generates:

- `data/analysis_results.json`
- `data/case_index.csv`

### 5. Generate visualizations

```bash
python src/visualize_data.py
```

This generates:

- `data/age_group_distribution.png`
- `data/gender_distribution.png`
- `data/top_10_countries.png`
- `data/cases_trend_over_time.png`

### 6. Generate the analysis report

```bash
python version1/generate_report.py
```

This generates:

- `report_output.md`

## Output

The main outputs of the project are:

- `analysis_results.json` — deterministic analysis results
- `case_index.csv` — case-level evidence index
- Visualization PNG files
- `report_output.md` — generated safety analysis report

## Reporting Period

The reporting period is derived from the `receivedate` field in the supplied dataset.

**Reporting Period:** 2024-12-27 to 2025-12-26

## 15-Day Alerts

The dataset identifies 1,023 of 1,024 unique cases as meeting the expedited reporting criteria.

The analysis therefore reports:

- Total unique cases: 1,024
- 15-Day Alert / expedited cases: 1,023
- Non-expedited cases: 1

This classification is derived from the supplied dataset. No additional regulatory conclusions are inferred.

## History of Safety-Related Actions

No history of safety-related actions was supplied with the dataset for this exercise.

Therefore, the project does not invent or infer:

- Labeling changes
- Regulatory communications
- Safety-related studies
- Additional monitoring
- Risk-minimization actions
- Other regulatory actions

## Reaction and Outcome Analysis

The analysis distinguishes between case-level and reaction-level information.

A single safety case can contain more than one reaction. Therefore:

- Case counts use unique `safetyreportid`
- Reaction counts are calculated at the reaction level
- Outcome counts are calculated at the reaction level

This prevents multiple reaction rows belonging to the same safety case from being incorrectly counted as separate cases.

## AI vs Deterministic Processing

The project separates numerical analysis from AI-assisted reasoning.

### Deterministic Python Processing

Python is responsible for:

- Loading and validating the safety dataset
- Deduplicating safety reports
- Calculating unique case counts
- Calculating seriousness
- Creating age groups
- Analyzing gender and country distribution
- Analyzing adverse reactions
- Analyzing reaction outcomes
- Calculating monthly case trends
- Identifying 15-Day Alert / expedited cases
- Creating the case index
- Saving structured analysis results to JSON

These operations are deterministic and reproducible.

### AI-Assisted Reasoning

AI reasoning is intended for:

- Selecting relevant findings
- Interpreting trends
- Producing narrative summaries
- Explaining observations in natural language
- Organizing evidence into report sections

The AI layer should not independently calculate or invent quantitative safety results when deterministic analysis is available.

## Grounding

All quantitative statements in the generated report are derived from the deterministic analysis results stored in:

`data/analysis_results.json`

Individual case-level evidence is available in:

`data/case_index.csv`

This provides traceability from aggregate findings to individual cases.

## Limitations

The current implementation has the following limitations:

- System Organ Class (SOC) analysis is not available because SOC information was not supplied.
- Expectedness assessment is outside the scope because product label or reference safety information was not supplied.
- History of regulatory or sponsor actions was not supplied.
- The analysis is based only on the supplied dataset.
- Descriptive findings do not establish causality.
- The system does not independently determine new medical safety signals.
- AI-generated narrative must remain grounded in deterministic evidence.
- Human review is required before treating the generated output as a regulatory document.

## Evaluation Approach

The system can be evaluated using the following criteria:

### Numerical Accuracy

Quantitative statements in the generated report should match the deterministic analysis results.

### Grounding

Generated statements should be traceable to `analysis_results.json` and, where appropriate, `case_index.csv`.

### Completeness

The report should contain the required analytical sections, including:

- Reporting Period
- Narrative Summary and Analysis
- Case Analysis
- Reaction Analysis
- Serious / 15-Day Alert Analysis
- Trends
- History of Actions
- Case Index / Listing
- Data Limitations
- Grounding

### Reproducibility

Running the deterministic analysis on the same input dataset should produce the same numerical results.

### Human Review

A reviewer should verify numerical consistency, evidence traceability, appropriate interpretation, and absence of unsupported medical conclusions.

## Version 1

The `version1/` directory contains the automated report-generation implementation.

```text
version1/
├── README.md
└── generate_report.py
```

The report generator reads:

`data/analysis_results.json`

and generates:

`report_output.md`

## Conclusion

This project demonstrates an evidence-backed safety-reporting workflow that separates deterministic data analysis from AI-assisted reasoning.

Python provides reproducible numerical analysis and structured evidence, while AI-assisted reasoning can be used to interpret those findings and generate grounded narrative content.

The workflow is designed to keep safety reporting traceable to the underlying evidence and to avoid unsupported quantitative or medical conclusions.
