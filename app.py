import streamlit as st
import random

# -----------------------------------------
# SIMPLE PLACEHOLDER LOGIC FOR BIOCLAIM GUARD
# -----------------------------------------

def run_bioclaim_guard(claim_text):
    score = round(random.uniform(0.55, 0.95), 2)
    explanation = (
        "Based on available scientific literature patterns, this claim appears "
        "moderately supported. However, stability and effectiveness may vary by "
        "formulation, population, and experimental conditions."
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
# BRAND STYLING
# -----------------------------------------

st.markdown("""
<style>
body {
    background-color: #f7f9fc;
}
.hero-title {
    color: #12355B;
    font-weight: 900;
    font-size: 46px;
    margin-bottom: 0;
}
.hero-subtitle {
    color: #6b7280;
    font-size: 18px;
    margin-top: 5px;
}
.section-title {
    color: #12355B;
    font-size: 22px;
    font-weight: 700;
    margin-top: 30px;
}
.card {
    background-color: white;
    padding: 25px;
    border-radius: 14px;
    box-shadow: 0px 10px 30px rgba(18, 53, 91, 0.08);
    margin-top: 20px;
}
.footer {
    color: #6b7280;
    font-size: 13px;
    margin-top: 40px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------------------
# HERO SECTION
# -----------------------------------------

st.markdown("<div class='hero-title'>BioClaim Guard</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='hero-subtitle'>Truth-as-a-Service for biomedical and health claims</div>",
    unsafe_allow_html=True
)

st.write("")
st.write(
    "BioClaim Guard helps researchers, journalists, and biotech teams **verify biomedical claims** "
    "using AI-assisted literature analysis — returning a transparent **truth score with citations**."
)

# -----------------------------------------
# INPUT SECTION
# -----------------------------------------

st.markdown("<div class='section-title'>Enter a Claim</div>", unsafe_allow_html=True)

claim_input = st.text_area(
    "Paste a biomedical or health-related statement below",
    height=120,
    placeholder="Example: mRNA vaccines remain stable at refrigerated temperatures (2–8°C) for up to 30 days."
)

# -----------------------------------------
# ACTION BUTTON
# -----------------------------------------

if st.button("🔍 Verify Claim"):
    if not claim_input.strip():
        st.error("Please enter a claim before running verification.")
    else:
        with st.spinner("Analyzing scientific literature and evidence…"):
            score, explanation, citations = run_bioclaim_guard(claim_input)

        # -----------------------------------------
        # RESULTS CARD
        # -----------------------------------------

        st.markdown("<div class='card'>", unsafe_allow_html=True)

        st.subheader("📊 Credibility Assessment")

        st.progress(score)
        st.success(f"Truth Score: **{int(score * 100)}%**")

        st.markdown("<div class='section-title'>Explanation</div>", unsafe_allow_html=True)
        st.write(explanation)

        st.markdown("<div class='section-title'>Top Supporting Sources</div>", unsafe_allow_html=True)
        for c in citations:
            st.markdown(f"- **{c['source']}** — [View Source]({c['link']})")

        st.markdown("</div>", unsafe_allow_html=True)

        st.info(
            "⚠️ **Demo Notice:** This version uses placeholder logic for demonstration purposes. "
            "In production, BioClaim Guard integrates a full Madison AI pipeline with live literature retrieval."
        )

# -----------------------------------------
# TRUST & ETHICS SECTION
# -----------------------------------------

st.markdown("<div class='section-title'>Ethics & Transparency</div>", unsafe_allow_html=True)
st.write(
    "BioClaim Guard is designed with **responsible AI principles** in mind. "
    "We highlight uncertainty, avoid hallucinated citations, and encourage users "
    "to consult original scientific sources before making decisions."
)

# -----------------------------------------
# FOOTER
# -----------------------------------------

st.markdown("""
<div class='footer'>
© 2025 BioClaim Guard • Built with Streamlit & Madison Framework<br>
Educational demo for INFO7375 – Branding & AI
</div>
""", unsafe_allow_html=True)
 
