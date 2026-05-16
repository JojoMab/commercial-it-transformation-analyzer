# Commercial IT Transformation Analyzer

![Python CI](https://github.com/JojoMab/commercial-it-transformation-analyzer/actions/workflows/python-ci.yml/badge.svg)

Dieses Bewerberprojekt analysiert synthetische Kunden-, Projekt-, Workshop- und Servicedaten. Es verbindet Wirtschaftsinformatik, KPI-Auswertung, SQLite, Projektpriorisierung, Ampellogik und Management Summary.

## Bewerbungskontext

Das Projekt passt zu dualen Studiengängen in Wirtschaftsinformatik, Business Information Systems und Informatik mit Consulting-Bezug. Es ist relevant für Bosch, Deloitte, metafinanz, CANCOM, Fujitsu, ADAC, EY und Telekom.

## Tech Stack

- Python 3.11
- SQLite
- CSV-Daten
- KPI-Scoring
- Unit Tests
- GitHub Actions

## Funktionen

- synthetische Projektdaten in SQLite laden
- KPI- und Service-Risiken auswerten
- Projektprioritäten berechnen
- Ampelstatus ROT/GELB/GRÜN ableiten
- Management Summary als TXT erzeugen
- Tests für Scoring und KPI-Auswertung ausführen

## Projektstruktur

```txt
commercial-it-transformation-analyzer/
├── main.py
├── commercial_it_analyzer/
│   ├── analysis.py
│   ├── storage.py
│   ├── report.py
│   ├── project_analyzer.py
│   ├── kpi_evaluator.py
│   └── report_generator.py
├── data/
├── tests/
└── docs/
```

## Schnellstart

```bash
python main.py
```

## Tests

```bash
python -m unittest discover -s tests -v
```

## Beispielausgabe

```txt
Commercial IT transformation analysis completed.
Projects analyzed: 72
Pipeline value: 7,191,000.00 EUR
```

## Hinweis auf synthetische Daten

Alle Kunden-, Projekt- und Servicedaten sind synthetisch. Das Projekt ist eine Bewerberprojekt-Simulation und verwendet keine echten Unternehmensdaten.

## English Summary

This project demonstrates business information systems fundamentals with synthetic transformation project data. It combines SQLite, KPI analysis, project scoring, traffic-light status logic and management reporting.
