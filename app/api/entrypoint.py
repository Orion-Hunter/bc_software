from fastapi import FastAPI

from app.api.controllers.index import router as index_router
from app.config.settings import Settings

settings = Settings()

app = FastAPI(
    title="Pandora Insights",
    docs_url=settings.DOCS_URL,
    redoc_url=settings.REDOC_URL,
    openapi_url=settings.OPENAPI_URL,
    version="0.0.0",
)

app.include_router(
    prefix="/v1",
    tags=["Health"],
    router=index_router,
)
