from fastapi import APIRouter
from app.api.routes.cleanings import router as cleanings_router

router = APIRouter()

# создаем пространство имен для клининг 

router.include_router(cleanings_router, prefix="/cleanings", tags=["cleanings"])