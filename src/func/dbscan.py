from collections import deque
from haversine import haversine

EPS = 2 # m(미터) 기준
MIN_CLUSTER = 3

class Kickboard:

    def __int__(self, id, lon, lat, cluseter_num, danger, suburb):
        self.id = id
        self.longitude = lon
        self.latitude = lat
        self.cluseter_num = cluseter_num
        self.danger = danger
        self.suburb = suburb

KickboardList = {} # { id : idValue, lat : latValue, lon : lonValue }

def data_input(kickboardlist):
    KickboardList = kickboardlist

def get_distance(kick_info1, kick_info2): # 위도 경도 기반 거리를 구하는 함수
    return haversine(kick_info1, kick_info2, unit="m")

visited = [False]*1000
adj = [[] for _ in range(1000)]  # 1000개의 서브리스트를 갖는 빈 리스트 초기화

cluster_count = 0

# [[(1,2),(2,3),(3,4)], [(2,3),(3,4),(4,5)]]

def bfs(start):
    queue = deque([start])
    cluster_sequence = []
    visited[start] = True
    isDangeSequence = False

    sorted_adj = [sorted(sublist, key=lambda x: x[0]) for sublist in adj]

    while queue:
        x = queue.popleft()
        cluster_sequence.append(x)

        for p in sorted_adj[start] :
            if p[0] > EPS : break
            if visited[p[1]] : continue
            visited[p[1]] = True
            queue.append(p[1])

            if KickboardList[p[1]].danger : isDangeSequence = True

    if len(cluster_sequence) < MIN_CLUSTER : return
    if isDangeSequence : return

    global cluster_count
    cluster_count += 1
    
    for v in cluster_sequence :
        KickboardList[v].cluster_number = cluster_count


def DBSCAN():
    for kick1_id, kick1_info in KickboardList.items():
        for kick2_id, kick2_info in KickboardList.items():
            if kick1_id <= kick2_id : continue
            dist = get_distance(kick1_info, kick2_info)
            adj[kick1_id].append((dist, kick2_id))
            adj[kick2_id].append((dist, kick1_id))

    for i in range(len(visited)) :
        if visited[i] == True : continue
        bfs(i)