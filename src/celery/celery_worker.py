import os
import asyncio
from celery import Celery


celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL")
celery.conf.broker_url = os.environ.get("CELERY_RESULT_BACKEND")


@celery.task(name="run_model")
def run_model(path: str) -> dict:
  asyncio.run(long_async_task(path))
  return {'result': path}



async def long_async_task(path: str):
    for i in range(100):
        print(f'${path} - ${i}')
        await asyncio.sleep(1)
