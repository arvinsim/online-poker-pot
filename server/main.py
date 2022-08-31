from fastapi import FastAPI
from datetime import datetime
from typing import List
from pydantic import BaseModel

from helpers import filter_players_from_ids


class Players(BaseModel):
    id: int
    name: str
    pot: int

class AddGamesParams(BaseModel):
    player_ids: List[int]


app = FastAPI()

games = []

players = [{
    'id': 1,
    'name': 'Arthur',
    'pot': 0
}]


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/games/")
async def get_games():
    return {
        'status': 'ok',
        'games': games
    }


@app.get("/players/")
async def get_players():
    return {
        'status': 'ok',
        'players': players
    }


@app.post('/games/')
async def add_game(params: AddGamesParams):
    return {'status': 'ok'}

@app.post("/players/")
async def add_players():
    return {'status': 'ok'}
