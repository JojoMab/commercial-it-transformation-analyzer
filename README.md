# Commercial IT Transformation Analyzer

![Python CI](https://github.com/JojoMab/commercial-it-transformation-analyzer/actions/workflows/python-ci.yml/badge.svg)

Python portfolio project for dual-study applications in business information systems, business engineering, sales and consulting.

The project analyzes a realistic synthetic Commercial IT project portfolio. It imports customer, project, workshop and service data into SQLite, calculates business KPIs and generates recruiter-friendly reports for business and IT stakeholders.

## GitHub Description

Python portfolio project for Commercial IT project prioritization with CSV, SQLite, KPI scoring and recruiter-friendly reports.

## Recruiter Snapshot

- Role fit: Bosch Building Technologies and Fujitsu Sales & Consulting
- Topic: Commercial IT, process digitization, project prioritization and consulting readiness
- Technology: Python standard library, CSV, SQLite, unit tests
- Dataset size: 24 customers, 72 project opportunities, 288 monthly service records, 72 workshop assessments
- Output: text report, CSV scoring table and SQLite database
- Runtime: under 10 seconds on a normal laptop
- Dependencies: no external Python packages

## Why This Project Fits The Roles

For Bosch Building Technologies, the project demonstrates:

- Commercial IT understanding
- ERP and database thinking through SQLite and structured CSV imports
- productivity and value creation analysis
- transparency for service and SLA risks in building and security-related processes
- workflow digitization through reporting and process improvement opportunities

For Fujitsu Sales & Consulting, the project demonstrates:

- customer and consulting readiness scoring
- prioritization of proposal and transformation projects
- sales-relevant pipeline analysis
- workshop-oriented recommendations
- clear communication of business value, payback and project risk

## Features

The CLI reads four CSV datasets and builds a SQLite database. It evaluates every project opportunity by:

- expected project value and margin
- monthly manual hours saved through automation
- annual productivity value
- payback period
- strategic customer priority
- consulting fit
- customer readiness
- technical and delivery risk

The result is a prioritized project list with recommendations:

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

## Examples

The example outputs are versioned intentionally so recruiters can inspect the result directly on GitHub without running the project locally:

- [Terminal output](examples/terminal_output.txt)
- [Sample transformation report](examples/transformation_report_sample.txt)

The terminal output shows the CLI run and the unit test run.

Run tests:

```bash
python3 -m unittest
```

Regenerate deterministic sample data:

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

These generated files are ignored by Git. A versioned sample report is available at [examples/transformation_report_sample.txt](examples/transformation_report_sample.txt).

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
│   ├── data_dictionary.md
│   └── recruiter_summary.md
├── examples/
│   ├── README.md
│   ├── terminal_output.txt
│   └── transformation_report_sample.txt
├── scripts/
│   └── generate_sample_data.py
└── tests/
    └── test_analysis.py
```

## Data Quality

The data is fictional and safe to publish. It is generated with a fixed random seed in `scripts/generate_sample_data.py`, so the sample dataset is reproducible.

The dataset is designed to resemble realistic Commercial IT and consulting scenarios:

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

The CSV scoring table can be reused for spreadsheet or Power BI-style analysis.

## Application Statement

As an application project, I built a Commercial IT Transformation Analyzer. The Python tool processes a realistic synthetic dataset with customer, project, workshop and service data, stores it in a SQLite database and calculates KPIs such as project value, margin, payback period, productivity gain and SLA risk. It generates a text report and a CSV evaluation. The project connects computer science, business administration, data analysis, process digitization and sales-/consulting-oriented thinking.

## Author

Johannes Maboudou
