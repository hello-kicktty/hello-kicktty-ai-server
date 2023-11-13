import src.func.dbscan as dbscan
import src.func.requestAPI as requsetApi
import src.func.convex_calc as convex

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return requsetApi.getKicks()

@app.get("/tmp")
async def root():
    dbscan_result = dbscan.DBSCAN(requsetApi.tmpOpenFile())
    return convex.convex_call(dbscan_result)