# main_fastapi.py (FastAPI で動かします)
# uvicorn main_fastapi:app --reload
# 「main_fastapi」の部分で、パスの指定をして起動させています。

import random
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# リクエストとレスポンスの定義
class JankenRequest(BaseModel):
    player_choice: str  # "rock", "paper", "scissors"

class JankenResponse(BaseModel):
    player_choice: str
    computer_choice: str
    result: str  # "win", "lose", "draw"


# アプリ部分（getは省略）
@app.post("/janken/", response_model=JankenResponse)
async def play_janken(request: JankenRequest):
    # コンピュータの手をランダムに選択
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    
    # 勝敗判定
    if request.player_choice == computer_choice:
        result = "draw"
    elif (request.player_choice == "rock" and computer_choice == "scissors") or \
         (request.player_choice == "paper" and computer_choice == "rock") or \
         (request.player_choice == "scissors" and computer_choice == "paper"):
        result = "win"
    else:
        result = "lose"
    
    return JankenResponse(
        player_choice=request.player_choice,
        computer_choice=computer_choice,
        result=result
    )