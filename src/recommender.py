def generate_recommendations(missing_skills):
    tips = []

    for skill in missing_skills:
        if skill in ["dashboards", "visualization"]:
            tips.append("Add a dashboard project (Tableau, Power BI, or Streamlit).")

        elif skill in ["statistics", "machine"]:
            tips.append("Highlight statistics or machine learning coursework.")

        elif skill in ["business", "decisions"]:
            tips.append("Emphasize business impact and decision-making.")

        elif skill in ["cloud", "platforms"]:
            tips.append("Mention AWS, GCP, or Azure experience.")

    return list(set(tips))[:5]
