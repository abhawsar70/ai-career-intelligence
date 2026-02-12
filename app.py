import nltk
nltk.download("punkt")
nltk.download("stopwords")



import streamlit as st
from src.similarity_engine import calculate_match_and_skills
from src.recommender import generate_recommendations

st.set_page_config(page_title="AI Career Intelligence", layout="centered")

st.title("AI Career Intelligence")
st.subheader("Resume–Job Match Analyzer")

resume = st.text_area("Paste your resume here", height=250)
job_desc = st.text_area("Paste the job description here", height=250)

if st.button("Analyze"):
    if not resume.strip() or not job_desc.strip():
        st.error("Please paste both resume and job description.")
    else:
        score, matched, missing = calculate_match_and_skills(resume, job_desc)
        recommendations = generate_recommendations(missing)

        st.metric("Match Score", f"{score:.2f}%")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Matched Skills")
            if matched:
                for skill in matched:
                    st.write("•", skill)
            else:
                st.write("None")

        with col2:
            st.subheader("Missing Skills")
            if missing:
                for skill in missing:
                    st.write("•", skill)
            else:
                st.write("None")

        st.subheader("AI Recommendations")
        if recommendations:
            for tip in recommendations:
                st.write("•", tip)
        else:
            st.write("No recommendations needed.")

