from recommender import generate_recommendations
from resume_parser import parse_resume
from jd_parser import parse_job_description
from similarity_engine import calculate_match_and_skills

print("Paste resume text. When done, type END on a new line and press Enter.")
lines = []
while True:
    line = input()
    if line.strip() == "END":
        break
    lines.append(line)
resume_text = "\n".join(lines)

print("\nPaste job description. When done, type END on a new line and press Enter.")
lines = []
while True:
    line = input()
    if line.strip() == "END":
        break
    lines.append(line)
jd_text = "\n".join(lines)

resume = parse_resume(resume_text)
job_desc = parse_job_description(jd_text)

score, matched, missing = calculate_match_and_skills(resume, job_desc)

print(f"\nResume–Job Match Score: {score}%")
print("\nMatched Skills:")
for m in matched:
    print("-", m)

print("\nMissing Skills:")
for m in missing:
    print("-", m)

recommendations = generate_recommendations(missing)

print("\nAI Recommendations:")
for r in recommendations:
    print("-", r)

