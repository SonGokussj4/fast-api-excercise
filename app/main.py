# inside of a Python .py file

# uvicorn main:app --reload
# gunicorn -w 4 -k uvicorn.workers.UvicornWorker  main:app --reload

import time
import uvicorn
from typing import List
from urllib.request import Request
from fastapi import Depends, FastAPI, APIRouter
from sqlalchemy.orm import Session

from app.api.api_v1.api import api_router
from app.core.config import settings


# BaseConfig.arbitrary_types_allowed = True
app = FastAPI(title="CSFD FAST API")

root_router = APIRouter()


@root_router.get("/", status_code=200)
def home():
    return {"Hello": "World"}


# @root_router.get("/", status_code=200)
# def root(request: Request, db: Session = Depends(deps.get_db)) -> dict:
#     """
#     Root GET
#     """
#     recipes = crud.recipe.get_multi(db=db, limit=10)
#     return TEMPLATES.TemplateResponse(
#         "index.html",
#         {"request": request, "recipes": recipes},
#     )


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


app.include_router(root_router)
app.include_router(api_router, prefix=settings.API_V1_STR)


if __name__ == "__main__":
    import uvicorn
    # uvicorn.run("main:app")
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")
