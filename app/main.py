from fastapi import FastAPI

from app.api import api_v1

API_STR: str = f"/api/v1"
app = FastAPI(title=__package__, openapi_url=f"{API_STR}/openapi.json")
app.include_router(api_v1.router, prefix=API_STR)
