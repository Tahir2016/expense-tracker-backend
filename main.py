from fastapi import FastAPI
from src.tracker.router import router as tracker_router
from src.user.router import router as user_router
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os

app = FastAPI()

origins = [
    "http://localhost:3000",
    os.getenv("FRONTEND_URL", ""),
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tracker_router)
app.include_router(user_router)

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)

