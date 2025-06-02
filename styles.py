"""
Streamlit styling and theme configurations for Hitesh Choudhary AI Persona - Minimalistic Version
"""

import streamlit as st

def apply_dark_theme():
    """Apply minimalistic dark theme with centered elements"""
    st.markdown("""
    <style>
        /* ========================================
           DARK MODE - MINIMALISTIC DESIGN
        ======================================== */
        
        /* Main App Container */
        .stApp {
            background-color: #0e1117 !important;
            color: #fafafa !important;
            margin : 0 !important!
        }
        
        /* Top Menu Bar */
        .stApp > header {
            background-color: #0e1117 !important;
            color: #fafafa !important;
        }
        
        /* Main Content Area - Centered and Clean */
        .main .block-container {
            background-color: #0e1117 !important;
            color: #fafafa !important;
            padding-top: 0rem !important;
            max-width: 100% !important;  
            width: auto !important;
            padding-left: 2rem !important;
            padding-right: 2rem !important;
            margin: 0 auto !important;
        }
        
        /* Hide Sidebar Completely */
        section[data-testid="stSidebar"] {
            display: none !important;
        }
        
        /* Global Text Elements */
        .stApp, .stApp * {
            color: #fafafa !important;
        }
        
        /* ========================================
           CENTERED LOADING SPINNER
        ======================================== */
        
        /* Center the spinner container */
        .stSpinner {
            display: flex !important;
            justify-content: center !important;
            align-items: center !important;
            text-align: center !important;
            margin: 2rem auto !important;
        }
        
        /* Spinner text styling */
        .stSpinner > div {
            color: #FF6B35 !important;
            text-align: center !important;
        }
        
        /* Loading text positioning */
        .stSpinner .stText {
            text-align: center !important;
            margin-top: 1rem !important;
        }
        
        /* ========================================
           MINIMALISTIC HEADER STYLES
        ======================================== */
        
        .main-header-reduced {
            text-align: center;
            color: #FF6B35 !important;
            font-size: 2.2rem;
            font-weight: 600;
            margin-bottom: 0.5rem !important;
            margin-top: 0rem !important;
            padding-top: 0rem !important;
            letter-spacing: -0.5px;
            width: 100% !important;
            max-width: none !important;  
            word-spacing: 3px !important;
        }
        
        .sub-header {
            text-align: center;
            color: #888 !important;
            font-size: 1rem;
            margin-bottom: 2rem;
            font-weight: 400;
        }
        
        /* ========================================
           CHAT MESSAGE STYLING - MINIMALISTIC
        ======================================== */
        
        .chat-message {
            padding: 1.2rem;
            margin: 1rem 0;
            border-radius: 8px;
            background-color: #1a1d23 !important;
            border: 1px solid #262b36;
            transition: all 0.2s ease;
        }
        
        .user-message {
            background-color: #1a1d23 !important;
            border-left: 3px solid #4FC3F7;
            color: #fafafa !important;
        }
        
        .hitesh-message {
            background-color: #1a1d23 !important;
            border-left: 3px solid #FF6B35;
            color: #fafafa !important;
        }
        
        .error-message {
            background-color: #2d1a1a !important;
            border-left: 3px solid #f44336;
            color: #ff9999 !important;
        }
        
        /* ========================================
           COMPREHENSIVE TEXTAREA DARK STYLING - FIXED
        ======================================== */
        
        /* Target all possible textarea selectors with higher specificity */
        .stTextArea textarea,
        .stTextArea > div > div > textarea,
        .stTextArea div[data-baseweb="textarea"] textarea,
        div[data-testid="stTextArea"] textarea,
        div[data-testid="stTextArea"] > div > div > textarea,
        textarea {
            background-color: #1a1d23 !important;
            color: #fafafa !important;
            border: 1px solid #333 !important;
            border-radius: 8px !important;
            font-size: 15px !important;
            line-height: 1.5 !important;
            resize: vertical !important;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
            height: 50px !important;
            min-height: 50px !important;
            box-shadow: none !important;
            outline: none !important;
        }
        
        /* Focus state for textarea */
        .stTextArea textarea:focus,
        .stTextArea > div > div > textarea:focus,
        .stTextArea div[data-baseweb="textarea"] textarea:focus,
        div[data-testid="stTextArea"] textarea:focus,
        div[data-testid="stTextArea"] > div > div > textarea:focus,
        textarea:focus {
            border-color: #FF6B35 !important;
            box-shadow: 0 0 0 2px rgba(255, 107, 53, 0.1) !important;
            outline: none !important;
            background-color: #1a1d23 !important;
            color: #fafafa !important;
        }
        
        /* Target the textarea containers */
        .stTextArea,
        .stTextArea > div,
        .stTextArea > div > div,
        div[data-testid="stTextArea"],
        div[data-testid="stTextArea"] > div,
        div[data-testid="stTextArea"] > div > div {
            background-color: transparent !important;
        }
        
        /* Placeholder text styling */
        .stTextArea textarea::placeholder,
        .stTextArea > div > div > textarea::placeholder,
        div[data-testid="stTextArea"] textarea::placeholder,
        textarea::placeholder {
            color: #888 !important;
            opacity: 1 !important;
        }
        
        /* Additional fallback for any missed selectors */
        [data-baseweb="textarea"] {
            background-color: #1a1d23 !important;
        }
        
        [data-baseweb="textarea"] textarea {
            background-color: #1a1d23 !important;
            color: #fafafa !important;
        }
        
        /* Force override any default Streamlit textarea styles */
        .stApp textarea,
        .stApp input[type="text"],
        .stApp .stTextArea textarea {
            background-color: #1a1d23 !important;
            color: #fafafa !important;
            border: 1px solid #333 !important;
        }
        
        /* Form specific textarea targeting */
        div[data-testid="stForm"] textarea,
        form textarea {
            background-color: #1a1d23 !important;
            color: #fafafa !important;
            border: 1px solid #333 !important;
        }
        
        /* Nuclear option - force all input elements to dark theme */
        input, textarea, select {
            background-color: #1a1d23 !important;
            color: #fafafa !important;
            border: 1px solid #333 !important;
        }
        
        /* Override any white backgrounds specifically */
        *[style*="background-color: white"],
        *[style*="background-color: #ffffff"],
        *[style*="background-color: #fff"],
        *[style*="background: white"],
        *[style*="background: #ffffff"],
        *[style*="background: #fff"] {
            background-color: #1a1d23 !important;
        }
        
        /* ========================================
           FORM LAYOUT - BUTTON INSIDE SEARCH FIELD
        ======================================== */
        
        /* Make form container relative for positioning */
        .stForm {
            border: none !important;
            background: transparent !important;
            padding: 0 !important;
            position: relative !important;
        }
        
        /* Form columns - make textarea column 100% width */
        .stForm div[data-testid="column"]:first-child {
            width: 100% !important;
            flex: 1 !important;
            position: relative !important;
        }
        
        /* Hide the second column completely */
        .stForm div[data-testid="column"]:last-child {
            display: none !important;
        }
        
        /* Make textarea container relative for button positioning */
        .stTextArea {
            position: relative !important;
            width: 100% !important;
        }
        
        /* Textarea with padding for button space */
        .stTextArea textarea,
        .stTextArea > div > div > textarea,
        div[data-testid="stTextArea"] textarea,
        div[data-testid="stTextArea"] > div > div > textarea {
            background-color: #1a1d23 !important;
            color: #fafafa !important;
            border: 1px solid #333 !important;
            border-radius: 8px !important;
            font-size: 15px !important;
            line-height: 1.5 !important;
            resize: vertical !important;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
            height: 50px !important;
            min-height: 50px !important;
            box-shadow: none !important;
            outline: none !important;
            width: 100% !important;
            padding-right: 80px !important; /* Space for button */
            padding-left: 15px !important;
            padding-top: 12px !important;
            padding-bottom: 12px !important;
        }
        
        /* Position submit button inside textarea */
        .stFormSubmitButton {
            position: absolute !important;
            right: 5px !important;
            top: 50% !important;
            transform: translateY(-50%) !important;
            z-index: 10 !important;
            height: auto !important;
            width: auto !important;
        }
        
        .stFormSubmitButton > button {
            background-color: #FF6B35 !important;
            color: white !important;
            border: none !important;
            border-radius: 6px !important;
            font-weight: 500 !important;
            height: 40px !important;
            width: 70px !important;
            font-size: 14px !important;
            transition: all 0.2s ease !important;
            cursor: pointer !important;
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
            margin: 0 !important;
            padding: 0 !important;
            box-shadow: 0 2px 4px rgba(255, 107, 53, 0.2) !important;
        }
        
        .stFormSubmitButton > button:hover {
            background-color: #e55a2b !important;
            transform: scale(1.05) !important;
            box-shadow: 0 4px 8px rgba(255, 107, 53, 0.3) !important;
        }
        
        /* Alternative positioning using CSS grid for form */
        .stForm > div {
            display: grid !important;
            grid-template-columns: 1fr !important;
            position: relative !important;
        }
        
        /* Ensure button appears above textarea */
        .stForm .stFormSubmitButton {
            grid-column: 1 !important;
            grid-row: 1 !important;
            position: absolute !important;
            right: 5px !important;
            top: 50% !important;
            transform: translateY(-50%) !important;
            z-index: 100 !important;
        }
        
        .stForm .stTextArea {
            grid-column: 1 !important;
            grid-row: 1 !important;
            position: relative !important;
        }
        
        /* General Button Styling for other buttons */
        .stButton > button {
            background-color: #FF6B35 !important;
            color: white !important;
            border: none !important;
            border-radius: 6px !important;
            font-weight: 500 !important;
            height: 3rem !important;
            font-size: 14px !important;
            transition: all 0.2s ease !important;
            cursor: pointer !important;
        }
        
        .stButton > button:hover {
            background-color: #e55a2b !important;
            transform: translateY(-1px) !important;
        }
        
        /* ========================================
           QUICK EXAMPLES - ORANGE BACKGROUND WITH BLACK TEXT
        ======================================== */
        
        .examples-container {
            margin-top: 2rem !important;
            margin-bottom: 2rem !important;
        }
        
        .examples-header {
            color: #fafafa !important;
            font-size: 1.1rem !important;
            font-weight: 500 !important;
            margin-bottom: 1rem !important;
            text-align: center !important;
        }
        
        /* ORANGE BACKGROUND: Example buttons with BLACK text by default */
        div[data-testid="column"] .stButton > button {
            background-color: #FF6B35 !important;
            color: #000000 !important;  /* Black text by default */
            border: 1px solid #FF6B35 !important;
            border-radius: 6px !important;
            padding: 0.8rem 1rem !important;
            font-size: 14px !important;
            text-align: left !important;
            width: 100% !important;
            height: auto !important;
            min-height: 2.5rem !important;
            transition: all 0.2s ease !important;
            cursor: pointer !important;
            font-weight: 500 !important;
            white-space: normal !important;
            word-wrap: break-word !important;
            box-shadow: 0 2px 4px rgba(255, 107, 53, 0.2) !important;
        }
        
        div[data-testid="column"] .stButton > button:hover {
            background-color: #e55a2b !important;
            border-color: #e55a2b !important;
            color: #ffffff !important;  /* White text on hover */
            transform: translateY(-2px) !important;
            box-shadow: 0 4px 8px rgba(255, 107, 53, 0.3) !important;
        }
        
        /* Alternative: Target all buttons except the main submit button */
        .stButton:not(.stFormSubmitButton) > button {
            background-color: #FF6B35 !important;
            color: #000000 !important;  /* Black text by default */
            border: 1px solid #FF6B35 !important;
            font-weight: 500 !important;
            box-shadow: 0 2px 4px rgba(255, 107, 53, 0.2) !important;
        }
        
        .stButton:not(.stFormSubmitButton) > button:hover {
            background-color: #e55a2b !important;
            border-color: #e55a2b !important;
            color: #ffffff !important;  /* White text on hover */
            transform: translateY(-2px) !important;
            box-shadow: 0 4px 8px rgba(255, 107, 53, 0.3) !important;
        }
        
        /* ========================================
           CUSTOM FOOTER - MINIMAL
        ======================================== */
        
        .custom-footer {
            text-align: center;
            color: #666;
            padding: 1rem 0;
            border-top: 1px solid #262b36;
            margin-top: 2rem;
            font-size: 14px;
        }
        
        .custom-footer strong {
            color: #FF6B35;
        }
        
        /* ========================================
           CODE BLOCKS - MINIMAL DARK
        ======================================== */
        
        code, pre, .stCode {
            background-color: #1a1d23 !important;
            color: #fafafa !important;
            border: 1px solid #333 !important;
            border-radius: 6px !important;
            font-size: 14px !important;
        }
        
        /* ========================================
           FORM SPACING - INLINE BUTTON LAYOUT
        ======================================== */
        
        /* Override default form styling for inline layout */
        .stForm {
            border: none !important;
            background: transparent !important;
            padding: 0 !important;
            position: relative !important;
        }
        
        /* Remove button spacer completely */
        .button-spacer {
            height: 0rem !important;
            display: none !important;
        }
        
        /* ========================================
           RESPONSIVE DESIGN
        ======================================== */
        
        @media (max-width: 768px) {
            .main .block-container {
                padding-left: 1rem !important;
                padding-right: 1rem !important;
                max-width: 100% !important;
            }
            
            .main-header-reduced {
                font-size: 1.8rem !important;
            }
            
            .stFormSubmitButton > button {
                height: 35px !important;
                width: 60px !important;
                font-size: 12px !important;
            }
            
            .stTextArea textarea,
            .stTextArea > div > div > textarea,
            div[data-testid="stTextArea"] textarea {
                height: 45px !important;
                min-height: 45px !important;
                padding-right: 70px !important;
            }
        }
        
        /* ========================================
           CLEAN TRANSITIONS
        ======================================== */
        
        * {
            transition: all 0.2s ease !important;
        }
        
        /* Remove default streamlit styling */
        .stApp > div > div > div > div {
            padding-top: 0 !important;
        }
        
        /* ========================================
           LAST RESORT OVERRIDES - NUCLEAR OPTION
        ======================================== */
        
        /* Force inherit background for all elements except specific ones */
        .stApp *:not(.stFormSubmitButton):not(.stButton) {
            background: inherit !important;
        }
        
        /* Specifically target any remaining white elements */
        .stApp div:not([data-testid="stFormSubmitButton"]):not([data-testid="stButton"]) {
            background-color: inherit !important;
        }
        
    </style>
    """, unsafe_allow_html=True)

