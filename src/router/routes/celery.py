from fastapi import APIRouter, Body, Response
from fastapi.responses import JSONResponse

import celery.states as status
from celery.result import AsyncResult


from src.celery.celery_worker import celery

router = APIRouter(
    prefix="/celery",
    tags=["Celery"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
def healthCheck():
    return JSONResponse({"message": "Celery Working"})


@router.post("/add-model", status_code=200)
def add_model(data=Body(...)) -> Response:
  path = data["path"]
  task = celery.send_task("run_model", args=[path])
  return JSONResponse({"task_id": task.id})


@router.get("/model-status/{task_id}")
async def model_status(task_id: str) ->  Response:
  res = AsyncResult(task_id)
  if res.state == status.SUCCESS:
    return { 'state': status.SUCCESS, 'result': res.result }
  return { 'state': res.state }