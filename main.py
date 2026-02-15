"""
Markets:
    'A' = Auchan
    'C' = Continente
    'P' = Pingo doce
"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def home():
    return {"message": "Home Page"}


@app.get("/status")
async def status():
    return "Api was working"
