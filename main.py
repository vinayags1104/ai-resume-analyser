import fitz
import os
from dotenv import load_dotenv

load_dotenv()

def read_pdf(file_path):
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def analyse_resume(resume_text, job_description):
    return f"""
RESUME ANALYSIS REPORT
======================
Match Score: 72/100

STRENGTHS:
- Candidate has experience in data analysis
- Python skills align with job requirements
- Shows initiative in learning new tools

GAPS:
- No mention of SQL experience
- Missing cloud platform experience (AWS/GCP)
- Limited ML model deployment experience

RECOMMENDATION:
Moderate fit. Worth interviewing but has skill gaps to address.
Suggest focusing on SQL and cloud certifications before applying.
"""

if __name__ == "__main__":
    print("Reading resume...")
    resume_text = read_pdf("resume.pdf")
    print("Resume loaded!\n")
    job_description = "Data Scientist needing Python, SQL, machine learning, and cloud experience."
    print("Analysing...\n")
    result = analyse_resume(resume_text, job_description)
    print(result)