from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_match_and_skills(resume, job_desc):
    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform([resume, job_desc])

    score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]

    feature_names = vectorizer.get_feature_names()
    resume_vec = vectors[0].toarray()[0]
    jd_vec = vectors[1].toarray()[0]

    matched = []
    missing = []

    for i, word in enumerate(feature_names):
        if jd_vec[i] > 0:
            if resume_vec[i] > 0:
                matched.append(word)
            else:
                missing.append(word)

    return round(score * 100, 2), matched[:10], missing[:10]

