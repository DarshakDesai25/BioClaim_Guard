import streamlit as st
import random

# -----------------------------------------
# PLACEHOLDER LOGIC
# -----------------------------------------

def run_bioclaim_guard(claim_text):
    score = round(random.uniform(0.55, 0.95), 2)
    explanation = (
        "Based on patterns in peer-reviewed biomedical literature, this claim appears "
        "moderately supported. Reported outcomes may vary depending on formulation, "
        "population demographics, and experimental design."
    )
    citations = [
        {"source": "PubMed Study A", "link": "https://pubmed.ncbi.nlm.nih.gov/"},
        {"source": "WHO Technical Brief", "link": "https://www.who.int/"},
    ]
    return score, explanation, citations


# -----------------------------------------
# PAGE CONFIG
# -----------------------------------------

st.set_page_config(
    page_title="BioClaim Guard",
    page_icon="🧬",
    layout="centered"
)

# -----------------------------------------
# GLOBAL STYLES
# -----------------------------------------

st.markdown("""
<style>
body {
    background-color: #f8fafc;
}
.hero {
    text-align: center;
    margin-top: 10px;
}
.hero-title {
    font-size: 48px;
    font-weight: 900;
    background: linear-gradient(90deg, #2563eb, #06b6d4);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.hero-subtitle {
    color: #475569;
    font-size: 18px;
    margin-top: 8px;
}
.badges span {
    display: inline-block;
    background: #e0f2fe;
    color: #0369a1;
    padding: 6px 12px;
    border-radius: 999px;
    font-size: 13px;
    margin: 6px 4px;
    font-weight: 600;
}
.section-title {
    font-size: 22px;
    font-weight: 700;
    color: #0f172a;
    margin-top: 40px;
}
.card {
    background: white;
    padding: 28px;
    border-radius: 18px;
    box-shadow: 0px 12px 30px rgba(15, 23, 42, 0.08);
    margin-top: 25px;
}
.score {
    font-size: 42px;
    font-weight: 800;
    color: #16a34a;
}
.source {
    background: #f1f5f9;
    padding: 12px;
    border-radius: 10px;
    margin-bottom: 8px;
}
.demo {
    background: #fff7ed;
    border-left: 6px solid #f97316;
    padding: 16px;
    border-radius: 12px;
    margin-top: 20px;
    color: #7c2d12;
}
.footer {
    text-align: center;
    font-size: 13px;
    color: #64748b;
    margin-top: 50px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------------------
# HERO
# -----------------------------------------

st.markdown("""
<div class="hero">
    <div class="hero-title">BioClaim Guard</div>
    <div class="hero-subtitle">
        Truth-as-a-Service for Biomedical & Health Claims
    </div>
    <div class="badges">
        <span>🧠 AI-Assisted</span>
        <span>📚 Citation-Backed</span>
        <span>🔍 Transparent Scoring</span>
    </div>
</div>
""", unsafe_allow_html=True)

st.write("")
st.write(
    "BioClaim Guard helps **researchers, journalists, and biotech teams** rapidly assess "
    "the credibility of biomedical statements using AI-assisted literature analysis."
)

# -----------------------------------------
# INPUT
# -----------------------------------------

st.markdown("<div class='section-title'>Enter a Claim</div>", unsafe_allow_html=True)

claim_input = st.text_area(
    "",
    height=130,
    placeholder="Example: mRNA vaccines remain stable at refrigerated temperatures (2–8°C) for up to 30 days."
)

# -----------------------------------------
# ACTION
# -----------------------------------------

verify_clicked = st.button("🔍 Verify Claim", use_container_width=True)

if verify_clicked:
    if not claim_input.strip():
        st.error("Please enter a biomedical or health-related claim.")
    else:
        with st.spinner("Analyzing peer-reviewed evidence…"):
            score, explanation, citations = run_bioclaim_guard(claim_input)

        # -----------------------------------------
        # RESULTS
        # -----------------------------------------

        st.markdown("<div class='card'>", unsafe_allow_html=True)

        st.subheader("Credibility Assessment")

        st.markdown(f"<div class='score'>{int(score * 100)}%</div>", unsafe_allow_html=True)
        st.progress(score)

        confidence_label = (
            "High confidence support"
            if score > 0.8 else
            "Moderate evidence support"
        )
        st.caption(f"Assessment: **{confidence_label}**")

        st.markdown("<div class='section-title'>Explanation</div>", unsafe_allow_html=True)
        st.write(explanation)

        st.markdown("<div class='section-title'>Supporting Sources</div>", unsafe_allow_html=True)
        for c in citations:
            st.markdown(
                f"<div class='source'><strong>{c['source']}</strong><br>"
                f"<a href='{c['link']}' target='_blank'>View Source</a></div>",
                unsafe_allow_html=True
            )

        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("""
        <div class="demo">
        ⚠️ <strong>Demo Notice:</strong>  
        This application uses placeholder scoring logic for demonstration purposes.  
        Production versions integrate live literature retrieval and citation validation.
        </div>
        """, unsafe_allow_html=True)

# -----------------------------------------
# ETHICS
# -----------------------------------------

st.markdown("<div class='section-title'>Ethics & Transparency</div>", unsafe_allow_html=True)
st.write(
    "BioClaim Guard is designed around **responsible AI principles**. "
    "We surface uncertainty, avoid fabricated citations, and encourage verification "
    "against original scientific sources."
)

# -----------------------------------------
# FOOTER
# -----------------------------------------

st.markdown("""
<div class="footer">
© 2025 BioClaim Guard • Built with Streamlit & Madison Framework<br>
Educational Demo for INFO7375 – Branding & AI
</div>
""", unsafe_allow_html=True)
