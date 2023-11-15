class Kickboard:
    def __init__(self, id, lat, lng):
        self.id = id
        self.lat = lat
        self.lng = lng
        self.cluster_id = -1
        self.danger = False
        self.border = False

    def set_cluster_id(self, num):
        self.cluster_id = num

    def set_is_border(self, boolean):
        self.border = boolean

    def get_id(self):
        return self.id

    def get_coordinates(self):
        return {"lat": self.lat, "lng": self.lng}

    def json_return(self):
        return {
                    'id': self.id,
                    'lat': self.lat,
                    'lon': self.lng,
                    'cluster_id': self.cluster_id
                }