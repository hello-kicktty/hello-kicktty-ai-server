import src.func.dbscan as dbscan
import src.func.requestAPI as requsetApi

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return requsetApi.getKicks()

@app.get("/tmp")
async def root():
    return dbscan.DBSCAN(requsetApi.tmpOpenFile())