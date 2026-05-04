from fastapi import Request
from fastapi.responses import JSONResponse


async def global_exception_handler(req: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "message": f"An unexpected error occurred: {str(exc)}",
            "success": False,
        },
    )

