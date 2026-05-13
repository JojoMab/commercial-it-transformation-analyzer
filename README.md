# Commercial IT Transformation Analyzer

![Python CI](https://github.com/JojoMab/commercial-it-transformation-analyzer/actions/workflows/python-ci.yml/badge.svg)

Python portfolio project for dual-study applications in Wirtschaftsinformatik, Business Engineering and Sales & Consulting.

This project evaluates a realistic synthetic Commercial IT project portfolio. It imports customer, project, workshop and service data into SQLite, calculates business KPIs and produces recruiter-friendly text and CSV reports.

## Recruiter Summary

- Role fit: Bosch Building Technologies and Fujitsu Sales & Consulting
- Topic: Commercial IT, process digitization, project prioritization and consulting readiness
- Tech stack: Python standard library, CSV, SQLite, unit tests
- Dataset size: 24 customers, 72 project opportunities, 288 monthly service records, 72 workshop assessments
- Output: text report, CSV score table and SQLite database
- Run time: under 10 seconds on a normal laptop
- Dependencies: none beyond Python 3

## Why This Project Fits The Roles

For Bosch Building Technologies, the project shows:

- Commercial IT thinking
- ERP and database understanding through SQLite and structured CSV import
- productivity and value-creation analysis
- service and SLA transparency for building/security operations
- process digitization through workflow and reporting opportunities

For Fujitsu Sales & Consulting, the project shows:

- customer and consulting readiness scoring
- proposal and transformation project prioritization
- sales-relevant pipeline analysis
- workshop-oriented recommendations
- clear communication of business value, payback and risk

## What The Program Does

The CLI reads four CSV datasets and builds an SQLite database. It then evaluates every project opportunity by:

- expected value and margin
- monthly manual hours saved through automation
- annual productivity value
- payback period
- strategic customer priority
- consulting fit
- customer readiness
- technical and delivery risk

The result is a ranked project list with recommendations:

- `Lead project`
- `Prepare proposal`
- `Run discovery workshop`
- `Monitor backlog`

## Quick Start

Run the project from the repository root:

```bash
python3 main.py
```

Expected terminal output:

```txt
Commercial IT transformation analysis completed.
Projects analyzed: 72
Pipeline value: 7,191,000.00 EUR
Annual productivity value: 2,858,611.20 EUR
Report: output/reports/transformation_report.txt
Project scores: output/reports/project_scores.csv
```

Run tests:

```bash
python3 -m unittest
```

Regenerate the deterministic sample data:

```bash
python3 scripts/generate_sample_data.py
```

## Generated Files

Running `python3 main.py` creates:

```txt
output/reports/commercial_it.db
output/reports/transformation_report.txt
output/reports/project_scores.csv
```

These generated files are ignored by Git. A tracked sample report is available at:

```txt
examples/transformation_report_sample.txt
```

## Project Structure

```txt
.
├── main.py
├── commercial_it_analyzer/
│   ├── analysis.py
│   ├── report.py
│   └── storage.py
├── data/
│   ├── customers.csv
│   ├── projects.csv
│   ├── service_metrics.csv
│   └── workshops.csv
├── docs/
│   ├── application_fit.md
│   └── data_dictionary.md
├── examples/
│   └── transformation_report_sample.txt
├── scripts/
│   └── generate_sample_data.py
└── tests/
    └── test_analysis.py
```

## Data Quality

The data is fictional and safe to publish. It is generated with a fixed random seed in `scripts/generate_sample_data.py`, so the sample dataset is reproducible.

The data is designed to resemble realistic Commercial IT and consulting scenarios:

- multiple industries and regions
- customer-specific system counts and revenue bands
- project categories such as ERP & Data, Commercial IT, Sales Enablement and Process Digitization
- monthly service KPIs over a full year
- workshop fields such as stakeholder count, requirements clarity and commercial urgency

## Main Outputs

The text report provides:

- portfolio KPI summary
- recommendation distribution
- category-level pipeline summary
- top project recommendations
- service risk view
- application relevance for Bosch and Fujitsu

The CSV score table provides project-level data for spreadsheet or Power BI-style analysis.

## Application Statement

Als Bewerberprojekt habe ich einen Commercial IT Transformation Analyzer entwickelt. Das Python-Tool verarbeitet einen realistischen synthetischen Datensatz mit Kunden-, Projekt-, Workshop- und Servicedaten, speichert ihn in einer SQLite-Datenbank und berechnet Kennzahlen wie Projektwert, Marge, Amortisationszeit, Produktivitätsgewinn und SLA-Risiko. Daraus entstehen ein Textreport und eine CSV-Auswertung. Das Projekt verbindet Informatik, BWL, Datenanalyse, Prozessdigitalisierung und Sales-/Consulting-orientiertes Denken.

## Author

Johannes Maboudou
