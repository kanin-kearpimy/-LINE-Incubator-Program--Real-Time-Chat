from typing import Optional
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
import os
from app.routers import api, web

# Basic Application Setup
app = FastAPI()
app.mount("/static", StaticFiles(directory='app/static'), name="static")
load_dotenv('./.env')

# import router
app.include_router(api.router)
app.include_router(web.router)

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://127.0.0.1:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)