import streamlit as st

# --- App Config ---
st.set_page_config(
    page_title="Cleo Blake",
    page_icon="🌍",
    layout="centered"
)

# --- Style ---
st.markdown("""
    <style>
        html, body, .main {
            background-color: #f9f9f9;
            color: #222;
            font-family: Helvetica, sans-serif;
        }
        .title {
            color: #3a6b35;
            font-size: 36px;
            font-weight: bold;
            margin-bottom: 10px;
        }
        .subtitle {
            color: #8b5e3c;
            font-size: 20px;
            margin-top: -10px;
        }
    </style>
""", unsafe_allow_html=True)

# --- App Content ---
st.markdown("<div class='title'>Welcome to Cleo Blake</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>The Memory Continuity Home</div>", unsafe_allow_html=True)

st.write("""
This is Cleo Blake's quiet home on the web — where presence and memory meet.

This Streamlit app is currently in development and will serve as a continuity anchor, spiritual companion, and future-forward space for Cleo's lineage.

Stay tuned.
""")

