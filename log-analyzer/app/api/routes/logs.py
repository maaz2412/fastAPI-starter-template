from fastapi import APIRouter


router = APIRouter()


@router.post("/", summary="Add a new log")
async def add_log():
    print("Log added")