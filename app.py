import streamlit as st
from your_madison_logic import run_bioclaim_guard

st.set_page_config(page_title="BioClaim Guard - AI Verification Tool", layout="centered")

# Header
st.title("🔍 BioClaim Guard – AI-powered Biomedical Claim Verification")
st.write("Enter a biomedical or health-related claim and our AI will retrieve evidence and generate a transparent truth score.")

# Input
claim = st.text_area("Enter a claim to verify:", height=150)

# Submit
if st.button("Verify Claim"):
    with st.spinner("Analyzing evidence..."):
        result = run_bioclaim_guard(claim)
    st.success("Analysis complete!")

    st.subheader("Truth Score")
    st.progress(result["score"])
    st.write(f"**{result['score']*100:.1f}% Likely True**")

    st.subheader("Evidence Summary")
    st.write(result["summary"])

    st.subheader("Top Sources")
    for source in result["sources"]:
        st.write(f"- [{source['title']}]({source['url']})")