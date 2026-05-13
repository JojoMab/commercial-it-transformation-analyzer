import tempfile
import unittest
from pathlib import Path

from commercial_it_analyzer.analysis import analyze_portfolio
from commercial_it_analyzer.storage import create_connection, load_csv_data


class PortfolioAnalysisTest(unittest.TestCase):
    def test_realistic_sample_portfolio_metrics(self):
        with tempfile.TemporaryDirectory() as temporary_dir:
            database_path = Path(temporary_dir) / "commercial_it.db"
            connection = create_connection(str(database_path))

            try:
                load_csv_data(connection, "data")
                summary, projects, service_risks = analyze_portfolio(connection)
                table_counts = {
                    table: connection.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
                    for table in ("customers", "projects", "service_metrics", "workshops")
                }
            finally:
                connection.close()

        self.assertEqual(table_counts["customers"], 24)
        self.assertEqual(table_counts["projects"], 72)
        self.assertEqual(table_counts["service_metrics"], 288)
        self.assertEqual(table_counts["workshops"], 72)
        self.assertEqual(summary.project_count, 72)
        self.assertEqual(summary.total_value_eur, 7191000.0)
        self.assertEqual(summary.monthly_hours_saved, 4107.2)
        self.assertEqual(summary.annual_productivity_value_eur, 2858611.2)
        self.assertEqual(projects[0]["project_id"], "P001")
        self.assertEqual(max(project["priority_score"] for project in projects), 100)
        self.assertEqual(len(service_risks), 24)
        self.assertIn("Monitor backlog", {project["recommendation"] for project in projects})
        self.assertGreater(max(risk["risk_score"] for risk in service_risks), 65)


if __name__ == "__main__":
    unittest.main()
