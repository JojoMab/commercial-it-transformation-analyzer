def evaluate_kpis(projects):
    if not projects:
        return {"average_score": 0, "red_projects": 0, "green_projects": 0}
    scores = [project["score"] for project in projects]
    return {
        "average_score": round(sum(scores) / len(scores), 2),
        "red_projects": sum(1 for project in projects if project["status"] == "ROT"),
        "green_projects": sum(1 for project in projects if project["status"] == "GRÜN"),
    }
