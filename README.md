
## Web App (Streamlit)

Run the interactive web app:

streamlit run app.py

Then open http://localhost:8501 in your browser.


# AI Career Intelligence (Resume–Job Matcher)

CLI tool that compares a resume and job description using NLP (TF-IDF + cosine similarity),
then prints a match score, matched skills, missing skills, and recommendations.

## Setup

### 1) Clone
git clone https://github.com/abhawsar70/ai-career-intelligence.git
cd ai-career-intelligence

### 2) Create venv + install
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

### 3) Run
python src/main.py

Paste resume text, then type END.
Paste job description text, then type END.

## Example Input
We are seeking a Data Analytics Intern with experience in Python, SQL, and dashboards.
END

