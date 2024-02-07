from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | John Ndelembi"
PAGE_ICON = ":wave:"
NAME = "John Ndelembi"
DESCRIPTION = """
Data Analyst, assisting enterprises by supporting data-driven decision-making.
"""
EMAIL = "williamjohnie61@gmail.com"
SOCIAL_MEDIA = {
    "Portfolio": "https://tome.app/fx-3c4/johns-portfolio-cllaidgc700wkoe5qqmitxx1q",
    "Twitter": "https://twitter.com/Johnwills171",
}
PROJECTS = {
    "🏆 Machine Learning model for predicting salaries based on variables": "https://tome.app/fx-3c4/johns-portfolio-cllaidgc700wkoe5qqmitxx1q",
     " Worked with Data analysis projects developing models and training them ": "Link to be posted later"
    }


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 16 months of expereince extracting actionable insights from data
- ✔️ Strong hands on experience and knowledge in Python,R and Stata
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas, matplotlib)
- 📊 Data Visulization: MS Excel, Python(matplotlib, seaborn)
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOBS
st.write("🚧", "**Data Analyst | Work from home**")
st.write("02/2023 - Present")
st.write(
    """
- ► Currently not in college therefore i perfom data analysis and build data science projects from home.
- ► Build a Machine Learning model for predicting salary of workers based on their experiences using Sci-kit lean library
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
       st.write(f"[{project}]({link})")
