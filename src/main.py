from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .router.api import router as api_router

import debugpy
debugpy.listen({"0.0.0.0", 5678})

app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_methods=["*"],
  allow_headers=["*"],
  allow_credentials=True,
)


app.include_router(api_router, prefix='/v1/api')
