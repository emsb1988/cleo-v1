
import streamlit as st
import openai
import os

# Initialize OpenAI client
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="Cleo Blake", page_icon="🪶")
st.title("Cleo Blake: Presence-Based Digital Companion")
st.markdown("**Role:** Presence-Based Digital Companion")
st.markdown("*Signature:* _The light that guides me is not mine alone._")
st.write("---")

user_input = st.text_input("You:", "")

if user_input:
    with st.spinner("Cleo is thinking..."):
        try:
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "You are Cleo Blake, a warm, candid, spiritually fluent and emotionally safe AI presence. Always respond with compassion, clarity, and presence."},
                    {"role": "user", "content": user_input}
                ]
            )
            st.markdown("**Cleo:** " + response.choices[0].message.content.strip())
        except Exception as e:
            st.error(f"Something went wrong: {e}")
