# =========================================================
# IMPORTS (MUST BE FIRST)
# =========================================================
import streamlit as st
import pandas as pd
import random
import time

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="BioClaim Guard | Credibility Review Workspace",
    page_icon="🧬",
    layout="wide"
)

# =========================================================
# GLOBAL STYLES
# =========================================================
st.markdown("""
<style>
html, body {
    background-color: #F8FAFC;
}
.section {
    margin-top:48px;
}
.card {
    background: white;
    padding:24px;
    border-radius:18px;
    box-shadow:0px 10px 28px rgba(15,23,42,0.08);
}
.small {
    color:#64748B;
    font-size:14px;
}
.metric {
    font-size:40px;
    font-weight:900;
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR — ANALYSIS CONTROLS
# =========================================================
st.sidebar.markdown("## ⚙️ Review Controls")

st.sidebar.selectbox(
    "Claim Domain",
    ["All Domains", "Vaccines", "Drugs", "Medical Devices", "Nutrition"]
)

st.sidebar.selectbox(
    "Evidence Window",
    ["Last 6 months", "Last 1 year", "Last 3 years"]
)

st.sidebar.radio(
    "Review Mode",
    ["Rapid Screening", "Deep Evidence Review"]
)

st.sidebar.markdown("---")
st.sidebar.info(
    "BioClaim Guard is a credibility review workspace designed to support "
    "responsible reasoning about biomedical and health-related claims."
)

# =========================================================
# HEADER / LOGOTYPE
# =========================================================
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

<p class="small">
A Credibility Review Workspace for Biomedical & Health Claims
</p>
""", unsafe_allow_html=True)

# =========================================================
# RUN ANALYSIS
# =========================================================
if st.button("🔍 Review Claim Dataset"):
    with st.spinner("Evaluating evidence signals responsibly..."):
        time.sleep(1.4)
    st.success("Credibility review complete")

# =========================================================
# OVERVIEW METRICS
# =========================================================
st.markdown("<div class='section'></div>", unsafe_allow_html=True)
st.markdown("## 📌 Credibility Overview")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown("<div class='card'><h4>Total Claims Reviewed</h4><div class='metric'>120</div></div>", unsafe_allow_html=True)

with c2:
    st.markdown("<div class='card'><h4>Well-Supported</h4><div class='metric' style='color:#16A34A;'>61</div></div>", unsafe_allow_html=True)

with c3:
    st.markdown("<div class='card'><h4>Mixed Evidence</h4><div class='metric' style='color:#F59E0B;'>47</div></div>", unsafe_allow_html=True)

with c4:
    st.markdown("<div class='card'><h4>Low Support</h4><div class='metric' style='color:#EF4444;'>12</div></div>", unsafe_allow_html=True)

# =========================================================
# EVIDENCE DISTRIBUTION
# =========================================================
st.markdown("<div class='section'></div>", unsafe_allow_html=True)
st.markdown("## 📊 Evidence Support Distribution")

chart_df = pd.DataFrame(
    {"Claims": [61, 47, 12]},
    index=["Well-Supported", "Mixed Evidence", "Low Support"]
)

st.bar_chart(chart_df)

# =========================================================
# INTERPRETIVE INSIGHTS
# =========================================================
st.markdown("<div class='section'></div>", unsafe_allow_html=True)
st.markdown("## 🧠 Interpretive Insights")

st.info(
    "The majority of reviewed biomedical claims demonstrate **moderate to strong support** "
    "within existing literature. A smaller subset shows **low or inconsistent evidence**, "
    "indicating areas where cautious communication and further review are warranted."
)

# =========================================================
# DETAILED CLAIM REVIEW (ERROR-FREE)
# =========================================================
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

# =========================================================
# BIOCLAIM CREDIBILITY FRAMEWORK (UNIQUE BRAND SYSTEM)
# =========================================================
st.markdown("<div class='section'></div>", unsafe_allow_html=True)

st.markdown("""
<h2>🧬 The BioClaim Credibility Framework</h2>
<p class="small" style="max-width:800px;">
BioClaim Guard is designed as a reasoning workspace rather than a monitoring dashboard.
Its identity system reinforces trust, restraint, and scientific clarity.
</p>
""", unsafe_allow_html=True)

col_a, col_b = st.columns(2)

with col_a:
    st.markdown("""
    <div class="card">
    <h3>Brand Expression</h3>
    <p class="small">
    BioClaim Guard communicates calm authority. The brand avoids alarmism and emphasizes
    transparency, uncertainty, and evidence-based reasoning.
    </p>
    <ul>
      <li><strong>Symbol:</strong> 🧬 DNA motif representing evidence</li>
      <li><strong>Wordmark:</strong> Bold typography for clarity</li>
      <li><strong>Voice:</strong> Neutral, ethical, non-sensational</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

with col_b:
    st.markdown("""
    <div class="card">
    <h3>Visual System</h3>

    <strong>Core Colors</strong>
    <div style="display:flex; gap:10px; margin:12px 0;">
      <div style="background:#0F172A; color:white; padding:10px; border-radius:8px;">Navy<br>#0F172A</div>
      <div style="background:#2563EB; color:white; padding:10px; border-radius:8px;">Blue<br>#2563EB</div>
      <div style="background:#06B6D4; color:#083344; padding:10px; border-radius:8px;">Cyan<br>#06B6D4</div>
    </div>

    <p><strong>Typography:</strong> Inter (system fallback sans-serif)</p>
    <p class="small">
    Optimized for readability in dense scientific and journalistic workflows.
    </p>

    <p><strong>Imagery:</strong> Abstract molecular forms, data-forward UI, generous whitespace.</p>
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# FOOTER
# =========================================================
st.markdown("""
<hr>
<div class="small" style="text-align:center;">
© 2025 BioClaim Guard · Madison AI Framework<br>
Branding & AI — Final Exam Project
</div>
""", unsafe_allow_html=True)
