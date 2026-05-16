def calculate_status(progress_percent, budget_used_percent, sla_breach_rate):
    if progress_percent < 50 or budget_used_percent > 110 or sla_breach_rate > 15:
        return "ROT"
    if progress_percent < 75 or budget_used_percent > 95 or sla_breach_rate > 8:
        return "GELB"
    return "GRÜN"


def calculate_project_score(progress_percent, budget_used_percent, sla_breach_rate):
    score = progress_percent - max(0, budget_used_percent - 90) - sla_breach_rate * 2
    return max(0, min(100, round(score, 1)))
