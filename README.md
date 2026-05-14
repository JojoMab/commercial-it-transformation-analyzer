# Commercial IT Transformation Analyzer

![Python CI](https://github.com/JojoMab/commercial-it-transformation-analyzer/actions/workflows/python-ci.yml/badge.svg)

Python-Portfolio-Projekt für Bewerbungen im dualen Studium Wirtschaftsinformatik, Business Engineering sowie Sales & Consulting.

Das Projekt analysiert ein realistisches, synthetisches Commercial-IT-Projektportfolio. Es importiert Kunden-, Projekt-, Workshop- und Servicedaten in SQLite, berechnet betriebswirtschaftliche Kennzahlen und erzeugt gut lesbare Reports für Recruiter und Fachabteilungen.

## GitHub-Beschreibung

Python-Portfolio-Projekt zur Commercial-IT-Projektpriorisierung mit CSV, SQLite, KPI-Scoring und recruiterfreundlichen Reports.

## Kurzprofil für Recruiter

- Rollenbezug: Bosch Building Technologies und Fujitsu Sales & Consulting
- Thema: Commercial IT, Prozessdigitalisierung, Projektpriorisierung und Consulting Readiness
- Technologie: Python-Standardbibliothek, CSV, SQLite, Unit Tests
- Datenumfang: 24 Kunden, 72 Projektchancen, 288 monatliche Service-Datensätze, 72 Workshop-Bewertungen
- Ergebnis: Textreport, CSV-Scoring-Tabelle und SQLite-Datenbank
- Laufzeit: unter 10 Sekunden auf einem normalen Laptop
- Abhängigkeiten: keine externen Python-Pakete

## Warum das Projekt zu den Stellen passt

Für Bosch Building Technologies zeigt das Projekt:

- Commercial-IT-Verständnis
- ERP- und Datenbankbezug durch SQLite und strukturierten CSV-Import
- Analyse von Produktivität und Wertschöpfung
- Transparenz zu Service- und SLA-Risiken in gebäude- und sicherheitsnahen Prozessen
- Digitalisierung von Arbeitsabläufen durch Reporting- und Workflow-Potenziale

Für Fujitsu Sales & Consulting zeigt das Projekt:

- Bewertung von Kunden- und Consulting Readiness
- Priorisierung von Angebots- und Transformationsprojekten
- Analyse einer sales-relevanten Pipeline
- Workshop-orientierte Handlungsempfehlungen
- klare Kommunikation von Business Value, Amortisation und Projektrisiko

## Funktionsumfang

Das CLI liest vier CSV-Datensätze ein und baut daraus eine SQLite-Datenbank. Anschließend bewertet es jede Projektchance nach:

- erwartetem Projektwert und Marge
- monatlich eingesparten manuellen Stunden durch Automatisierung
- jährlichem Produktivitätswert
- Amortisationszeit
- strategischer Kundenpriorität
- Consulting Fit
- Kundenbereitschaft
- technischem und organisatorischem Risiko

Aus den Kennzahlen entsteht eine priorisierte Projektliste mit Empfehlungen:

- `Lead project`
- `Prepare proposal`
- `Run discovery workshop`
- `Monitor backlog`

## Schnellstart

Projekt aus dem Repository-Root starten:

```bash
python3 main.py
```

Erwartete Terminalausgabe:

```txt
Commercial IT transformation analysis completed.
Projects analyzed: 72
Pipeline value: 7,191,000.00 EUR
Annual productivity value: 2,858,611.20 EUR
Report: output/reports/transformation_report.txt
Project scores: output/reports/project_scores.csv
```

## Beispiele im Repository

Die Beispielausgaben sind bewusst versioniert, damit Recruiter das Ergebnis direkt auf GitHub prüfen können, ohne das Projekt lokal auszuführen:

- [Terminal-Mitschnitt](examples/terminal_output.txt)
- [Beispielreport](examples/transformation_report_sample.txt)

Der Terminal-Mitschnitt zeigt den Start des CLI und den Unit-Test-Lauf.

Tests ausführen:

```bash
python3 -m unittest
```

Deterministische Beispieldaten neu erzeugen:

```bash
python3 scripts/generate_sample_data.py
```

## Erzeugte Dateien

Beim Start mit `python3 main.py` entstehen:

```txt
output/reports/commercial_it.db
output/reports/transformation_report.txt
output/reports/project_scores.csv
```

Diese Dateien sind generiert und werden nicht versioniert. Ein versioniertes Beispiel für den Report liegt unter [examples/transformation_report_sample.txt](examples/transformation_report_sample.txt).

## Projektstruktur

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
│   └── recruiter_summary_de.md
├── examples/
│   ├── terminal_output.txt
│   └── transformation_report_sample.txt
├── scripts/
│   └── generate_sample_data.py
└── tests/
    └── test_analysis.py
```

## Datenqualität

Die Daten sind fiktiv und können sicher veröffentlicht werden. Sie werden mit einem festen Random Seed in `scripts/generate_sample_data.py` erzeugt, sodass der Beispieldatensatz reproduzierbar bleibt.

Die Daten sind so aufgebaut, dass sie realistische Commercial-IT- und Consulting-Szenarien abbilden:

- verschiedene Branchen und Regionen
- kundenspezifische Systemzahlen und Umsatzklassen
- Projektkategorien wie ERP & Data, Commercial IT, Sales Enablement und Process Digitization
- monatliche Service-KPIs über ein volles Jahr
- Workshop-Felder wie Stakeholder-Anzahl, Anforderungsklarheit und kommerzielle Dringlichkeit

## Wichtigste Ergebnisse

Der Textreport liefert:

- Portfolio-KPI-Zusammenfassung
- Verteilung der Handlungsempfehlungen
- Pipeline-Sicht nach Projektkategorie
- Top-Projektvorschläge
- Service-Risiko-Sicht
- Bewerbungsbezug zu Bosch und Fujitsu

Die CSV-Scoring-Tabelle eignet sich zusätzlich für eine Weiterverarbeitung in Excel oder Power-BI-ähnlichen Auswertungen.

## Bewerbungssatz

Als Bewerberprojekt habe ich einen Commercial IT Transformation Analyzer entwickelt. Das Python-Tool verarbeitet einen realistischen synthetischen Datensatz mit Kunden-, Projekt-, Workshop- und Servicedaten, speichert ihn in einer SQLite-Datenbank und berechnet Kennzahlen wie Projektwert, Marge, Amortisationszeit, Produktivitätsgewinn und SLA-Risiko. Daraus entstehen ein Textreport und eine CSV-Auswertung. Das Projekt verbindet Informatik, BWL, Datenanalyse, Prozessdigitalisierung und Sales-/Consulting-orientiertes Denken.

## Autor

Johannes Maboudou
