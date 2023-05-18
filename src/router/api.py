from fastapi import APIRouter
from src.router.routes import celery, base

router = APIRouter()

router.include_router(celery.router)
router.include_router(base.router)