import math
from haversine import haversine

id1 = (37.44806369675929, 126.64803836321096)
id2 = (37.448860057232686, 126.65027257029978)
dist = haversine(id1, id2, unit="m")
def calc_dist(id1, id2):
    ret = math.pow(id1[0]-id2[0], 2) + math.pow(id1[1]-id2[1], 2)
    sqrt_ret = math.sqrt(ret)
    return sqrt_ret
print(calc_dist(id1, id2)) #0.0023718919282531416

