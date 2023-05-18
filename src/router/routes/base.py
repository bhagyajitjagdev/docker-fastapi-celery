from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse

router = APIRouter(
    prefix="/base",
    tags=["Base"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
def healthCheck():
    return JSONResponse({"message": "Base Working"})
