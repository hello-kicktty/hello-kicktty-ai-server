import src.func.dbscan as dbscan
import src.func.requestAPI as requsetApi
import src.func.convex_calc as convex
from src.func.Kickboard import Kickboard


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.kickboard import kickboard_router

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(kickboard_router)


@app.get("/")
async def root():
    return requsetApi.getKicks()


@app.get("/tmp")
async def root():
    dbscan_result = dbscan.DBSCAN(requsetApi.tmpOpenFile()) # Kickboard class List
    return ({ "items": [kick.json_return() for kick in dbscan_result] })

    #return convex.convex_call(dbscan_result)