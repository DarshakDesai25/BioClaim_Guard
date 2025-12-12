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
    background:white;
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
# SIMULATION LOGIC (REACTIVE, DEMO-SAFE)
# =========================================================
def simulate_credibility(domain, mode):
    if domain == "Vaccines":
        well, mixed, low = 70, 35, 15
    elif domain == "Drugs":
        well, mixed, low = 55, 45, 20
    elif domain == "Medical Devices":
        well, mixed, low = 50, 40, 18
    elif domain == "Nutrition":
        well, mixed, low = 40, 50, 30
    else:
        well, mixed, low = 61, 47, 12

    if mode == "Deep Evidence Review":
        well += 5
        mixed -= 3
        low = max(low - 2, 0)

    return well, mixed, low

# =========================================================
# SIDEBAR — REVIEW CONTROLS
# =========================================================
st.sidebar.markdown("## ⚙️ Review Controls")

domain = st.sidebar.selectbox(
    "Claim Domain",
    ["All Domains", "Vaccines", "Drugs", "Medical Devices", "Nutrition"]
)

window = st.sidebar.selectbox(
    "Evidence Window",
    ["Last 6 months", "Last 1 year", "Last 3 years"]
)

mode = st.sidebar.radio(
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
# RUN REVIEW BUTTON (OPTIONAL)
# =========================================================
if st.button("🔍 Review Claim Dataset"):
    with st.spinner("Evaluating evidence patterns responsibly…"):
        time.sleep(1.2)
    st.success("Credibility review updated")

# =========================================================
# REACTIVE METRICS
# =========================================================
well, mixed, low = simulate_credibility(domain, mode)
total = well + mixed + low

st.markdown("<div class='section'></div>", unsafe_allow_html=True)
st.markdown("## 📌 Credibility Overview")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(
        f"<div class='card'><h4>Total Claims Reviewed</h4><div class='metric'>{total}</div></div>",
        unsafe_allow_html=True
    )

with c2:
    st.markdown(
        f"<div class='card'><h4>Well-Supported</h4><div class='metric' style='color:#16A34A;'>{well}</div></div>",
        unsafe_allow_html=True
    )

with c3:
    st.markdown(
        f"<div class='card'><h4>Mixed Evidence</h4><div class='metric' style='color:#F59E0B;'>{mixed}</div></div>",
        unsafe_allow_html=True
    )

with c4:
    st.markdown(
        f"<div class='card'><h4>Low Support</h4><div class='metric' style='color:#EF4444;'>{low}</div></div>",
        unsafe_allow_html=True
    )

# =========================================================
# CREDIBILITY TRAJECTORY (WORKING GRAPH)
# =========================================================
st.markdown("<div class='section'></div>", unsafe_allow_html=True)
st.markdown("## 🌊 Credibility Trajectory")

trajectory_df = pd.DataFrame(
    {
        "Well-Supported": [well * 0.6, well * 0.8, well],
        "Mixed Evidence": [mixed * 0.7, mixed * 0.9, mixed],
        "Low Support": [low * 0.8, low * 0.9, low],
    },
    index=["Initial Scan", "Context Review", "Final Assessment"]
)

st.line_chart(trajectory_df)

st.caption(
    "This trajectory illustrates how evidence confidence evolves across review stages. "
    "Values update dynamically based on domain and review depth."
)

# =========================================================
# INTERPRETIVE INSIGHTS
# =========================================================
st.markdown("<div class='section'></div>", unsafe_allow_html=True)
st.markdown("## 🧠 Interpretive Insights")

st.info(
    "Credibility is not static. Domains with mature research bases trend toward "
    "stronger support over deeper review, while heterogeneous domains maintain larger "
    "mixed-evidence regions."
)

# =========================================================
# DETAILED CLAIM REVIEW (STABLE TABLE)
# =========================================================
st.markdown("<div class='section'></div>", unsafe_allow_html=True)
st.markdown("## 📋 Detailed Claim Review")

rows = 10

df = pd.DataFrame({
    "Claim ID": range(1, rows + 1),
    "Domain": random.choices(
        ["Vaccine", "Drug", "Device", "Nutrition"], k=rows
    ),
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
# BIOCLAIM CREDIBILITY FRAMEWORK (BRAND IDENTITY)
# =========================================================
st.markdown("<div class='section'></div>", unsafe_allow_html=True)

st.markdown("""
<h2>🧬 The BioClaim Credibility Framework</h2>
<p class="small" style="max-width:820px;">
BioClaim Guard is intentionally designed as a reasoning workspace rather than a monitoring
or threat-detection dashboard. Its brand system reinforces trust, restraint, and clarity.
</p>
""", unsafe_allow_html=True)

col_a, col_b = st.columns(2)

with col_a:
    st.markdown("""
    <div class="card">
    <h3>Brand Expression</h3>
    <ul>
      <li><strong>Symbol:</strong> 🧬 DNA motif representing evidence</li>
      <li><strong>Voice:</strong> Calm, ethical, non-sensational</li>
      <li><strong>Positioning:</strong> Credibility over certainty</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

with col_b:
    st.markdown("""
    <div class="card">
    <h3>Visual System</h3>

    <div style="display:flex; gap:10px; margin-bottom:12px;">
      <div style="background:#0F172A; color:white; padding:10px; border-radius:8px;">Navy<br>#0F172A</div>
      <div style="background:#2563EB; color:white; padding:10px; border-radius:8px;">Blue<br>#2563EB</div>
      <div style="background:#06B6D4; color:#083344; padding:10px; border-radius:8px;">Cyan<br>#06B6D4</div>
    </div>

    <p><strong>Typography:</strong> Inter (system sans-serif)</p>
    <p class="small">Optimized for dense scientific and journalistic workflows.</p>
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
