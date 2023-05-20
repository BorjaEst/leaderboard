from fastapi import FastAPI

from app.api import api_v1
from app.config import settings

app = FastAPI(title=__package__, **settings.app.dict())
app.include_router(api_v1.router, prefix=settings.v1_str)
