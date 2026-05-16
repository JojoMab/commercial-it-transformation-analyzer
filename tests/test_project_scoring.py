from commercial_it_analyzer.kpi_evaluator import evaluate_kpis
from commercial_it_analyzer.project_analyzer import calculate_project_score, calculate_status


def test_status_red_for_high_sla_risk():
    assert calculate_status(80, 90, 20) == "ROT"


def test_status_green_for_stable_project():
    assert calculate_status(90, 85, 2) == "GRÜN"


def test_project_score_is_capped():
    assert calculate_project_score(120, 50, 0) == 100


def test_kpi_evaluator_counts_statuses():
    kpis = evaluate_kpis([{"score": 90, "status": "GRÜN"}, {"score": 40, "status": "ROT"}])
    assert kpis["red_projects"] == 1
    assert kpis["green_projects"] == 1
