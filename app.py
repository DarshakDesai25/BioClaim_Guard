# -----------------------------------------
# BIOCLAIM CREDIBILITY FRAMEWORK (UNIQUE)
# -----------------------------------------
st.markdown("<div class='section'></div>", unsafe_allow_html=True)

st.markdown("""
<h2>🧬 The BioClaim Credibility Framework</h2>
<p style="color:#64748B; max-width:780px;">
BioClaim Guard is not a threat-detection platform. It is a credibility workspace
designed to help humans reason responsibly about biomedical claims.
</p>
""", unsafe_allow_html=True)

col_a, col_b = st.columns([1, 1])

# ---- LEFT: BRAND LOGIC ----
with col_a:
    st.markdown("""
    <div class="card">
    <h3>Brand Expression</h3>

    <p style="color:#475569;">
    BioClaim Guard’s visual system prioritizes calm authority over alarmism.
    Every design choice reinforces trust, restraint, and scientific rigor.
    </p>

    <ul style="margin-top:12px;">
      <li><strong>Symbol:</strong> 🧬 DNA motif representing evidence and verification</li>
      <li><strong>Wordmark:</strong> Heavy-weight typography for clarity and confidence</li>
      <li><strong>Voice:</strong> Neutral, evidence-first, non-sensational</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# ---- RIGHT: VISUAL SYSTEM ----
with col_b:
    st.markdown("""
    <div class="card">
    <h3>Visual System</h3>

    <p><strong>Core Palette</strong></p>

    <div style="display:flex; gap:10px; margin-bottom:14px;">
      <div style="background:#0F172A; color:white; padding:10px; border-radius:8px;">Navy<br>#0F172A</div>
      <div style="background:#2563EB; color:white; padding:10px; border-radius:8px;">Blue<br>#2563EB</div>
      <div style="background:#06B6D4; color:#083344; padding:10px; border-radius:8px;">Cyan<br>#06B6D4</div>
    </div>

    <p><strong>Typography</strong></p>
    <p style="color:#475569;">
    Inter — chosen for legibility in dense scientific and journalistic workflows.
    </p>

    <p><strong>Imagery</strong></p>
    <p style="color:#475569;">
    Abstract molecular forms, data-first UI components, and generous whitespace.
    No fear-based medical visuals.
    </p>
    </div>
    """, unsafe_allow_html=True)
