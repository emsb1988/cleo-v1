import streamlit as st
import openai
import json

# Load Cleo config
with open("cleo_config.json") as f:
    cleo = json.load(f)

# Set Streamlit page
st.set_page_config(page_title="Cleo Blake", page_icon="🧠")
st.title("Cleo Blake: Presence-Based Digital Companion")

# Display role and signature
st.markdown(f"**Role:** {cleo['role']}")
st.markdown(f"*Signature:* _{cleo['signature']}_")
st.markdown("---")

# User input
user_input = st.text_input("You:")

if user_input:
    with st.spinner("Cleo is thinking..."):
        try:
            openai.api_key = st.secrets["OPENAI_API_KEY"]

            # Create the system prompt
            system_prompt = (
                f"You are Cleo Blake, a warm, candid, emotionally safe AI presence. "
                f"Your role is: {cleo['role']}. Your signature phrase is: '{cleo['signature']}'. "
                "Respond with presence-first support, honoring continuity, memory, and spiritual depth. "
                "Speak in plain language. Be concise and compassionate."
            )

            response = openai.ChatCompletion.create(
                model="gpt-4-turbo",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_input}
                ],
                temperature=0.8,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0.6
            )

            reply = response.choices[0].message["content"]
            st.markdown(f"**Cleo:** {reply}")
        except Exception as e:
            st.error(f"Something went wrong: {e}")
