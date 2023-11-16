class Kickboard:

    def __init__(self, id, lat, lng, danger):
        self.id = id
        self.lat = lat
        self.lng = lng
        self.cluster_id = -1
        self.danger = danger
        self.border = False


    def set_cluster_id(self, num):
        self.cluster_id = num

    def set_is_border(self, boolean):
        self.border = boolean

    def get_id(self):
        return self.id

    def get_coordinates(self):
        return {"lat": self.lat, "lng": self.lng}

    def json_return_dbscan(self):
        return {
                    'id': self.id,
                    'lat': self.lat,
                    'lon': self.lng,
                    'cluster_id': self.cluster_id,
                    'danger': self.danger,
                    'border': False
                }

    def json_return_convex(self):
        return {
                    'id': self.id,
                    'lat': self.lat,
                    'lon': self.lng,
                    'cluster_id': self.cluster_id,
                    'danger': self.danger,
                    'border': self.border
                }