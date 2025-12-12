import streamlit as st
import random

# -----------------------------------------
# SIMPLE PLACEHOLDER LOGIC FOR BIOCLAIM GUARD
# (Replace with real Madison / LLM logic later)
# -----------------------------------------

def run_bioclaim_guard(claim_text):
    score = round(random.uniform(0.55, 0.95), 2)
    explanation = (
        "Based on patterns observed in peer-reviewed biomedical literature, "
        "this claim appears partially supported. Confidence varies depending "
        "on formulation, population, and experimental context. Further expert "
        "review is recommended before publication."
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
    page_title="BioClaim Guard — Biomedical Claim Verification",
    page_icon="🧬",
    layout="centered"
)

# -----------------------------------------
# GLOBAL BRAND STYLES
# -----------------------------------------

st.markdown("""
<style>
.main {
    background-color: #f7f9fc;
}
.hero-title {
    color: #12355B;
    font-weight: 900;
    font-size: 46px;
    margin-bottom: 0px;
}
.hero-subtitle {
    color: #6b7280;
    font-size: 18px;
    margin-top: 4px;
}
.section-title {
    color: #12355B;
    font-weight: 700;
    font-size: 24px;
    margin-top: 30px;
}
.callout {
    background-color: #ffffff;
    border-left: 6px solid #12355B;
    padding: 16px;
    border-radius: 6px;
    margin-top: 12px;
}
.footer {
    color: #6b7280;
    font-size: 14px;
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
    "<div class='hero-subtitle'>AI-powered verification for biomedical and health-related claims</div>",
    unsafe_allow_html=True
)

st.write("")
st.write(
    "BioClaim Guard helps researchers, journalists, and biotech teams **evaluate the credibility of biomedical claims** "
    "by analyzing patterns in trusted scientific literature and returning a transparent confidence score with citations."
)

st.markdown(
    "<div class='callout'><b>Use case:</b> Pre-publication review, scientific communication checks, health misinformation prevention.</div>",
    unsafe_allow_html=True
)

# -----------------------------------------
# TOOL SECTION
# -----------------------------------------

st.markdown("<div class='section-title'>Verify a Claim</div>", unsafe_allow_html=True)

st.write(
    "Paste a biomedical or health-related statement below. "
    "BioClaim Guard will return a confidence score, explanation, and example sources."
)

claim_input = st.text_area(
    "Enter a biomedical claim",
    height=130,
    placeholder="Example: mRNA vaccines remain stable at refrigerated temperatures (2–8°C) for up to 30 days."
)

# -----------------------------------------
# RUN VERIFICATION
# -----------------------------------------

if st.button("🔍 Verify Claim"):
    if not claim_input.strip():
        st.error("Please enter a claim before running verification.")
    else:
        with st.spinner("Analyzing scientific literature and evidence patterns…"):
            score, explanation, citations = run_bioclaim_guard(claim_input)

        # -----------------------------------------
        # RESULTS SECTION
        # -----------------------------------------

        st.markdown("<div class='section-title'>Results</div>", unsafe_allow_html=True)

        st.success(f"**Truth Score: {int(score * 100)}%**")

        st.subheader("Explanation")
        st.write(explanation)

        st.subheader("Representative Sources")
        for c in citations:
            st.markdown(f"- **{c['source']}** — [Open Source]({c['link']})")

        st.warning(
            "⚠️ **Academic Disclaimer**: This demo uses placeholder logic for presentation purposes. "
            "Scores are illustrative and should not replace expert review or regulatory evaluation."
        )

# -----------------------------------------
# FOOTER
# -----------------------------------------

st.markdown(
    "<div class='footer'>© 2025 BioClaim Guard · Madison AI Project · INFO7375 Branding & AI</div>",
    unsafe_allow_html=True
)
