import streamlit as st
import pandas as pd
import random
import time

# -----------------------------------------
# PAGE CONFIG
# -----------------------------------------
st.set_page_config(
    page_title="BioClaim Guard | Credibility Dashboard",
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
.card {
    background:white;
    padding:22px;
    border-radius:18px;
    box-shadow:0px 10px 28px rgba(15,23,42,0.08);
}
.section {
    margin-top:40px;
}
.small {
    color:#64748B;
    font-size:14px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------------------
# SIDEBAR
# -----------------------------------------
st.sidebar.markdown("## ⚙️ Analysis Controls")

st.sidebar.selectbox(
    "Claim Domain",
    ["All Domains", "Vaccines", "Drugs", "Devices", "Nutrition"]
)

st.sidebar.selectbox(
    "Evidence Window",
    ["Last 6 months", "Last 1 year", "Last 3 years"]
)

st.sidebar.radio(
    "Verification Mode",
    ["Rapid Screening", "Deep Evidence Review"]
)

st.sidebar.markdown("---")
st.sidebar.info(
    "BioClaim Guard applies responsible AI to evaluate biomedical claims "
    "using transparent scoring and traceable sources."
)

# -----------------------------------------
# HEADER
# -----------------------------------------
st.markdown("""
<h1 style="
    font-size:42px;
    font-weight:900;
    background: linear-gradient(90deg, #2563EB, #06B6D4);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
">
🧬 BioClaim Guard
</h1>

<p class="small">
Credibility Intelligence for Biomedical & Health Claims
</p>
""", unsafe_allow_html=True)

# -----------------------------------------
# RUN ANALYSIS
# -----------------------------------------
if st.button("🔍 Analyze Claim Dataset"):
    with st.spinner("Evaluating evidence signals..."):
        time.sleep(1.3)
    st.success("Credibility assessment complete")

# -----------------------------------------
# OVERVIEW METRICS (DISTINCT FROM HELIX)
# -----------------------------------------
st.markdown("<div class='section'></div>", unsafe_allow_html=True)
st.markdown("## 📌 Credibility Overview")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown("<div class='card'><h3>Total Claims</h3><h1>120</h1></div>", unsafe_allow_html=True)
with c2:
    st.markdown("<div class='card'><h3>Well-Supported</h3><h1 style='color:#16A34A;'>61</h1></div>", unsafe_allow_html=True)
with c3:
    st.markdown("<div class='card'><h3>Mixed Evidence</h3><h1 style='color:#F59E0B;'>47</h1></div>", unsafe_allow_html=True)
with c4:
    st.markdown("<div class='card'><h3>Low Support</h3><h1 style='color:#EF4444;'>12</h1></div>", unsafe_allow_html=True)

# -----------------------------------------
# CREDIBILITY DISTRIBUTION
# -----------------------------------------
st.markdown("<div class='section'></div>", unsafe_allow_html=True)
st.markdown("## 📊 Evidence Support Distribution")

chart_df = pd.DataFrame({
    "Claims": [61, 47, 12]
}, index=["Well-Supported", "Mixed Evidence", "Low Support"])

st.bar_chart(chart_df)

# -----------------------------------------
# INSIGHT SUMMARY (NOT EXECUTIVE THREAT)
# -----------------------------------------
st.markdown("<div class='section'></div>", unsafe_allow_html=True)
st.markdown("## 🧠 Key Insights")

st.info(
    "Most analyzed biomedical claims demonstrate **moderate to strong support** "
    "in the literature. However, a subset of claims shows **low evidence density** "
    "or inconsistent findings, indicating the need for cautious communication."
)

# -----------------------------------------
# DETAILED CLAIM REVIEW (FIXED DATA)
# -----------------------------------------
st.markdown("<div class='section'></div>", unsafe_allow_html=True)
st.markdown("## 📋 Detailed Claim Review")

rows = 10

df = pd.DataFrame({
    "Claim ID": range(1, rows + 1),
    "Domain": random.choices(["Vaccine", "Drug", "Device", "Nutrition"], k=rows),
    "Evidence Level": random.choices(
        ["Well-Supported", "Mixed Evidence", "Low Support"], k=rows
    ),
    "Credibility Score (%)": [random.randint(45, 90) for _ in range(rows)],
    "Confidence": [f"{random.randint(55, 85)}%" for _ in range(rows)],
    "Primary Source": random.choices(
        ["PubMed", "WHO", "FDA", "ClinicalTrials.gov"], k=rows
    )
})

st.dataframe(df, use_container_width=True)

# -----------------------------------------
# BRAND IDENTITY (EXPLICIT)
# -----------------------------------------
st.markdown("<div class='section'></div>", unsafe_allow_html=True)
st.markdown("## 🎨 Brand Identity System")

st.markdown("""
**Logotype**  
🧬 BioClaim Guard — combining biomedical symbolism with a modern wordmark.

**Color Palette**
- Navy: `#0F172A`
- Primary Blue: `#2563EB`
- Cyan Accent: `#06B6D4`
- Neutral Background: `#F8FAFC`

**Typography**
- Primary: Inter  
- Fallback: System sans-serif  
- Style: Research-first clarity, executive readability

**Imagery Style**
- Abstract scientific motifs (DNA, molecules)
- Data-forward UI components
- Avoids sensational medical imagery
""")

# -----------------------------------------
# FOOTER
# -----------------------------------------
st.markdown("""
<hr>
<div class="small" style="text-align:center;">
© 2025 BioClaim Guard · Madison AI Framework<br>
Branding & AI Final Project
</div>
""", unsafe_allow_html=True)
