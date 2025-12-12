import streamlit as st
import pandas as pd
import random
import time
import matplotlib.pyplot as plt

# -----------------------------------------
# PAGE CONFIG
# -----------------------------------------
st.set_page_config(
    page_title="BioClaim Guard | Executive Dashboard",
    page_icon="🧬",
    layout="wide"
)

# -----------------------------------------
# GLOBAL STYLES
# -----------------------------------------
st.markdown("""
<style>
html, body {
    background-color: #F8FAFC;
}
.metric-card {
    background:white;
    padding:20px;
    border-radius:16px;
    box-shadow:0px 10px 30px rgba(15,23,42,0.08);
    text-align:center;
}
.section {
    margin-top:40px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------------------
# SIDEBAR CONFIGURATION
# -----------------------------------------
st.sidebar.markdown("## ⚙️ Analysis Configuration")

claim_type = st.sidebar.selectbox(
    "Claim Category",
    ["All Claims", "Vaccines", "Drugs", "Medical Devices", "Nutrition"]
)

time_range = st.sidebar.selectbox(
    "Time Range",
    ["Last 6 months", "Last 1 year", "Last 3 years"]
)

analysis_depth = st.sidebar.radio(
    "Analysis Depth",
    ["Quick Scan", "Deep Analysis"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 🧬 About BioClaim Guard")
st.sidebar.info(
    "BioClaim Guard is an AI-assisted credibility assessment tool for biomedical "
    "and health-related claims. Powered by Madison AI Framework."
)

# -----------------------------------------
# HEADER / LOGO
# -----------------------------------------
st.markdown("""
<h1 style="
    font-size:44px;
    font-weight:900;
    background: linear-gradient(90deg, #2563EB, #06B6D4);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
">
🧬 BioClaim Guard
</h1>

<p style="font-size:16px; color:#475569;">
Executive Credibility Intelligence Dashboard · Powered by Madison AI
</p>
""", unsafe_allow_html=True)

# -----------------------------------------
# RUN ANALYSIS
# -----------------------------------------
if st.button("🚀 Run Credibility Analysis"):
    with st.spinner("Analyzing biomedical claims..."):
        time.sleep(1.5)
    st.success("Analysis complete!")

# -----------------------------------------
# EXECUTIVE DASHBOARD METRICS
# -----------------------------------------
st.markdown("<div class='section'></div>", unsafe_allow_html=True)
st.markdown("## 📊 Executive Dashboard")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("<div class='metric-card'><h3>Total Claims</h3><h1>120</h1></div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='metric-card'><h3>High Risk</h3><h1 style='color:#EF4444;'>12</h1></div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div class='metric-card'><h3>Moderate</h3><h1 style='color:#F59E0B;'>47</h1></div>", unsafe_allow_html=True)

with col4:
    st.markdown("<div class='metric-card'><h3>Avg Confidence</h3><h1>61%</h1></div>", unsafe_allow_html=True)

# -----------------------------------------
# THREAT DISTRIBUTION CHART
# -----------------------------------------
st.markdown("<div class='section'></div>", unsafe_allow_html=True)
st.markdown("## 📈 Credibility Distribution")

labels = ["High Risk", "Moderate", "Low"]
values = [12, 47, 61]

fig, ax = plt.subplots()
ax.bar(labels, values)
ax.set_ylabel("Number of Claims")
ax.set_title("Claim Credibility Levels")

st.pyplot(fig)

# -----------------------------------------
# EXECUTIVE SUMMARY
# -----------------------------------------
st.markdown("<div class='section'></div>", unsafe_allow_html=True)
st.markdown("## 🧠 Executive Summary")

st.info(
    "BioClaim Guard analyzed **120 biomedical claims** across vaccines, drugs, "
    "medical devices, and nutrition. Analysis identified **12 high-risk claims** "
    "requiring immediate review, **47 moderately supported claims**, and **61 claims "
    "with strong evidence backing**. Average confidence score across the dataset is **61%**."
)

# -----------------------------------------
# DETAILED RESULTS TABLE
# -----------------------------------------
st.markdown("<div class='section'></div>", unsafe_allow_html=True)
st.markdown("## 📋 Detailed Claim Analysis")

data = {
    "Claim ID": range(1, 11),
    "Claim Category": random.choices(
        ["Vaccine", "Drug", "Device", "Nutrition"], k=10
    ),
    "Credibility Level": random.choices(
        ["High Risk", "Moderate", "Low"], k=10
    ),
    "Score (%)": [random.randint(45, 90) for _ in range(10)],
    "Confidence": ["55%", "60%", "65%", "70%", "75%", "80%", "85%", "60%", "68%", "72%"],
    "Source": ["PubMed", "WHO", "FDA", "ClinicalTrials.gov"] * 2
}

df = pd.DataFrame(data)

st.dataframe(df, use_container_width=True)

# -----------------------------------------
# BRAND IDENTITY SYSTEM (VISIBLE ON SITE)
# -----------------------------------------
st.markdown("<div class='section'></div>", unsafe_allow_html=True)
st.markdown("## 🎨 Brand Identity System")

st.markdown("""
### Logo & Logotype
🧬 **BioClaim Guard** — DNA icon + wordmark symbolizing protection, science, and trust.
""")

st.markdown("""
### Color Palette
- Navy: `#0F172A`
- Primary Blue: `#2563EB`
- Cyan Accent: `#06B6D4`
- Background: `#F8FAFC`
""")

st.markdown("""
### Typography
- **Primary:** Inter
- **Fallback:** System sans-serif
- **Style:** Clear hierarchy, readable, executive-friendly
""")

st.markdown("""
### Imagery Style
- Abstract biomedical motifs
- Clean dashboards and data visualization
- No fear-based medical imagery
""")

# -----------------------------------------
# FOOTER
# -----------------------------------------
st.markdown("""
<hr>
<div style="text-align:center; color:#64748B; font-size:13px;">
© 2025 BioClaim Guard · Madison AI Framework<br>
Final Exam Project – Branding & AI
</div>
""", unsafe_allow_html=True)
