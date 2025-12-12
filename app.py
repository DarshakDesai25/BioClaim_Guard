import streamlit as st
import random
import time

# -----------------------------------------
# PAGE CONFIG (MUST BE FIRST)
# -----------------------------------------
st.set_page_config(
    page_title="BioClaim Guard",
    page_icon="🧬",
    layout="centered"
)

# -----------------------------------------
# GLOBAL BACKGROUND
# -----------------------------------------
st.markdown("""
<style>
html, body {
    background-color: #F8FAFC;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------------------
# MOCK BIOCLAIM ENGINE
# -----------------------------------------
def run_bioclaim_guard(claim_text):
    time.sleep(1.5)
    score = round(random.uniform(0.55, 0.95), 2)
    explanation = (
        "Based on patterns observed in peer-reviewed biomedical literature, this claim "
        "appears to have moderate to strong empirical support. Reported outcomes may vary "
        "depending on formulation, population, and experimental conditions."
    )
    citations = [
        {"source": "PubMed Review", "link": "https://pubmed.ncbi.nlm.nih.gov/"},
        {"source": "WHO Technical Brief", "link": "https://www.who.int/"}
    ]
    return score, explanation, citations

# -----------------------------------------
# HERO / LOGOTYPE
# -----------------------------------------
st.markdown("""
<div style="text-align:center; margin-top:25px;">
  <h1 style="
    font-size:52px;
    font-weight:900;
    background: linear-gradient(90deg, #2563EB, #06B6D4);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
    margin-bottom:6px;
  ">
    🧬 BioClaim Guard
  </h1>

  <p style="font-size:18px; color:#475569;">
    Truth-as-a-Service for Biomedical & Health Claims
  </p>

  <div style="margin-top:14px;">
    <span style="background:#E0F2FE; color:#0369A1; padding:6px 14px; border-radius:999px; margin:4px; display:inline-block;">🧠 AI-Assisted</span>
    <span style="background:#E0F2FE; color:#0369A1; padding:6px 14px; border-radius:999px; margin:4px; display:inline-block;">📚 Citation-Backed</span>
    <span style="background:#E0F2FE; color:#0369A1; padding:6px 14px; border-radius:999px; margin:4px; display:inline-block;">🔍 Transparent Scoring</span>
  </div>
</div>
""", unsafe_allow_html=True)

st.write("")
st.write(
    "BioClaim Guard helps **researchers, journalists, and biotech teams** rapidly assess "
    "the credibility of biomedical claims using AI-assisted literature analysis."
)

# -----------------------------------------
# CLAIM INPUT
# -----------------------------------------
st.markdown("### 📝 Enter a Claim")

claim_input = st.text_area(
    "",
    height=130,
    placeholder="Example: mRNA vaccines remain stable at refrigerated temperatures (2–8°C) for up to 30 days."
)

# -----------------------------------------
# VERIFY BUTTON
# -----------------------------------------
verify = st.button("🔍 Verify Claim", use_container_width=True)

if verify:
    if not claim_input.strip():
        st.error("Please enter a biomedical or health-related claim.")
    else:
        with st.spinner("Analyzing scientific evidence..."):
            score, explanation, citations = run_bioclaim_guard(claim_input)

        confidence = "High confidence support" if score >= 0.8 else "Moderate evidence support"
        color = "#16A34A" if score >= 0.8 else "#F59E0B"

        st.markdown(f"""
        <div style="
            background:white;
            padding:30px;
            border-radius:20px;
            box-shadow:0px 20px 40px rgba(15,23,42,0.1);
            margin-top:25px;
        ">
        <h3>📊 Credibility Assessment</h3>

        <div style="font-size:48px; font-weight:900; color:{color};">
            {int(score * 100)}%
        </div>

        <p><strong>{confidence}</strong></p>

        <hr style="margin:22px 0;"/>

        <h4>Explanation</h4>
        <p style="color:#334155;">{explanation}</p>

        <h4 style="margin-top:20px;">Supporting Sources</h4>
        """, unsafe_allow_html=True)

        for c in citations:
            st.markdown(
                f"""
                <div style="
                    background:#F1F5F9;
                    padding:12px;
                    border-radius:12px;
                    margin-bottom:8px;
                ">
                <strong>{c['source']}</strong><br>
                <a href="{c['link']}" target="_blank">View source</a>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("""
        <div style="
            background:#FFF7ED;
            border-left:6px solid #F97316;
            padding:16px;
            border-radius:14px;
            margin-top:20px;
            color:#7C2D12;
        ">
        ⚠️ <strong>Demo Notice:</strong><br>
        This version uses placeholder logic for demonstration. Production versions integrate
        live scientific literature retrieval and validation.
        </div>
        """, unsafe_allow_html=True)

# -----------------------------------------
# ETHICS
# -----------------------------------------
st.markdown("### 🛡️ Ethics & Transparency")
st.write(
    "BioClaim Guard is designed around **responsible AI principles**. "
    "We surface uncertainty, avoid fabricated citations, and encourage "
    "verification against original scientific sources."
)

# -----------------------------------------
# BRAND IDENTITY SYSTEM (EXPLICIT REQUIREMENT)
# -----------------------------------------
st.markdown("<hr style='margin:50px 0;'>", unsafe_allow_html=True)
st.markdown("## 🎨 Brand Identity System")

# LOGO
st.markdown("""
### Logo & Logotype
The BioClaim Guard logotype combines a DNA symbol with a clean wordmark to communicate
scientific credibility, protection, and trust.

<div style="font-size:36px; font-weight:900; margin:20px 0;">
🧬 BioClaim Guard
</div>

<em>Primary logotype · Compact wordmark · Monochrome-ready</em>
""", unsafe_allow_html=True)

# COLORS
st.markdown("""
### Color Palette
<div style="display:flex; gap:16px; flex-wrap:wrap; margin-top:10px;">

<div style="background:#0F172A; color:white; padding:16px; border-radius:12px;">
<strong>Navy</strong><br>#0F172A
</div>

<div style="background:#2563EB; color:white; padding:16px; border-radius:12px;">
<strong>Primary Blue</strong><br>#2563EB
</div>

<div style="background:#06B6D4; color:#083344; padding:16px; border-radius:12px;">
<strong>Cyan Accent</strong><br>#06B6D4
</div>

<div style="background:#F8FAFC; color:#0F172A; padding:16px; border-radius:12px; border:1px solid #E5E7EB;">
<strong>Background</strong><br>#F8FAFC
</div>

</div>
""", unsafe_allow_html=True)

# TYPOGRAPHY
st.markdown("""
### Typography
- **Primary Typeface:** Inter  
- **Fallback System Fonts:** -apple-system, BlinkMacSystemFont, sans-serif  
- **Usage:** Bold weights for headlines, regular weights for readable body text
""")

# IMAGERY
st.markdown("""
### Imagery Style
BioClaim Guard uses restrained, non-sensational scientific visuals.

- DNA and molecular motifs  
- Clean, UI-first layouts  
- Soft gradients and clinical whitespace  
- Avoids fear-based or exaggerated medical imagery
""")

# BRAND VOICE
st.markdown("""
### Brand Voice
- **Tone:** Calm, authoritative, transparent  
- **Personality:** Evidence-driven, ethical, supportive  
- **Language:** Avoids hype; emphasizes nuance and uncertainty
""")

# -----------------------------------------
# FOOTER
# -----------------------------------------
st.markdown("""
<div style="
    text-align:center;
    font-size:13px;
    color:#64748B;
    margin-top:50px;
">
© 2025 BioClaim Guard • Built with Streamlit<br>
Educational Demo for INFO7375 – Branding & AI
</div>
""", unsafe_allow_html=True)
