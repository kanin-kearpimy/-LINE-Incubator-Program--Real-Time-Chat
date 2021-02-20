from fastapi import APIRouter, Request, WebSocket

router = APIRouter()

@router.get('/chat/message')
async def websocket_endpoint(request: Request):
    req = await request.json()
    message = req['message']
    return message

@router.get('/chat/history')
async def websocket_endpoint(request: Request):
    return [{
        "date": 'today',
        "user": "mock",
        "message": "hello"
    }]