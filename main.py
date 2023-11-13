import requests
import json
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return getKicks()
    


def getKicks():
    url = "http://13.124.82.89:54401/kickboards"
    res = requests.get(url)
    if res.status_code == 200:
        return res.text
    else:
        return res.status_code