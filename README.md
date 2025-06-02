Hitesh Choudhary AI Persona - FastAPI + Streamlit
A Chain of Thought AI persona of coding teacher Hitesh Choudhary, built with FastAPI backend and Streamlit frontend.
🚀 Features

Chain of Thought Reasoning: Step-by-step thinking process visible in responses
Dual Chat Modes: Normal conversation and enhanced analysis mode
Hinglish Communication: Mix of Hindi and English, just like Hitesh
Real-time Chat Interface: Beautiful Streamlit UI with chat history
API-First Design: Separate FastAPI backend for scalability
Demo Examples: Pre-built examples showing CoT in action

📋 Prerequisites

Python 3.8+
OpenAI API key
Git (optional)

🛠️ Installation & Setup

1. Clone or Download Files
   bash# If using git
   git clone <your-repo-url>
   cd hitesh-ai-persona

# Or download the files manually

2. Create Virtual Environment
   bashpython -m venv venv

# Activate virtual environment

# On Windows:

venv\Scripts\activate

# On macOS/Linux:

source venv/bin/activate 3. Install Dependencies
bashpip install -r requirements.txt 4. Environment Setup
Create a .env file in the project root:
envOPENAI_API_KEY=your_openai_api_key_here 5. File Structure
Your project should look like this:
hitesh-ai-persona/
├── main.py # FastAPI backend
├── app.py # Streamlit frontend  
├── requirements.txt # Python dependencies
├── .env # Environment variables
└── README.md # This file
🚀 Running the Application
Step 1: Start FastAPI Backend
bash# Run the FastAPI server
uvicorn main:app --reload --host 0.0.0.0 --port 8000
The API will be available at:

API: http://localhost:8000
Docs: http://localhost:8000/docs
ReDoc: http://localhost:8000/redoc

Step 2: Start Streamlit Frontend
Open a new terminal, activate your virtual environment, then:
bash# Run the Streamlit app
streamlit run app.py
The Streamlit app will be available at: http://localhost:8501
🎯 Usage
Chat Modes

Normal CoT Mode: Natural conversation with step-by-step thinking
Enhanced Analysis Mode: Deep problem breakdown with detailed reasoning

Example Questions to Try

"What is a function?"
"How to debug JavaScript errors?"
"Should I learn React or Vue?"
"How to become job-ready in tech?"
"Explain async/await in simple terms"

API Endpoints
Health Check
bashGET http://localhost:8000/health
Chat with Hitesh
bashPOST http://localhost:8000/chat
Content-Type: application/json

{
"message": "What is a closure in JavaScript?",
"mode": "normal"
}
Get Demo Examples
bashGET http://localhost:8000/demo-examples
🧠 Chain of Thought Features
The AI persona uses Chain of Thought reasoning, which means:

Visible Thinking Process: See how Hitesh thinks through problems
Step-by-Step Breakdown: Complex topics explained in manageable parts
Why Before What: Understanding the reasoning behind concepts
Real-world Connections: Practical examples and analogies
Teaching Methodology: Focus on HOW to learn, not just WHAT to learn

🎨 Customization
Modify the Persona
Edit the SYSTEM_PROMPT in main.py to customize:

Teaching style
Communication patterns
Expertise areas
Response format

UI Customization
Modify the CSS in app.py to change:

Colors and themes
Layout and spacing
Chat message styling
Sidebar appearance

Add New Features

New API endpoints in main.py
Additional UI components in app.py
Custom chat modes
Integration with other AI models

🐛 Troubleshooting
Common Issues

API Connection Failed

Ensure FastAPI server is running on port 8000
Check if the API_BASE_URL in app.py is correct

OpenAI API Errors

Verify your API key in .env file
Check your OpenAI account balance
Ensure model name (gpt-4o-mini) is available

Module Import Errors

Ensure virtual environment is activated
Run pip install -r requirements.txt again

Streamlit Connectivity Issues

Check if both servers are running
Verify firewall settings
Try restarting both servers

Debug Mode
Run FastAPI in debug mode:
bashuvicorn main:app --reload --log-level debug
Run Streamlit in debug mode:
bashstreamlit run app.py --logger.level debug
📊 API Documentation
Once the FastAPI server is running, visit:

Interactive API docs: http://localhost:8000/docs
Alternative docs: http://localhost:8000/redoc

🔒 Security Notes

In production, update CORS settings in main.py
Use environment variables for all sensitive data
Consider implementing rate limiting
Add authentication if needed

🚀 Deployment
FastAPI Backend

Deploy to services like Railway, Render, or AWS
Update CORS origins for production domains
Set up proper environment variables

Streamlit Frontend

Deploy to Streamlit Cloud, Heroku, or similar
Update API_BASE_URL to your production API
Configure secrets for environment variables

🤝 Contributing

Fork the repository
Create a feature branch
Make your changes
Test thoroughly
Submit a pull request

📜 License
This project is for educational purposes. Please respect OpenAI's usage policies.
🙏 Acknowledgments

Hitesh Choudhary for the inspiration and teaching methodology
OpenAI for the GPT models
FastAPI and Streamlit communities

Remember: Chain of Thought thinking se sab kuch possible hai! Chai aur Code! ☕️💻
"# Persona-AI-Bot" 
