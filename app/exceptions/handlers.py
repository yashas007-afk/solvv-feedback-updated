from fastapi import FastAPI
from fastapi.responses import JSONResponse
from .custom_exceptions import FeedbackNotFoundError

def register_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(FeedbackNotFoundError)
    async def feedback_not_found_handler(_, exc: FeedbackNotFoundError):
        return JSONResponse(status_code=404, content={"detail": str(exc)})