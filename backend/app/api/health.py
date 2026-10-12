from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class HealthResponse(BaseModel):
    status: str
    service: str
    version: str


@router.get("/health", response_model=HealthResponse)
async def health_check() -> HealthResponse:
    """Проверка работоспособности сервиса."""
    return HealthResponse(
        status="ok",
        service="password-strength-service",
        version="0.1.0",
    )