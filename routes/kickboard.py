from fastapi import APIRouter



kickboard_router = APIRouter()


@kickboard_router.get("/cluster")
async def cluster_kickboard(lat=float, lng=float):

    return "test"