def apply_light_theme():
    """Apply light theme (for future use if needed)"""
    st.markdown("""
    <style>
        .stApp {
            background-color: #000000 !important;
            color: #262730 !important;
        }
    </style>
    """, unsafe_allow_html=True)

def get_theme_colors():
    """Return theme color palette for consistent usage"""
    return {
        "primary": "#FF6B35",
        "primary_hover": "#e55a2b",
        "background": "#0e1117",
        "secondary_bg": "#1a1d23",
        "text_primary": "#fafafa",
        "text_secondary": "#ccc",
        "accent_blue": "#4FC3F7",
        "success": "#69f0ae",
        "error": "#ff9999",
        "border": "#333",
    }

def apply_custom_footer():
    """Apply custom footer styling"""
    st.markdown("""
    <style>
        .custom-footer {
            text-align: center;
            color: #666;
            padding: 1rem 0;
            border-top: 1px solid #262b36;
            margin-top: 2rem;
            font-size: 14px;
        }
        
        .custom-footer strong {
            color: #FF6B35;
        }
    </style>
    """, unsafe_allow_html=True)

# Preset configurations
SIDEBAR_EXAMPLES = [
    "What is a function?",
    "How to debug JavaScript?", 
    "React vs Vue?",
    "How to get a tech job?",
    "Async/await explained",
    "What are closures?",
    "How to learn DSA?",
    "Best practices for coding?"
]

CHAT_PLACEHOLDERS = [
    "Ask me anything about coding, career, or tech...",
    "What would you like to learn today?",
    "Need help with programming concepts?",
    "Type your question here...",
]