from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
from openai import OpenAI
import os
from typing import Optional

# Import system prompts
from prompts import SYSTEM_PROMPT, ENHANCED_ANALYSIS_TEMPLATE

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(
    title="Hitesh Choudhary AI Persona API",
    description="Chain of Thought AI Persona of Hitesh Choudhary",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify Streamlit app's URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize OpenAI client
client = OpenAI()

# Pydantic models for request/response
class ChatRequest(BaseModel):
    message: str
    # mode: Optional[str] = "normal"  # COMMENTED OUT - Mode functionality removed

class ChatResponse(BaseModel):
    response: str
    # mode: str  # COMMENTED OUT - Mode functionality removed
    success: bool

class HealthResponse(BaseModel):
    status: str
    message: str

@app.get("/", response_model=HealthResponse)
async def root():
    """Health check endpoint"""
    return HealthResponse(
        status="healthy",
        message="Hitesh Choudhary AI Persona API is running! 🚀"
    )

@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Detailed health check"""
    try:
        # Test OpenAI connection
        client.models.list()
        return HealthResponse(
            status="healthy",
            message="API and OpenAI connection are working perfectly! Chai aur Code! ☕️💻"
        )
    except Exception as e:
        raise HTTPException(
            status_code=503,
            detail=f"Service unavailable: {str(e)}"
        )

@app.post("/chat", response_model=ChatResponse)
async def chat_with_hitesh(request: ChatRequest):
    """Main chat endpoint with Chain of Thought reasoning"""
    try:
        if not request.message.strip():
            raise HTTPException(
                status_code=400,
                detail="Message cannot be empty! Kuch toh poochiye! 😄"
            )
        
        # Always use normal mode now
        user_message = request.message
        
        # Make API call to OpenAI
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_message}
            ],
            temperature=0.8,
            max_tokens=800  # Fixed token limit since no mode switching
        )
        
        ai_response = response.choices[0].message.content
        
        return ChatResponse(
            response=ai_response,
            # mode=request.mode,  # COMMENTED OUT - Mode functionality removed
            success=True
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Koi technical issue aa gaya! Error: {str(e)}"
        )

@app.get("/persona-info")
async def get_persona_info():
    """Get information about Hitesh Choudhary persona"""
    return {
        "name": "Hitesh Choudhary",
        "description": "AI Persona of coding teacher Hitesh Choudhary",
        "specialties": [
            "JavaScript & Web Development",
            "React & Frontend Frameworks", 
            "Career Guidance in Tech",
            "Beginner-friendly Teaching",
            "Industry Best Practices"
        ],
        "teaching_style": [
            "Chain of Thought reasoning",
            "Step-by-step explanations",
            "Hinglish communication",
            "Practical examples",
            "Industry standards focus"
        ],
        "signature_phrases": ["Chai aur Code", "hands-on approach", "industry standard"],
        "channels": {
            "main_channel": "1M+ subscribers",
            "second_channel": "300K+ subscribers"
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)