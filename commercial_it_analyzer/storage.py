import csv
import sqlite3
from pathlib import Path


SCHEMA = {
    "customers": """
        CREATE TABLE IF NOT EXISTS customers (
            customer_id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            industry TEXT NOT NULL,
            region TEXT NOT NULL,
            security_systems INTEGER NOT NULL,
            annual_revenue_eur REAL NOT NULL,
            strategic_priority INTEGER NOT NULL
        )
    """,
    "projects": """
        CREATE TABLE IF NOT EXISTS projects (
            project_id TEXT PRIMARY KEY,
            customer_id TEXT NOT NULL,
            project_name TEXT NOT NULL,
            category TEXT NOT NULL,
            phase TEXT NOT NULL,
            estimated_value_eur REAL NOT NULL,
            estimated_cost_eur REAL NOT NULL,
            manual_hours_per_month REAL NOT NULL,
            automated_hours_per_month REAL NOT NULL,
            implementation_weeks INTEGER NOT NULL,
            consulting_fit INTEGER NOT NULL,
            delivery_risk INTEGER NOT NULL,
            FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
        )
    """,
    "service_metrics": """
        CREATE TABLE IF NOT EXISTS service_metrics (
            metric_id TEXT PRIMARY KEY,
            customer_id TEXT NOT NULL,
            month TEXT NOT NULL,
            service_tickets INTEGER NOT NULL,
            sla_breaches INTEGER NOT NULL,
            average_resolution_hours REAL NOT NULL,
            system_downtime_hours REAL NOT NULL,
            FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
        )
    """,
    "workshops": """
        CREATE TABLE IF NOT EXISTS workshops (
            workshop_id TEXT PRIMARY KEY,
            project_id TEXT NOT NULL,
            stakeholders INTEGER NOT NULL,
            requirements_clarity INTEGER NOT NULL,
            customer_readiness INTEGER NOT NULL,
            technical_complexity INTEGER NOT NULL,
            commercial_urgency INTEGER NOT NULL,
            FOREIGN KEY(project_id) REFERENCES projects(project_id)
        )
    """,
}


TABLE_FILES = {
    "customers": "customers.csv",
    "projects": "projects.csv",
    "service_metrics": "service_metrics.csv",
    "workshops": "workshops.csv",
}


def create_connection(database_path: str) -> sqlite3.Connection:
    path = Path(database_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(path)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database(connection: sqlite3.Connection) -> None:
    for statement in SCHEMA.values():
        connection.execute(statement)
    connection.commit()


def load_csv_data(connection: sqlite3.Connection, data_dir: str) -> None:
    initialize_database(connection)
    for table, filename in TABLE_FILES.items():
        connection.execute(f"DELETE FROM {table}")
        rows = _read_csv(Path(data_dir) / filename)
        if rows:
            columns = rows[0].keys()
            placeholders = ", ".join(["?"] * len(columns))
            column_list = ", ".join(columns)
            values = [tuple(row[column] for column in columns) for row in rows]
            connection.executemany(
                f"INSERT INTO {table} ({column_list}) VALUES ({placeholders})",
                values,
            )
    connection.commit()


def _read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))

