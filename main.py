# inside of a Python .py file

# uvicorn main:app --reload
# gunicorn -w 4 -k uvicorn.workers.UvicornWorker  main:app --reload

import uvicorn

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def home():
    return {"Hello": "World"}

    if __name__ == "__main__":

        uvicorn.run("main:app")

@app.get("/teams")
def create_team():
    teams = []
    team = {

        "team_name": "Phoenix Suns",
        "players": [

            {

                  "name": "Chris Paul",
                  "age": 36

            }

        ]

    }

    teams.append(team)
    return {'teams':teams}




class Player(BaseModel):
    player_name: str
    player_team: str
    player_age: int

@app.post("/teams")
def create_team(request: Player):
    return {'teams':request}
