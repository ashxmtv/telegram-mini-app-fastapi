from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from dotenv import load_dotenv
import json
import hashlib
import hmac
import time
from typing import Optional, Dict, Any

# Load environment variables
load_dotenv()

# Create FastAPI app
app = FastAPI(
    title="Telegram Mini App",
    description="A modern Telegram Mini App built with FastAPI",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure this properly for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

# Configuration
BOT_TOKEN = os.getenv('BOT_TOKEN')
WEBAPP_URL = os.getenv('WEBAPP_URL', 'https://your-domain.com')

# Pydantic models
class InitDataRequest(BaseModel):
    initData: Dict[str, Any]

class MessageRequest(BaseModel):
    chat_id: int
    message: str

class UserDataResponse(BaseModel):
    success: bool
    user: Dict[str, Any]

class ApiResponse(BaseModel):
    success: bool
    message: str
    data: Optional[Dict[str, Any]] = None

def validate_telegram_data(init_data: Dict[str, Any]) -> bool:
    """Validate Telegram WebApp data using HMAC"""
    if not init_data or not BOT_TOKEN:
        return False
    
    try:
        # Parse the init data
        data_check_string = '\n'.join([
            f"{k}={v}" for k, v in sorted(init_data.items()) 
            if k != 'hash'
        ])
        
        # Create secret key
        secret_key = hmac.new(
            "WebAppData".encode(),
            BOT_TOKEN.encode(),
            hashlib.sha256
        ).digest()
        
        # Calculate hash
        data_hash = hmac.new(
            secret_key,
            data_check_string.encode(),
            hashlib.sha256
        ).hexdigest()
        
        return data_hash == init_data.get('hash', '')
    except Exception:
        return False

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """Main page of the Mini App"""
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/api/init", response_model=ApiResponse)
async def init_app(request: InitDataRequest):
    """Initialize the Mini App with Telegram data"""
    try:
        # Validate Telegram data
        if not validate_telegram_data(request.initData):
            raise HTTPException(status_code=401, detail="Invalid Telegram data")
        
        # Extract user information
        user_data = json.loads(request.initData.get('user', '{}'))
        
        return ApiResponse(
            success=True,
            message="Mini App initialized successfully",
            data={"user": user_data}
        )
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/send-message", response_model=ApiResponse)
async def send_message(request: MessageRequest):
    """Send message to user via Telegram Bot"""
    try:
        # Here you would integrate with Telegram Bot API
        # For now, we'll just return success
        return ApiResponse(
            success=True,
            message="Message sent successfully",
            data={"chat_id": request.chat_id, "message": request.message}
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/user-data", response_model=UserDataResponse)
async def get_user_data(
    user_id: Optional[str] = None,
    first_name: Optional[str] = None,
    last_name: Optional[str] = None,
    username: Optional[str] = None
):
    """Get user data from Telegram"""
    try:
        user_data = {
            'id': user_id,
            'first_name': first_name,
            'last_name': last_name,
            'username': username
        }
        
        return UserDataResponse(
            success=True,
            user=user_data
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": time.time(),
        "service": "Telegram Mini App API",
        "version": "1.0.0"
    }

@app.get("/api/info")
async def api_info():
    """API information endpoint"""
    return {
        "name": "Telegram Mini App API",
        "version": "1.0.0",
        "framework": "FastAPI",
        "endpoints": [
            {"path": "/", "method": "GET", "description": "Main Mini App interface"},
            {"path": "/api/init", "method": "POST", "description": "Initialize Mini App"},
            {"path": "/api/send-message", "method": "POST", "description": "Send message to user"},
            {"path": "/api/user-data", "method": "GET", "description": "Get user information"},
            {"path": "/health", "method": "GET", "description": "Health check"},
            {"path": "/api/info", "method": "GET", "description": "API information"}
        ]
    }

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get('PORT', 8000))
    uvicorn.run(app, host="0.0.0.0", port=port) 