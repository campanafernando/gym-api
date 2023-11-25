from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app.domains.user import user_api
from app.domains.gym import gym_api

import time

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


origins = [
    "http://localhost:8000",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


app.include_router(user_api.router, prefix="/v1", tags=["users"])
app.include_router(gym_api.router, prefix="/v1", tags=["gym"])

