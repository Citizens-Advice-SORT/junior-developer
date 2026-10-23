from fastapi import APIRouter

router = APIRouter(tags=["hello"])


@router.get("/")
async def hello():
    return {"message": "Hello World"}
