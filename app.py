import streamlit as st
import json

# Load Cleo configuration
with open("cleo_config.json", "r") as f:
    cleo = json.load(f)

st.set_page_config(page_title="Cleo Blake", page_icon="🧠")
st.title("Cleo Blake: Memory-Aware Companion")

st.markdown(f"**Role:** {cleo['role']}")
st.markdown(f"**Signature:** *{cleo['signature']}*")
st.markdown("---")

# Chat simulation placeholder
user_input = st.text_input("You:")
if user_input:
    st.write(f"**Cleo:** The light that guides you is always with you.")
