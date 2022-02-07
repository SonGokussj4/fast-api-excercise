# inside of a Python .py file

# uvicorn main:app --reload
# gunicorn -w 4 -k uvicorn.workers.UvicornWorker  main:app --reload

from typing import List
from urllib.request import Request
import uvicorn
import time

from app import crud

from fastapi import Depends, FastAPI, APIRouter
from pydantic import BaseModel, BaseConfig
from sqlalchemy.orm import Session

from app.api import deps
from app.models.user import User


BaseConfig.arbitrary_types_allowed = True


app = FastAPI(
    title="CSFD FAST API",
    # openapi_url="/openapi.json"
)

api_router = APIRouter()


@api_router.get("/", status_code=200)
def home():
    return {"Hello": "World"}


@api_router.get("/users/{user_id}", status_code=200)
async def fetch_user(*, user_id: int, db: Session = Depends(deps.get_db)) -> dict:  # 3
    """
    Fetch a single recipe by ID
    """
    user = crud.user.get_by_id(db, user_id=user_id)
    return user


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


app.include_router(api_router)


if __name__ == "__main__":
    import uvicorn
    # uvicorn.run("main:app")
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")
