from fastapi import APIRouter, Request

router = APIRouter()

@router.post('/api/add-list')
async def addList(request: Request):
    all_request = await request.json()
    return all_request