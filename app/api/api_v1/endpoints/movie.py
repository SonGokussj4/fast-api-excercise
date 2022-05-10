from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Any, Optional

from app import crud
from app.api import deps
from app.schemas.movie import Movie, MovieSearchResults

router = APIRouter()


@router.get("/", status_code=200, response_model=MovieSearchResults)
async def fetch_all_movies(*, db: Session = Depends(deps.get_db)) -> dict:
    """
    Fetch all Movies
    """
    movies = await crud.movie.get_all(db)
    if not movies:
        raise HTTPException(status_code=404, detail="No movies found")
    return {
        "results": movies,
        "count": len(movies)
    }



@router.get("/{movie_id:int}", status_code=200, response_model=Movie)
async def fetch_movie(*, movie_id: int, db: Session = Depends(deps.get_db)) -> dict:
    """
    Fetch one Movie
    """
    movie = await crud.movie.get_by_id(db, movie_id=movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie


@router.post("/", status_code=200, response_model=Movie, summary="Add a Movie")
async def add_movie(*, movie: Movie, db: Session = Depends(deps.get_db)) -> dict:
    """
    Add a movie to DB
    """
    print("Adding movie: ", movie)
    added_movie = await crud.movie.add_movie(db, movie=movie)
    print(f'added_movie: {added_movie}')
    if not added_movie:
        raise HTTPException(status_code=404, detail=f"Movie {movie.Url} couldn't be added")
    return added_movie

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
