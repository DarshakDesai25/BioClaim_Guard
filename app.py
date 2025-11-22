import streamlit as st
import random

# -----------------------------------------
# SIMPLE PLACEHOLDER LOGIC FOR BIOCLAIM GUARD
# (Replace with real LLM logic later)
# -----------------------------------------

def run_bioclaim_guard(claim_text):
    # Fake scores for now — avoids errors
    score = round(random.uniform(0.55, 0.95), 2)
    explanation = (
        "Based on similar scientific literature, this claim appears moderately supported. "
        "Further validation recommended for precise scientific reporting."
    )
    citations = [
        {"source": "PubMed Study A", "link": "https://pubmed.ncbi.nlm.nih.gov/"}, 
        {"source": "WHO Technical Brief", "link": "https://www.who.int/"},
    ]
    return score, explanation, citations


# -----------------------------------------
# STREAMLIT UI
# -----------------------------------------

st.set_page_config(
    page_title="BioClaim Guard",
    page_icon="🧬",
    layout="centered"
)

# Brand styling
st.markdown("""
    <style>
    .main {
        background-color: #f7f9fc;
    }
    .title-text {
        color: #12355B;
        font-weight: 900;
        font-size: 42px;
    }
    .subtitle-text {
        color: #6b7280;
        font-size: 18px;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------
# HEADER SECTION
# -----------------------------------------

st.markdown("<div class='title-text'>BioClaim Guard</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle-text'>AI-powered biomedical claim verification</div>", unsafe_allow_html=True)
st.write("")

st.write("Paste a biomedical or health-related claim below. BioClaim Guard will analyze it and return a truth score + citations.")

# -----------------------------------------
# INPUT
# -----------------------------------------

claim_input = st.text_area("Enter your claim", height=120)

if st.button("Verify Claim"):
    if not claim_input.strip():
        st.error("Please enter a claim before running verification.")
    else:
        with st.spinner("Analyzing scientific literature…"):
            score, explanation, citations = run_bioclaim_guard(claim_input)

        # -----------------------------------------
        # OUTPUT
        # -----------------------------------------

        st.success(f"Truth Score: **{int(score*100)}%**")

        st.subheader("Explanation")
        st.write(explanation)

        st.subheader("Top Citations")
        for c in citations:
            st.markdown(f"- **{c['source']}** — [Open Source]({c['link']})")

        st.info("⚠️ Note: This is a demo version using placeholder logic. Full Madison pipeline can be integrated here later.")

