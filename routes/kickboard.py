from fastapi import APIRouter
import src.func.dbscan as dbscan
import src.func.convex_calc as convex
import src.func.requestAPI as requestApi



kickboard_router = APIRouter()


@kickboard_router.get("/cluster")
async def cluster_kickboard(lat=float, lng=float):
    # dbscan_result : List of Kickboard class
    # dbscan_result = dbscan.DBSCAN(requsetApi.tmpOpenFile())  # Kickboard class List - using tmp local file
    dbscan_result = dbscan.DBSCAN(requestApi.getKicks())  # Kickboard class List - using by get method

    # return ({ "items": [kick.json_return_dbscan() for kick in dbscan_result] })

    # convex_result : List of Kickboard class
    convex_result = convex.convex_call(dbscan_result)
    return ({ "items": [kick.json_return_convex() for kick in convex_result] })
