from collections import deque
import math

EPS = 5 # m(미터) 기준
MIN_CLUSTER = 3

KickboardList = [] # { id : idValue, lat : latValue, lon : lonValue }



def get_distance(kick_info1, kick_info2): # 위도 경도 기반 거리를 구하는 함수
    tmp = math.sqrt(math.pow(kick_info1['lat'] - kick_info2['lat'], 2) + math.pow(kick_info1['lon'] - kick_info2['lon'], 2))
    dist = tmp * 0.00001
    # 1m = 0.00001
    #print(tmp)
    return dist

visited = [False]*1000
adj = []  # 1000개의 서브리스트를 갖는 빈 리스트 초기화

cluster_count = 0

# [[(1,2),(2,3),(3,4)], [(2,3),(3,4),(4,5)]]

def bfs(start):
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
    print(cluster_sequence)
    for v in cluster_sequence:
        KickboardList[v-1]['cluster_number'] = cluster_count
        #print(v, cluster_count)

def initial_global():
    global KickboardList
    global visited
    global adj
    global cluster_count
    KickboardList = []
    visited = [False]*1000
    adj = [[] for _ in range(1000)]  # 1000개의 서브리스트를 갖는 빈 리스트 초기화
    cluster_count = 0
    
def items(k_tmp):
    for i in k_tmp:
        KickboardList.append({
            'id': i['id'],
            'info': (i['lat'], i['lng'])
        })
    return

def organizeOtherCluster(k_tmp):
    for i in k_tmp:
        if 'cluster_number' not in i.keys():
            i['cluster_number'] = -1

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

def DBSCAN(k_tmp):
    initial_global()
    items(k_tmp)
    for i in KickboardList:
        kick1_id, kick1_info = i['id'], i['info']
        for j in KickboardList:
            kick2_id, kick2_info = j['id'], j['info']
            if kick1_id <= kick2_id : continue
            dist = get_distance(kick1_info, kick2_info)
            adj[kick1_id].append((dist, kick2_id))
            adj[kick2_id].append((dist, kick1_id))
    for i in range(len(adj)):
        adj[i] = list(sorted(adj[i], key=lambda x: x[0]))
    for i in range(len(visited)):
        if visited[i] == True: continue
        bfs(i)
    organizeOtherCluster(KickboardList)
    return makeReturnJson(KickboardList)