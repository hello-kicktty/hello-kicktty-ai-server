from pydantic import BaseModel


class Kickboard(BaseModel):
    id: int
    lat: float
    lng: float
    cluster_id: int
    danger: bool
    border: bool

    class ConfigDict:
        json_schema_extra = {
            "example": {
                "id": 203,
                "lat": 37.44770920973431,
                "lng": 126.64792654504153,
                "cluster_id": 4,
                "danger": False,
                "border": False,
            }
        }
