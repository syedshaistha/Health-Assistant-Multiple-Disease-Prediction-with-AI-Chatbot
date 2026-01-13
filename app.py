# MediChat/app.py

import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from MediChat.src.prompt import system_prompt
from datetime import datetime
import os

from dotenv import load_dotenv
load_dotenv()

# ------------------ Paths ------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_FILE = os.path.join(BASE_DIR, "templates", "medichat.html")
CSS_FILE = os.path.join(BASE_DIR, "static", "style.css")


GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    st.error("GEMINI_API_KEY not found")
    st.stop()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
  # <-- normal hyphen
    temperature=0.5,
    google_api_key=st.secrets["GEMINI_API_KEY"],
    convert_system_message_to_human=True
)




# ------------------ Load HTML & CSS ------------------
def load_html_css():
    """Load HTML and inject CSS"""
    with open(CSS_FILE, "r", encoding="utf-8") as f:
        css_content = f.read()
    with open(HTML_FILE, "r", encoding="utf-8") as f:
        html_content = f.read()
    # Inject CSS into HTML
    html_with_css = html_content.replace(
        '<link rel="stylesheet" href="{{ url_for(\'static\', filename=\'style.css\') }}" />',
        f"<style>{css_content}</style>"
    )
    return html_with_css


# ------------------ Main App ------------------
def run_medichat():

    # --- Inject CSS for Streamlit-native components ---
    st.markdown("""
        <style>
            /* Button */
            .container, .container-fluid, .container-lg, .container-md, .container-sm, .container-xl, .container-xxl {
                padding: var(--bs-gutter-x, .75rem);
            }
        </style>
    """, unsafe_allow_html=True)



    # ✅ ALWAYS initialize session state inside the function
    st.session_state.setdefault("messages", [{
        "role": "bot",
        "content": "👋 Hello! I'm MediChat, your intelligent health assistant. How can I help you today?",
        "time": datetime.now().strftime("%H:%M"),
    }])
    st.session_state.setdefault("last_input", "")

    # Load HTML + CSS
    html_code = load_html_css()

    # Generate chat HTML
    chat_container_html = ""
    for msg in st.session_state["messages"]:
        role = msg["role"]
        content = msg["content"]
        time = msg["time"]

        if role == "user":
            chat_container_html += f"""
            <div class="message-user d-flex justify-content-end mb-4">
                <div class="message-content">
                    <p>{content}</p>
                    <span class="message-time">{time}</span>
                </div>
                <div class="avatar-container">
                    <img src="https://i.ibb.co/d5b84Xw/Untitled-design.png" class="user-avatar rounded-circle"/>
                </div>
            </div>
            """
        else:
            chat_container_html += f"""
            <div class="message-bot d-flex mb-4">
                <div class="avatar-container">
                    <img src="https://cdn-icons-png.flaticon.com/512/387/387569.png" class="bot-avatar rounded-circle"/>
                    <span class="online-status"></span>
                </div>
                <div class="message-content">
                    <p>{content}</p>
                    <span class="message-time">{time}</span>
                </div>
            </div>
            """

    full_html = html_code.replace("{{ chat_container }}", chat_container_html)

    # Render chat HTML
    st.components.v1.html(
        full_html,
        height=500,
        scrolling=True,
    )

    # --- Input section ---
    with st.form("chat_form", clear_on_submit=True):
        col1, col2 = st.columns([4, 1])
        with col1 : user_input = st.text_input(label="Your message:", placeholder="Your message", label_visibility="collapsed")  # 👈 hides the label above
        with col2 : submitted = st.form_submit_button("Send")

    if submitted and user_input:
        if user_input != st.session_state["last_input"]:
            st.session_state["last_input"] = user_input

            # Save user message
            st.session_state["messages"].append({
                "role": "user",
                "content": user_input,
                "time": datetime.now().strftime("%H:%M"),
            })

            # Get bot response
            try:
                response = llm.invoke(user_input)

                bot_reply = response.content if hasattr(response, "content") else str(response)

                #bot_reply = response.content if hasattr(response, "content") else str(response)
            except Exception as e:
                bot_reply = f"⚠️ Error: {str(e)}"

            st.session_state["messages"].append({
                "role": "bot",
                "content": bot_reply,
                "time": datetime.now().strftime("%H:%M"),
            })

            st.rerun()

# ------------------ Run ------------------
if __name__ == "__main__":
    run_medichat()