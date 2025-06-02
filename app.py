import streamlit as st
import requests
import json
from typing import Dict, Any
import time

# Import styling functions
from styles import apply_dark_theme, get_theme_colors, apply_custom_footer, SIDEBAR_EXAMPLES, CHAT_PLACEHOLDERS

# Page configuration
st.set_page_config(
    page_title="Hitesh Choudhary AI Persona",
    page_icon="👨‍🏫",
    layout="centered",  # Changed to centered for minimalistic look
    initial_sidebar_state="collapsed"
)

# API Configuration
API_BASE_URL = "https://persona-ai-bot.onrender.com"  
# API_BASE_URL = "http://localhost:8000"  

def check_api_health() -> bool:
    """Check if the FastAPI backend is running"""
    try:
        response = requests.get(f"{API_BASE_URL}/health", timeout=5)
        return response.status_code == 200
    except:
        return False

def send_chat_message(message: str, mode: str = "normal") -> Dict[str, Any]:
    """Send chat message to FastAPI backend"""
    try:
        payload = {
            "message": message,
            "mode": mode
        }
        response = requests.post(
            f"{API_BASE_URL}/chat",
            json=payload,
            timeout=30
        )
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"success": False, "error": str(e)}

def get_persona_info() -> Dict[str, Any]:
    """Get persona information"""
    try:
        response = requests.get(f"{API_BASE_URL}/persona-info", timeout=10)
        return response.json()
    except:
        return {}

# Initialize session state
if "api_connected" not in st.session_state:
    st.session_state.api_connected = False
if "message_sent" not in st.session_state:
    st.session_state.message_sent = False
if "current_input" not in st.session_state:
    st.session_state.current_input = ""

# Apply themes
apply_dark_theme()
apply_custom_footer()
colors = get_theme_colors()

# Header
st.markdown('<h1 class="main-header-reduced">👋 Talk to your coding mentor, Hitesh Sir🚀</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Empowering You to Code with Confidence ☕️💻 – Your Friendly AI Tech Mentor</p>', unsafe_allow_html=True)


# Check API connection with centered loading
if not st.session_state.api_connected:
    with st.spinner("Connecting..."):
        api_status = check_api_health()
        st.session_state.api_connected = api_status

if not st.session_state.api_connected:
    st.error("❌ Cannot connect to FastAPI backend. Please ensure the server is running on http://localhost:8000")
    st.info("Run: `uvicorn main:app --reload`")
    st.stop()

st.markdown("<br><br><br/>", unsafe_allow_html=True)  
# Chat interface
# st.markdown("💬 **Ask me anything about coding, career, or tech**")

# Current conversation container
current_chat_container = st.container()

# Chat input form
# Chat input form - Updated for inline button
with st.form(key="chat_form", clear_on_submit=True):
    # Single column layout - button will be positioned inside via CSS
    user_input = st.text_area(
        "Your question:",
        placeholder=CHAT_PLACEHOLDERS[0],
        value=st.session_state.current_input,
        key="user_message_input",
        height=100,
        label_visibility="collapsed"
    )
    
    # Submit button - will be positioned inside textarea via CSS
    send_button = st.form_submit_button("🚀 Send")

# with st.form(key="chat_form", clear_on_submit=True):
#     col1, col2 = st.columns([5, 1])
    
#     with col1:
#         user_input = st.text_area(
#             "Your question:",
#             placeholder=CHAT_PLACEHOLDERS[0],
#             value=st.session_state.current_input,
#             key="user_message_input",
#             height=100,
#             label_visibility="collapsed"
#         )
    
#     with col2:
#         st.markdown('<div class="button-spacer"></div>', unsafe_allow_html=True)
#         send_button = st.form_submit_button("🚀 Send", use_container_width=True)

# Process user input
if send_button and user_input.strip():
    st.session_state.current_input = ""
    
    # Display user message
    with current_chat_container:
        st.markdown(f"""
        <div class="chat-message user-message">
        <strong>😊 You:</strong> {user_input}
        </div>
        """, unsafe_allow_html=True)
    
    # Show centered loading and get response
    with st.spinner("Hitesh is thinking..."):
        response = send_chat_message(user_input, "normal")
        
        if response.get("success"):
            with current_chat_container:
                st.markdown(f"""
                <div class="chat-message hitesh-message">
                <strong>👨‍🏫 Hitesh:</strong> {response["response"]}
                </div>
                """, unsafe_allow_html=True)
        else:
            error_msg = response.get("detail", response.get("error", "Unknown error occurred"))
            with current_chat_container:
                st.markdown(f"""
                <div class="chat-message error-message">
                <strong>❌ Error:</strong> {error_msg}
                </div>
                """, unsafe_allow_html=True)

# Quick Examples Section - List Style
# st.markdown("""
# <div class="examples-container">
#     <h4 class="examples-header">💡 Quick Examples</h4>
# </div>
# """, unsafe_allow_html=True)

# Create two columns for examples
# col1, col2 = st.columns(2)

# for i, question in enumerate(SIDEBAR_EXAMPLES):
#     # Alternate between columns
#     current_col = col1 if i % 2 == 0 else col2
    
#     with current_col:
#         if st.button(
#             f"• {question}", 
#             key=f"example_{i}",
#             use_container_width=True,
#             help=f"Click to ask: {question}"
#         ):
#             st.session_state.current_input = question
#             st.session_state.message_sent = False
#             st.rerun()

# Footer
st.markdown("""
<div class="custom-footer">
    <p><strong>Chai aur Code</strong> - Learn step by step! ☕️💻</p>
</div>
""", unsafe_allow_html=True)