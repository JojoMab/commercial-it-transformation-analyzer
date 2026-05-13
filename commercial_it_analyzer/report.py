import csv
from collections import Counter, defaultdict
from pathlib import Path

from commercial_it_analyzer.analysis import PortfolioSummary


def write_text_report(
    summary: PortfolioSummary,
    projects: list[dict],
    service_risks: list[dict],
    output_path: str,
) -> str:
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    ranked_projects = sorted(projects, key=lambda item: item["priority_score"], reverse=True)
    ranked_risks = sorted(service_risks, key=lambda item: item["risk_score"], reverse=True)
    recommendation_counts = Counter(project["recommendation"] for project in projects)
    service_action_counts = Counter(risk["action"] for risk in service_risks)
    category_summary = _summarize_categories(projects)

    lines = [
        "Commercial IT Transformation Report",
        "===================================",
        "",
        "Portfolio KPIs",
        "--------------",
        f"Projects analyzed: {summary.project_count}",
        f"Total pipeline value: {summary.total_value_eur:,.2f} EUR",
        f"Total expected margin: {summary.total_margin_eur:,.2f} EUR",
        f"Average margin: {summary.average_margin_percent:.1f}%",
        f"Monthly hours saved: {summary.monthly_hours_saved:.1f}",
        f"Annual productivity value: {summary.annual_productivity_value_eur:,.2f} EUR",
        f"Average priority score: {summary.average_priority_score:.1f}",
        "",
        "Recommendation Mix",
        "------------------",
        f"Lead project: {recommendation_counts['Lead project']}",
        f"Prepare proposal: {recommendation_counts['Prepare proposal']}",
        f"Run discovery workshop: {recommendation_counts['Run discovery workshop']}",
        f"Monitor backlog: {recommendation_counts['Monitor backlog']}",
        "",
        "Category Pipeline Summary",
        "-------------------------",
    ]

    for category, values in sorted(category_summary.items()):
        lines.append(
            f"{category}: {values['count']} projects | "
            f"value {values['value_eur']:,.2f} EUR | "
            f"avg. score {values['average_score']:.1f}"
        )

    lines.extend(
        [
            "",
            "Service Action Mix",
            "------------------",
            f"Immediate SLA improvement workshop: {service_action_counts['Immediate SLA improvement workshop']}",
            f"Prioritize monitoring report: {service_action_counts['Prioritize monitoring report']}",
            f"Keep in standard reporting: {service_action_counts['Keep in standard reporting']}",
            "",
        ]
    )

    lines.extend(
        [
        "Top Project Recommendations",
        "---------------------------",
        ]
    )

    for project in ranked_projects[:5]:
        lines.append(
            f"{project['project_id']} | {project['project_name']} | "
            f"{project['customer_name']} | Score {project['priority_score']} | "
            f"{project['recommendation']} | Payback {project['payback_months']} months"
        )

    lines.extend(["", "Service Risk View", "-----------------"])
    for risk in ranked_risks:
        lines.append(
            f"{risk['customer_name']} | Risk {risk['risk_score']} | "
            f"SLA breach rate {risk['breach_rate_percent']}% | "
            f"avg. monthly downtime {risk['average_monthly_downtime_hours']} h | {risk['action']}"
        )

    lines.extend(
        [
            "",
            "Application Relevance",
            "---------------------",
            "Bosch Building Technologies: shows Commercial IT, ERP/data thinking, productivity transparency and workflow digitization.",
            "Fujitsu Sales & Consulting: shows proposal prioritization, customer readiness, modernization potential and consulting-style recommendations.",
        ]
    )

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return str(path)


def write_project_scores(projects: list[dict], output_path: str) -> str:
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "project_id",
        "project_name",
        "customer_name",
        "category",
        "phase",
        "value_eur",
        "margin_eur",
        "margin_percent",
        "monthly_hours_saved",
        "annual_productivity_value_eur",
        "payback_months",
        "priority_score",
        "recommendation",
    ]
    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for project in sorted(projects, key=lambda item: item["priority_score"], reverse=True):
            writer.writerow({field: project[field] for field in fieldnames})
    return str(path)


def _summarize_categories(projects: list[dict]) -> dict[str, dict]:
    grouped = defaultdict(list)
    for project in projects:
        grouped[project["category"]].append(project)

    summary = {}
    for category, rows in grouped.items():
        summary[category] = {
            "count": len(rows),
            "value_eur": sum(row["value_eur"] for row in rows),
            "average_score": sum(row["priority_score"] for row in rows) / len(rows),
        }
    return summary
