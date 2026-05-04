#entry point of the application

from fastapi import FastAPI
from app.core.config import config
from app.api.router import router
from app.core.exception_handler import global_exception_handler

#Initialize fastAPI router
app = FastAPI(
    title = config.PROJECT_NAME,
    version = config.VERSION,
)


#register the apps router
app.include_router(router)

#Exception handlers
app.add_exception_handler(Exception, global_exception_handler)