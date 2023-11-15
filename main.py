import src.func.dbscan as dbscan
import src.func.requestAPI as requsetApi
import src.func.convex_calc as convex
from src.func.Kickboard import Kickboard

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return requsetApi.getKicks()

@app.get("/tmp")
async def root():
    dbscan_result = dbscan.DBSCAN(requsetApi.tmpOpenFile()) # Kickboard class List
    return ({ "items": [kick.json_return() for kick in dbscan_result] })

    #return convex.convex_call(dbscan_result)