# Commercial IT Transformation Analyzer

Commercial IT Transformation Analyzer is a Python CLI project for evaluating digitalization, sales consulting and commercial IT project opportunities.

The project was designed as a portfolio project for dual study applications in Wirtschaftsinformatik. It connects business analysis, data processing, database usage and consulting-style recommendations.

## Target Roles

This project is tailored to two application targets:

- Bosch Building Technologies: B.Sc. Wirtschaftsinformatik - Business Engineering
- Fujitsu Germany: B.Sc. Wirtschaftsinformatik Sales & Consulting

## Why This Project Fits

The analyzer simulates a practical Commercial IT and Sales Consulting workflow:

- customer and project data is loaded from CSV files into SQLite
- project opportunities are evaluated by value, margin, payback time and productivity impact
- service metrics are analyzed for SLA and operational risk
- consulting readiness and customer urgency are included in the project score
- results are exported as a text report and CSV score table

This directly demonstrates:

- data and database handling
- analytical thinking
- business and IT understanding
- workflow digitization
- consulting-oriented communication
- structured project prioritization

## Features

- CSV import into SQLite
- Portfolio KPI calculation
- Project scoring for Commercial IT and Sales Consulting use cases
- Productivity value calculation based on saved manual work hours
- SLA and service risk analysis for security/building operations scenarios
- Text report generation
- CSV export for spreadsheet or Power BI usage
- deterministic sample data generator
- No external Python dependencies

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
├── scripts/
│   └── generate_sample_data.py
├── tests/
│   └── test_analysis.py
└── output/
    └── reports/
```

## Usage

Run the default analysis:

```bash
python3 main.py
```

The command generates:

```txt
output/reports/commercial_it.db
output/reports/transformation_report.txt
output/reports/project_scores.csv
```

Use custom paths:

```bash
python3 main.py \
  --data-dir data \
  --database output/reports/commercial_it.db \
  --report output/reports/transformation_report.txt \
  --scores output/reports/project_scores.csv
```

## Example Output

```txt
Commercial IT transformation analysis completed.
Projects analyzed: 72
Pipeline value: 7,191,000.00 EUR
Annual productivity value: 2,858,611.20 EUR
Report: output/reports/transformation_report.txt
Project scores: output/reports/project_scores.csv
```

## Tests

Run the unit tests:

```bash
python3 -m unittest
```

## Data Model

The project uses four CSV datasets:

- `customers.csv`: 24 customer profiles across industries, regions, revenue bands and strategic priorities
- `projects.csv`: 72 project opportunities with value, cost, manual effort, automation impact and implementation risk
- `service_metrics.csv`: 288 monthly service rows covering ticket volume, SLA breaches, resolution time and downtime
- `workshops.csv`: 72 consulting readiness assessments with stakeholders, requirements clarity and urgency

The data is intentionally fictional and safe to publish, but the ranges are designed to be realistic for Commercial IT, building services, Sales Consulting and transformation portfolio scenarios.

Regenerate the deterministic sample data:

```bash
python3 scripts/generate_sample_data.py
```

## Scoring Logic

Each project receives a priority score based on:

- expected margin
- productivity improvement
- strategic customer relevance
- consulting fit
- customer readiness
- requirements clarity
- delivery and technical risk

The result is translated into a recommendation:

- `Lead project`
- `Prepare proposal`
- `Run discovery workshop`
- `Monitor backlog`

## Application Statement

I developed a Commercial IT Transformation Analyzer that evaluates digitalization and consulting projects using customer, service and project data. The tool loads CSV data into SQLite, calculates business KPIs such as margin, payback time and productivity value, and generates a consulting-oriented text report plus a CSV score table. The project connects Wirtschaftsinformatik, data analysis, process digitization and Sales & Consulting workflows.

## Author

Johannes Maboudou
