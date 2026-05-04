from fastapi import APIRouter
from api.routes import logs


router = APIRouter()


router.include_router(logs.router, prefix="/logs", tags=["Logs"])