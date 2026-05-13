import sqlite3
from dataclasses import dataclass


HOURLY_COST_EUR = 58


@dataclass(frozen=True)
class PortfolioSummary:
    project_count: int
    total_value_eur: float
    total_margin_eur: float
    average_margin_percent: float
    monthly_hours_saved: float
    annual_productivity_value_eur: float
    average_priority_score: float


def analyze_portfolio(connection: sqlite3.Connection) -> tuple[PortfolioSummary, list[dict], list[dict]]:
    project_rows = connection.execute(
        """
        SELECT
            p.project_id,
            p.project_name,
            p.category,
            p.phase,
            p.estimated_value_eur,
            p.estimated_cost_eur,
            p.manual_hours_per_month,
            p.automated_hours_per_month,
            p.implementation_weeks,
            p.consulting_fit,
            p.delivery_risk,
            c.name AS customer_name,
            c.industry,
            c.region,
            c.security_systems,
            c.strategic_priority,
            COALESCE(w.requirements_clarity, 3) AS requirements_clarity,
            COALESCE(w.customer_readiness, 3) AS customer_readiness,
            COALESCE(w.technical_complexity, 3) AS technical_complexity,
            COALESCE(w.commercial_urgency, 3) AS commercial_urgency
        FROM projects p
        JOIN customers c ON c.customer_id = p.customer_id
        LEFT JOIN workshops w ON w.project_id = p.project_id
        ORDER BY p.project_id
        """
    ).fetchall()

    service_rows = connection.execute(
        """
        SELECT
            c.customer_id,
            c.name AS customer_name,
            SUM(sm.service_tickets) AS service_tickets,
            SUM(sm.sla_breaches) AS sla_breaches,
            AVG(sm.average_resolution_hours) AS average_resolution_hours,
            SUM(sm.system_downtime_hours) AS annual_downtime_hours,
            AVG(sm.system_downtime_hours) AS average_monthly_downtime_hours
        FROM customers c
        JOIN service_metrics sm ON sm.customer_id = c.customer_id
        GROUP BY c.customer_id, c.name
        ORDER BY sla_breaches DESC, system_downtime_hours DESC
        """
    ).fetchall()

    projects = [_score_project(row) for row in project_rows]
    service_risks = [_score_service_risk(row) for row in service_rows]
    summary = _summarize(projects)
    return summary, projects, service_risks


def _score_project(row: sqlite3.Row) -> dict:
    value = float(row["estimated_value_eur"])
    cost = float(row["estimated_cost_eur"])
    margin = value - cost
    margin_percent = margin / value * 100 if value else 0
    hours_saved = float(row["manual_hours_per_month"]) - float(row["automated_hours_per_month"])
    annual_value = hours_saved * HOURLY_COST_EUR * 12
    payback_months = cost / (annual_value / 12) if annual_value else 0

    business_score = min(40, margin_percent * 0.45 + row["strategic_priority"] * 4)
    productivity_score = min(25, hours_saved / 4)
    consulting_score = row["consulting_fit"] * 4 + row["commercial_urgency"] * 2
    readiness_score = row["customer_readiness"] * 3 + row["requirements_clarity"] * 2
    risk_penalty = row["delivery_risk"] * 4 + row["technical_complexity"] * 2
    raw_score = business_score + productivity_score + consulting_score + readiness_score - risk_penalty
    priority_score = round(max(0, min(100, raw_score)), 1)

    if priority_score >= 90:
        recommendation = "Lead project"
    elif priority_score >= 75:
        recommendation = "Prepare proposal"
    elif priority_score >= 60:
        recommendation = "Run discovery workshop"
    else:
        recommendation = "Monitor backlog"

    return {
        "project_id": row["project_id"],
        "project_name": row["project_name"],
        "customer_name": row["customer_name"],
        "category": row["category"],
        "phase": row["phase"],
        "value_eur": value,
        "cost_eur": cost,
        "margin_eur": margin,
        "margin_percent": round(margin_percent, 1),
        "monthly_hours_saved": round(hours_saved, 1),
        "annual_productivity_value_eur": round(annual_value, 2),
        "payback_months": round(payback_months, 1),
        "priority_score": priority_score,
        "recommendation": recommendation,
    }


def _score_service_risk(row: sqlite3.Row) -> dict:
    tickets = int(row["service_tickets"])
    breaches = int(row["sla_breaches"])
    breach_rate = breaches / tickets * 100 if tickets else 0
    annual_downtime = float(row["annual_downtime_hours"])
    average_monthly_downtime = float(row["average_monthly_downtime_hours"])
    resolution = float(row["average_resolution_hours"])
    risk_score = round(breach_rate * 1.2 + average_monthly_downtime * 2.5 + resolution * 1.1, 1)

    if risk_score >= 65:
        action = "Immediate SLA improvement workshop"
    elif risk_score >= 45:
        action = "Prioritize monitoring report"
    else:
        action = "Keep in standard reporting"

    return {
        "customer_id": row["customer_id"],
        "customer_name": row["customer_name"],
        "service_tickets": tickets,
        "sla_breaches": breaches,
        "breach_rate_percent": round(breach_rate, 1),
        "average_resolution_hours": round(resolution, 1),
        "system_downtime_hours": round(annual_downtime, 1),
        "average_monthly_downtime_hours": round(average_monthly_downtime, 1),
        "risk_score": risk_score,
        "action": action,
    }


def _summarize(projects: list[dict]) -> PortfolioSummary:
    project_count = len(projects)
    total_value = sum(project["value_eur"] for project in projects)
    total_margin = sum(project["margin_eur"] for project in projects)
    total_hours_saved = sum(project["monthly_hours_saved"] for project in projects)
    total_productivity_value = sum(project["annual_productivity_value_eur"] for project in projects)
    average_margin = total_margin / total_value * 100 if total_value else 0
    average_score = sum(project["priority_score"] for project in projects) / project_count if project_count else 0

    return PortfolioSummary(
        project_count=project_count,
        total_value_eur=round(total_value, 2),
        total_margin_eur=round(total_margin, 2),
        average_margin_percent=round(average_margin, 1),
        monthly_hours_saved=round(total_hours_saved, 1),
        annual_productivity_value_eur=round(total_productivity_value, 2),
        average_priority_score=round(average_score, 1),
    )
