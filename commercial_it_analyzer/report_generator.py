def create_management_summary(projects, kpis):
    lines = [
        "Management Summary",
        "==================",
        "",
        f"Durchschnittlicher Score: {kpis['average_score']}",
        f"Rote Projekte: {kpis['red_projects']}",
        f"Grüne Projekte: {kpis['green_projects']}",
        "",
        "Projektstatus",
    ]
    for project in projects:
        lines.append(f"{project['name']}: {project['status']} (Score {project['score']})")
    return "
".join(lines)
