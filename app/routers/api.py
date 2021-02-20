from fastapi import APIRouter, Request, WebSocket
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Date, Integer, String
import os

router = APIRouter()

# Database Setup Start

engine = create_engine('sqlite:///fastapi.db', echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
class Chat(Base):

    __tablename__ = "chat"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    date = Column(String)
    message = Column(String)


    def __init__(self, name, date, message):
        self.date = date
        self.name = name
        self.message = message


if(os.path.isfile('fastapi.db') == False):
    Base.metadata.create_all(engine)

connection = engine.connect()

database = SessionLocal()


@router.post('/chat/message')
async def websocket_endpoint(request: Request):
    req = await request.json()
    message = req['message']
    database.add(Chat(name=str(req['username']), date=str(req['date']), message=str(req['message'])))
    database.commit()
    return {'status': 200, 'message': 'ok'}

@router.get('/chat/history')
async def websocket_endpoint(request: Request):
    chat_history = database.query(Chat).all()
        
    return chat_history