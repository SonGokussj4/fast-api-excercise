from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Any, Optional

from app import crud
from app.api import deps
# from app.schemas.user import Recipe, RecipeCreate, RecipeSearchResults
from app.schemas.user import User, UserCreate, UserSearchResults
from app.schemas.rating import RatingSearchResults, UserRatings


router = APIRouter()


@router.get("/", status_code=200, response_model=UserSearchResults)
async def fetch_all_users(*, db: Session = Depends(deps.get_db)) -> dict:
    """
    Fetch all Users
    """
    users = await crud.user.get_all(db)
    return {
        "results": users,
        "count": len(users)
    }


@router.get("/{user_id:int}", status_code=200, response_model=User, summary="Fetch a User by ID")
async def fetch_user_by_id(*, user_id: int, db: Session = Depends(deps.get_db)) -> dict:
    """
    Fetch a single user by ID
    """
    user = await crud.user.get_by_id(db, user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/", status_code=200, response_model=User, summary="Add a User")
async def add_user(*, user: User, db: Session = Depends(deps.get_db)) -> dict:
    """
    Add a user to DB
    """
    added_user = await crud.user.add_user(db, user=user)
    print(f'added_user: {added_user}')
    if not added_user:
        raise HTTPException(status_code=404, detail=f"User {user.Username} couldn't be added")
    return added_user


@router.get("/{username:str}", status_code=200, response_model=User)
async def fetch_user_by_username(*, username: str, db: Session = Depends(deps.get_db)) -> dict:
    """
    Fetch a single user by username
    """
    user = await crud.user.get_by_username(db, username=username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get("/{username:str}/ratings", status_code=200, response_model=UserRatings)  # , response_model=UserRatings
async def fetch_user_ratings(*, username: str, db: Session = Depends(deps.get_db)) -> dict:
    """
    Fetch watched and rated movies of selected username
    """
    ratings = await crud.user.get_ratings_by_username(db, username=username)
    return {
        "results": ratings,
        "count": len(ratings)
    }


@router.post("/{username:str}", status_code=200, response_model=UserCreate)
async def create_user(*, username: str, db: Session = Depends(deps.get_db)) -> dict:
    """
    Create user
    """
    user = await crud.user.create_user(db)
    return user

# @router.get("/{recipe_id}", status_code=200, response_model=Recipe)
# def fetch_recipe(
#     *,
#     recipe_id: int,
#     db: Session = Depends(deps.get_db),
# ) -> Any:
#     """
#     Fetch a single recipe by ID
#     """
#     result = crud.recipe.get(db=db, id=recipe_id)
#     if not result:
#         # the exception is raised, not returned - you will get a validation
#         # error otherwise.
#         raise HTTPException(
#             status_code=404, detail=f"Recipe with ID {recipe_id} not found"
#         )

#     return result


# @router.get("/search/", status_code=200, response_model=RecipeSearchResults)
# def search_recipes(
#     *,
#     keyword: Optional[str] = Query(None, min_length=3, example="chicken"),
#     max_results: Optional[int] = 10,
#     db: Session = Depends(deps.get_db),
# ) -> dict:
#     """
#     Search for recipes based on label keyword
#     """
#     recipes = crud.recipe.get_multi(db=db, limit=max_results)
#     if not keyword:
#         return {"results": recipes}

#     results = filter(lambda recipe: keyword.lower() in recipe.label.lower(), recipes)
#     return {"results": list(results)[:max_results]}


# @router.post("/", status_code=201, response_model=Recipe)
# def create_recipe(
#     *, recipe_in: RecipeCreate, db: Session = Depends(deps.get_db)
# ) -> dict:
#     """
#     Create a new recipe in the database.
#     """
#     recipe = crud.recipe.create(db=db, obj_in=recipe_in)

#     return recipe
