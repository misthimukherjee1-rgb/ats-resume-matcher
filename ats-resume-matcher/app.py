Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import re
from collections import Counter
import streamlit as st

STOPWORDS = {
    "a","an","the","and","or","but","if","then","else","to","of","in","on","for","with","as","by","at","from",
    "is","are","was","were","be","been","being","this","that","these","those","it","its","i","me","my","we","our",
    "you","your","they","their","he","she","his","her","can","will","should","could","would","may","might"
}

def tokenize(text: str) -> list[str]:
    text = text.lower()
    words = re.findall(r"[a-z0-9\+\#]+", text)
    return [w for w in words if w not in STOPWORDS and len(w) > 2]

def keyword_stats(resume_text: str, jd_text: str):
    r = tokenize(resume_text)
    j = tokenize(jd_text)

    rset, jset = set(r), set(j)
    common = sorted(rset & jset)
    missing = sorted(jset - rset)

    score = (len(common) / len(jset) * 100) if jset else 0.0
...     top_jd = Counter(j).most_common(15)
... 
...     return score, common, missing, top_jd
... 
... st.set_page_config(page_title="ATS Resume Matcher", page_icon="📄")
... 
... st.title("📄 ATS Resume Keyword Matcher")
... st.write("Compare your **Resume** vs a **Job Description** to get a keyword match score and missing terms.")
... 
... resume_text = st.text_area("Resume Text", height=220, placeholder="Paste your resume text here...")
... jd_text = st.text_area("Job Description Text", height=220, placeholder="Paste the job description here...")
... 
... c1, c2 = st.columns(2)
... analyze = c1.button("Analyze Match ✅")
... clear = c2.button("Clear 🔄")
... 
... if clear:
...     st.session_state.clear()
...     st.rerun()
... 
... if analyze:
...     if not resume_text.strip() or not jd_text.strip():
...         st.warning("Please paste both Resume and Job Description text.")
...     else:
...         score, common, missing, top_jd = keyword_stats(resume_text, jd_text)
... 
...         st.subheader("✅ Match Score")
...         st.metric("Keyword Match (%)", f"{score:.1f}%")
... 
...         st.subheader("🔍 Top Keywords in Job Description")
...         st.write([f"{w} ({c})" for w, c in top_jd])
... 
...         st.subheader("✅ Keywords Found in Resume")
...         st.write(common if common else "No common keywords found.")
... 
...         st.subheader("⚠️ Missing Keywords (Add only if true for you)")
