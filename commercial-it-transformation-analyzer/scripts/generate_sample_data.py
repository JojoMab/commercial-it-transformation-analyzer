import csv
import random
from pathlib import Path


SEED = 20260513
DATA_DIR = Path(__file__).resolve().parents[1] / "data"


CUSTOMERS = [
    ("C001", "Metro Campus Services", "Building Operations", "South", 58, 840000, 5),
    ("C002", "Helio Manufacturing", "Manufacturing", "West", 41, 690000, 4),
    ("C003", "Stuttgart Retail Group", "Retail", "South", 96, 1280000, 5),
    ("C004", "Northline Logistics", "Logistics", "North", 34, 540000, 3),
    ("C005", "Public Services Munich", "Public Sector", "South", 73, 980000, 4),
    ("C006", "Alpine Healthcare Network", "Healthcare", "South", 88, 1460000, 5),
    ("C007", "Rhine Office Properties", "Real Estate", "West", 52, 760000, 4),
    ("C008", "Central Rail Facilities", "Transportation", "Central", 67, 1120000, 5),
    ("C009", "Hanse Hotel Alliance", "Hospitality", "North", 39, 610000, 3),
    ("C010", "EduTech Campus Group", "Education", "East", 44, 520000, 4),
    ("C011", "DataPark Colocation", "Data Center", "West", 71, 1750000, 5),
    ("C012", "Bavaria Food Production", "Food Production", "South", 48, 720000, 3),
    ("C013", "GreenCity Utilities", "Energy & Utilities", "East", 64, 1190000, 5),
    ("C014", "Prime Shopping Centers", "Retail Real Estate", "West", 83, 1510000, 5),
    ("C015", "MediLab Diagnostics", "Life Sciences", "South", 37, 680000, 4),
    ("C016", "SecureBank Operations", "Financial Services", "Central", 57, 1380000, 5),
    ("C017", "AeroParts Systems", "Aerospace Supply", "North", 46, 790000, 4),
    ("C018", "Urban Mobility Services", "Transportation", "East", 69, 1030000, 4),
    ("C019", "Municipal Housing West", "Public Housing", "West", 61, 870000, 4),
    ("C020", "PharmaCold Logistics", "Healthcare Logistics", "Central", 43, 810000, 4),
    ("C021", "NordTech Electronics", "Electronics", "North", 55, 930000, 4),
    ("C022", "SmartFactory Dresden", "Manufacturing", "East", 78, 1320000, 5),
    ("C023", "Capital Event Venues", "Event & Venues", "Central", 36, 590000, 3),
    ("C024", "Airport Retail Services", "Airport Retail", "South", 92, 1440000, 5),
]


PROJECT_BLUEPRINTS = [
    ("Commercial IT", "Service Ticket KPI Reporting", 54000, 112000, 52, 132, 2, 4),
    ("Commercial IT", "SLA Performance Analytics", 62000, 148000, 63, 156, 3, 5),
    ("ERP & Data", "Spare Parts Master Data Cleanup", 38000, 92000, 41, 98, 2, 3),
    ("ERP & Data", "Contract Data Quality Review", 42000, 98000, 38, 88, 2, 4),
    ("Process Digitization", "Maintenance Workflow Automation", 68000, 176000, 74, 174, 3, 5),
    ("Process Digitization", "Field Service Planning Workflow", 57000, 142000, 58, 138, 2, 4),
    ("Sales Enablement", "Offer Calculation Automation", 32000, 86000, 31, 76, 2, 5),
    ("Sales Enablement", "Proposal Pipeline Scoring", 35000, 91000, 28, 72, 1, 5),
    ("Sales & Consulting", "Customer Readiness Assessment", 26000, 74000, 24, 64, 1, 5),
    ("Sales & Consulting", "Transformation Workshop Package", 30000, 82000, 27, 69, 1, 5),
]


MONTHS = [f"2026-{month:02d}" for month in range(1, 13)]


def main() -> None:
    random.seed(SEED)
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    customers = _build_customers()
    projects, workshops = _build_projects_and_workshops(customers)
    metrics = _build_service_metrics(customers)

    _write_csv(
        DATA_DIR / "customers.csv",
        ["customer_id", "name", "industry", "region", "security_systems", "annual_revenue_eur", "strategic_priority"],
        customers,
    )
    _write_csv(
        DATA_DIR / "projects.csv",
        [
            "project_id",
            "customer_id",
            "project_name",
            "category",
            "phase",
            "estimated_value_eur",
            "estimated_cost_eur",
            "manual_hours_per_month",
            "automated_hours_per_month",
            "implementation_weeks",
            "consulting_fit",
            "delivery_risk",
        ],
        projects,
    )
    _write_csv(
        DATA_DIR / "service_metrics.csv",
        [
            "metric_id",
            "customer_id",
            "month",
            "service_tickets",
            "sla_breaches",
            "average_resolution_hours",
            "system_downtime_hours",
        ],
        metrics,
    )
    _write_csv(
        DATA_DIR / "workshops.csv",
        [
            "workshop_id",
            "project_id",
            "stakeholders",
            "requirements_clarity",
            "customer_readiness",
            "technical_complexity",
            "commercial_urgency",
        ],
        workshops,
    )

    print(f"Generated {len(customers)} customers")
    print(f"Generated {len(projects)} projects")
    print(f"Generated {len(metrics)} monthly service metric rows")
    print(f"Generated {len(workshops)} workshop assessments")


