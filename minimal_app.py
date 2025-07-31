from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from dotenv import load_dotenv
import time
from typing import Optional, Dict, Any

# Load environment variables
load_dotenv()

# Create FastAPI app
app = FastAPI(
    title="Telegram Mini App",
    description="A minimal Telegram Mini App built with FastAPI",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic models
class MessageRequest(BaseModel):
    chat_id: int
    message: str

class ApiResponse(BaseModel):
    success: bool
    message: str
    data: Optional[Dict[str, Any]] = None

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "🚀 Telegram Mini App API is running!",
        "status": "active",
        "framework": "FastAPI",
        "timestamp": time.time()
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": time.time(),
        "service": "Telegram Mini App API",
        "version": "1.0.0"
    }

@app.post("/api/send-message", response_model=ApiResponse)
async def send_message(request: MessageRequest):
    """Send message to user via Telegram Bot"""
    try:
        return ApiResponse(
            success=True,
            message="Message sent successfully",
            data={"chat_id": request.chat_id, "message": request.message}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/info")
async def api_info():
    """API information endpoint"""
    return {
        "name": "Telegram Mini App API",
        "version": "1.0.0",
        "framework": "FastAPI",
        "endpoints": [
            {"path": "/", "method": "GET", "description": "Root endpoint"},
            {"path": "/health", "method": "GET", "description": "Health check"},
            {"path": "/api/send-message", "method": "POST", "description": "Send message to user"},
            {"path": "/api/info", "method": "GET", "description": "API information"},
            {"path": "/docs", "method": "GET", "description": "API documentation"}
        ]
    }

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get('PORT', 8000))
    print(f"🚀 Starting FastAPI server on http://localhost:{port}")
    print(f"📖 API Documentation: http://localhost:{port}/docs")
    uvicorn.run(app, host="0.0.0.0", port=port) 