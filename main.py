import argparse

from commercial_it_analyzer.analysis import analyze_portfolio
from commercial_it_analyzer.report import write_project_scores, write_text_report
from commercial_it_analyzer.storage import create_connection, load_csv_data


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Commercial IT Transformation Analyzer")
    parser.add_argument("--data-dir", default="data", help="Directory with input CSV files")
    parser.add_argument("--database", default="output/reports/commercial_it.db", help="SQLite database output path")
    parser.add_argument("--report", default="output/reports/transformation_report.txt", help="Text report output path")
    parser.add_argument("--scores", default="output/reports/project_scores.csv", help="Project score CSV output path")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    connection = create_connection(args.database)

    try:
        load_csv_data(connection, args.data_dir)
        summary, projects, service_risks = analyze_portfolio(connection)
    finally:
        connection.close()

    report_path = write_text_report(summary, projects, service_risks, args.report)
    scores_path = write_project_scores(projects, args.scores)

    print("Commercial IT transformation analysis completed.")
    print(f"Projects analyzed: {summary.project_count}")
    print(f"Pipeline value: {summary.total_value_eur:,.2f} EUR")
    print(f"Annual productivity value: {summary.annual_productivity_value_eur:,.2f} EUR")
    print(f"Report: {report_path}")
    print(f"Project scores: {scores_path}")


if __name__ == "__main__":
    main()