def _build_customers() -> list[dict]:
    return [
        {
            "customer_id": customer_id,
            "name": name,
            "industry": industry,
            "region": region,
            "security_systems": security_systems,
            "annual_revenue_eur": annual_revenue_eur,
            "strategic_priority": strategic_priority,
        }
        for customer_id, name, industry, region, security_systems, annual_revenue_eur, strategic_priority in CUSTOMERS
    ]


def _build_projects_and_workshops(customers: list[dict]) -> tuple[list[dict], list[dict]]:
    phases = ["idea", "workshop", "proposal", "delivery"]
    projects = []
    workshops = []
    project_number = 1

    for customer in customers:
        blueprints = random.sample(PROJECT_BLUEPRINTS, 3)
        scale = 0.82 + customer["strategic_priority"] * 0.07 + customer["security_systems"] / 500

        for category, project_name, min_value, max_value, min_hours, max_hours, base_risk, base_fit in blueprints:
            value = _round_to_1000(random.randint(min_value, max_value) * scale)
            margin_ratio = random.uniform(0.42, 0.61) if category in {"Commercial IT", "Sales & Consulting"} else random.uniform(0.35, 0.54)
            cost = _round_to_1000(value * (1 - margin_ratio))
            manual_hours = round(random.uniform(min_hours, max_hours) * scale, 1)
            automation_ratio = random.uniform(0.30, 0.52)
            automated_hours = round(manual_hours * automation_ratio, 1)
            implementation_weeks = random.randint(6, 18) + max(0, base_risk - 2)
            risk = _clamp(base_risk + random.choice([-1, 0, 0, 1]), 1, 5)
            consulting_fit = _clamp(base_fit + random.choice([-1, 0, 0, 1]), 1, 5)
            phase = random.choices(phases, weights=[2, 3, 4, 2], k=1)[0]
            project_id = f"P{project_number:03d}"

            projects.append(
                {
                    "project_id": project_id,
                    "customer_id": customer["customer_id"],
                    "project_name": project_name,
                    "category": category,
                    "phase": phase,
                    "estimated_value_eur": int(value),
                    "estimated_cost_eur": int(cost),
                    "manual_hours_per_month": manual_hours,
                    "automated_hours_per_month": automated_hours,
                    "implementation_weeks": implementation_weeks,
                    "consulting_fit": consulting_fit,
                    "delivery_risk": risk,
                }
            )

            workshops.append(
                {
                    "workshop_id": f"W{project_number:03d}",
                    "project_id": project_id,
                    "stakeholders": random.randint(3, 10),
                    "requirements_clarity": _clamp(random.randint(2, 5) + (1 if phase in {"proposal", "delivery"} else 0), 1, 5),
                    "customer_readiness": _clamp(random.randint(2, 5) + (1 if customer["strategic_priority"] >= 5 else 0), 1, 5),
                    "technical_complexity": _clamp(risk + random.choice([-1, 0, 1]), 1, 5),
                    "commercial_urgency": _clamp(customer["strategic_priority"] + random.choice([-1, 0, 0, 1]), 1, 5),
                }
            )
            project_number += 1

    return projects, workshops


def _build_service_metrics(customers: list[dict]) -> list[dict]:
    metrics = []
    metric_number = 1

    for customer in customers:
        base_tickets = max(12, int(customer["security_systems"] * random.uniform(0.55, 0.95)))
        priority = customer["strategic_priority"]
        process_maturity = random.uniform(0.72, 1.18)

        for month_index, month in enumerate(MONTHS, start=1):
            seasonal_factor = 1.12 if month_index in {1, 2, 11, 12} else 0.94 if month_index in {7, 8} else 1.0
            tickets = max(8, int(base_tickets * seasonal_factor + random.randint(-6, 8)))
            breach_rate = max(0.03, min(0.22, (0.16 - priority * 0.018) * process_maturity + random.uniform(-0.025, 0.035)))
            breaches = max(0, round(tickets * breach_rate))
            average_resolution = round(random.uniform(12.5, 29.5) * process_maturity + breaches * 0.18, 1)
            downtime = round(random.uniform(2.0, 8.5) * process_maturity + breaches * random.uniform(0.35, 0.95), 1)

            metrics.append(
                {
                    "metric_id": f"M{metric_number:04d}",
                    "customer_id": customer["customer_id"],
                    "month": month,
                    "service_tickets": tickets,
                    "sla_breaches": breaches,
                    "average_resolution_hours": average_resolution,
                    "system_downtime_hours": downtime,
                }
            )
            metric_number += 1

    return metrics


def _write_csv(path: Path, fieldnames: list[str], rows: list[dict]) -> None:
    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def _round_to_1000(value: float) -> int:
    return int(round(value / 1000) * 1000)


def _clamp(value: int, minimum: int, maximum: int) -> int:
    return max(minimum, min(maximum, value))


if __name__ == "__main__":
    main()

