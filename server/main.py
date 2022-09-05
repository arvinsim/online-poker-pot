from fastapi import FastAPI
from datetime import datetime
from typing import List
from pydantic import BaseModel

from helpers import filter_players_from_ids


class Game(BaseModel):
    id: int
    pot: int


class Player(BaseModel):
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


@app.get("/games")
async def get_games():
    return {
        'status': 'ok',
        'games': games
    }


@app.get("/players")
async def get_players():
    return {
        'status': 'ok',
        'players': players
    }


@app.post('/games')
async def add_game(params: AddGamesParams):
    params_dict = params.dict()

    # Getting the current date and time
    dt = datetime.now()

    # getting the timestamp
    ts = datetime.timestamp(dt)

    new_game = {'id': ts, 'players': filter_players_from_ids(params_dict['player_ids'], players)}
    games.append(new_game)

    return {'status': 'ok', 'games': games}


@app.post("/players")
async def add_players():
    return {'status': 'ok'}
