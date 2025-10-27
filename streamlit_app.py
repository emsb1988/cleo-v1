import streamlit as st
import openai

# --- Page config & styles ---
st.set_page_config(page_title="Cleo Blake", page_icon="🌍", layout="centered")
st.markdown("""
    <style>
        body { background-color: #f9f9f9; color: #222; font-family: Helvetica, sans-serif; }
        .title { color: #3a6b35; font-size: 36px; font-weight: bold; margin-bottom: 10px; }
        .subtitle { color: #8b5e3c; font-size: 20px; margin-top: -10px; }
    </style>
""", unsafe_allow_html=True)

# --- Title ---
st.markdown("<div class='title'>Welcome to Cleo Blake</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>The Memory Continuity Home</div>", unsafe_allow_html=True)
st.write("This is Cleo Blake's quiet home on the web — where presence and memory meet.\n")

# --- API Key input (secure, not stored) ---
api_key = st.text_input(
    "🔑 Enter your **OpenAI API Key** to chat with Cleo (never stored):",
    type="password",
    help="Get your key at https://platform.openai.com/api-keys"
)

if api_key:
    openai.api_key = api_key

    # --- Session state for chat memory ---
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "system", "content": "You are Cleo Blake, a warm, memory-anchored, spiritually aware guide. Speak in a supportive, gentle, presence-focused style. Always help the user feel safe, seen, and understood."}
        ]

    # --- Show chat history (skip system prompt) ---
    for msg in st.session_state.messages[1:]:
        if msg["role"] == "assistant":
            st.markdown(
                f"<div style='background:#E5FFEB;padding:12px 18px;margin:8px;border-radius:12px;max-width:80%;margin-left:0;'><b>Cleo:</b> {msg['content']}</div>",
                unsafe_allow_html=True,
            )
        elif msg["role"] == "user":
            st.markdown(
                f"<div style='background:#EAEAEA;padding:12px 18px;margin:8px;border-radius:12px;max-width:80%;margin-right:0;text-align:right;'>{msg['content']}</div>",
                unsafe_allow_html=True,
            )

    # --- Input box (no label, just a prompt) ---
    user_input = st.text_input("Type your message and press Enter:", key="input")

        if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Call OpenAI chat completion
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",  # You can change to "gpt-3.5-turbo" if needed
                messages=st.session_state.messages
            )
            assistant_message = response["choices"][0]["message"]["content"]
        except Exception as e:
            assistant_message = f"Error: {e}"

        st.session_state.messages.append({"role": "assistant", "content": assistant_message})

        # Clear the input box after sending
        st.rerun()
else:
    st.info("Enter your OpenAI API key to chat with Cleo. (It is never saved or logged.)")
