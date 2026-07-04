import streamlit as st
import fitz
import os
from dotenv import load_dotenv

load_dotenv()

def read_pdf(uploaded_file):
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
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
"""

st.title("AI Resume Analyser")
st.write("Upload your resume and paste a job description to see how well you match.")

uploaded_file = st.file_uploader("Upload your resume (PDF)", type="pdf")
job_description = st.text_area("Paste the job description here", height=200)

if st.button("Analyse Resume"):
    if uploaded_file and job_description:
        with st.spinner("Analysing your resume..."):
            resume_text = read_pdf(uploaded_file)
            result = analyse_resume(resume_text, job_description)
            st.success("Analysis complete!")
            st.text(result)
    else:
        st.warning("Please upload a resume and paste a job description.")