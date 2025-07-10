from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import users, analyze
from app.databse import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()
origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,        
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(analyze.router)
