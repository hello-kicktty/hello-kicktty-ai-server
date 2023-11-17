import requests
import json
from pydantic import BaseModel
from fastapi import APIRouter
import src.func.dbscan as dbscan
import src.func.convex_calc as convex
import src.func.requestAPI as requestApi
from typing import List

kickboard_router = APIRouter()


@kickboard_router.post("/cluster")
async def cluster_kickboard(lat=float, lng=float):
    # dbscan_result : List of Kickboard class
    # dbscan_result = dbscan.DBSCAN(requsetApi.tmpOpenFile())  # Kickboard class List - using tmp local file
    dbscan_result = dbscan.DBSCAN(requestApi.getKicks())  # Kickboard class List - using by get method

    # convex_result : List of Kickboard class
    convex_result = convex.convex_call(dbscan_result)

    json_data = json.dumps([{"id": kick.id, "lat": kick.lat, "lng": kick.lng, "cluster_id": kick.cluster_id, "danger": kick.danger, "border": kick.border} for kick in convex_result])

    url = "http://3.35.50.22:59295/update" 
    headers = {"Content-Type": "application/json"}

    response = requests.post(url, data=json_data, headers=headers)

    return
