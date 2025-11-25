from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import app
import uvicorn
import logging
import os
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    API_PORT = int(os.getenv("API_PORT", "8000"))
    print(API_PORT)
    
    print(f"Starting server on port {API_PORT}")
    
    logging.basicConfig(level=logging.INFO)
    
    uvicorn.run(
        "main:app",
        host="0.0.0.0",#можно указать хост сети, чтобы по вайфай, например: 172.28.31.255
        port=API_PORT,#
        reload=True,
        log_level="info",
        access_log=True,
    )