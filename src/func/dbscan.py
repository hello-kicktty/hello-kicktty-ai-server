from collections import deque
import math
from src.func.Kickboard import Kickboard

EPS = 7 # m(미터) 기준
MIN_CLUSTER = 7

def get_distance(kick_info1, kick_info2): # 위도 경도 기반 거리를 구하는 함수
    tmp = math.sqrt(math.pow(kick_info1['lat'] - kick_info2['lat'], 2) + math.pow(kick_info1['lng'] - kick_info2['lng'], 2))
    dist = tmp * 100000
    # 1m = 100000
    #print(tmp)

    return dist

visited = [False]*1000
adj = []  # 1000개의 서브리스트를 갖는 빈 리스트 초기화

cluster_count = -1

# [[(1,2),(2,3),(3,4)], [(2,3),(3,4),(4,5)]]

def bfs(kickboard_info_list, start): # start는 정수
    queue = deque([start])
    cluster_sequence = []
    visited[start] = True
    isDangeSequence = False
    
    while queue:
        x = queue.popleft()
        cluster_sequence.append(x)

        for p in adj[x] :
            if p[0] > EPS : break
            if visited[p[1]] : continue
            visited[p[1]] = True
            queue.append(p[1])

            
            #if KickboardList[p[1]].danger : isDangeSequence = True

    if len(cluster_sequence) < MIN_CLUSTER :
        return
    if isDangeSequence : return

    global cluster_count
    cluster_count += 1
    print(cluster_count)
    print(cluster_sequence)
    for v in cluster_sequence:
        kickboard_info_list[v-1].set_cluster_id(cluster_count)
        #print(v, cluster_count)

def initial_global():
    global visited
    global adj
    global cluster_count
    visited = [False] * 1000
    adj = [[] for _ in range(1000)]  # 1000개의 서브리스트를 갖는 빈 리스트 초기화
    cluster_count = -1



def makeReturnJson(k_tmp):
    arr = []
    for i in k_tmp:
        arr.append({
            'id': i['id'],
            'lat': i['info'][0],
            'lon': i['info'][1],
            'cluster_num': i['cluster_number']
        })
    return arr

def DBSCAN(kickboard_info_list):
    initial_global()
    for kick1 in kickboard_info_list:
        for kick2 in kickboard_info_list:
            if kick1.get_id() <= kick2.get_id() : continue
            dist = get_distance(kick1.get_coordinates(), kick2.get_coordinates())
            #print(dist)
            adj[kick1.get_id()].append((dist, kick2.get_id()))
            adj[kick2.get_id()].append((dist, kick1.get_id()))

    for i in range(len(adj)):
        adj[i] = list(sorted(adj[i], key=lambda x: x[0]))
    for i in range(len(visited)):
        if visited[i] == True: continue
        bfs(kickboard_info_list, i)

    return kickboard_info_list