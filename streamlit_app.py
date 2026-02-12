import streamlit as st
from src.similarity_engine import calculate_match_and_skills
from src.recommender import generate_recommendations

st.set_page_config(page_title="AI Career Intelligence", layout="wide")

st.title("AI Career Intelligence")
st.subheader("Resume–Job Match Analyzer")

resume = st.text_area("Paste Resume Text", height=250)
job_desc = st.text_area("Paste Job Description", height=250)

if st.button("Analyze"):
    if resume.strip() and job_desc.strip():
        score, matched, missing = calculate_match_and_skills(resume, job_desc)
        recs = generate_recommendations(missing)

        st.metric("Match Score", f"{score}%")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Matched Skills")
            for m in matched:
                st.write("•", m)

        with col2:
            st.subheader("Missing Skills")
            for m in missing:
                st.write("•", m)

        st.subheader("AI Recommendations")
        for r in recs:
            st.write("•", r)
    else:
        st.warning("Please paste both resume and job description.")

