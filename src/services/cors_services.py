from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def set_cors(app: FastAPI):
    allow_origins = [
        "http://localhost:8000",
        "http://localhost:8000",
        "http://localhost:2024"
    ]
    
    app.add_middleware(
        CORSMiddleware,
        allow_origins=allow_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
