from fastapi import APIRouter

from app.api.api_v1.endpoints import user, movie, rating


api_router = APIRouter()
api_router.include_router(user.router, prefix="/users", tags=["users"])
api_router.include_router(movie.router, prefix="/movies", tags=["movies"])
api_router.include_router(rating.router, prefix="/ratings", tags=["ratings"])