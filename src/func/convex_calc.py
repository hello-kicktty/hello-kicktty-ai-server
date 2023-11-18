import math
from src.func.Kickboard import Kickboard


def ccw(kick1, kick2, kick3):
    val = (kick2.lng - kick1.lng) * (kick3.lat - kick2.lat) - (kick2.lat - kick1.lat) * (kick3.lng - kick2.lng)
    if val == 0:
        return 0
    return 1 if val > 0 else 2

def polar_angle(kick1, kick2):
    x_diff = kick2.lat - kick1.lat
    y_diff = kick2.lng - kick1.lng
    return math.atan2(y_diff, x_diff)

def graham_scan(kickboard_list_in_cluster):
    kickboard_num_in_cluster_id = len(kickboard_list_in_cluster)
    if kickboard_num_in_cluster_id < 3:
        return []
    # 점들 중 가장 아래에 있는 점을 찾음
    pivot_kick = min(kickboard_list_in_cluster, key=lambda kick: (kick.lat, kick.lng))


    # 극각에 따라 점들을 정렬
    kickboard_List_sorted_polar_angle = sorted(kickboard_list_in_cluster, key=lambda kick: (polar_angle(pivot_kick, kick), kick.lat, kick.lng))

    # Graham's Scan 알고리즘 적용
    convex = [pivot_kick, kickboard_List_sorted_polar_angle[0], kickboard_List_sorted_polar_angle[1]]

    for kick in kickboard_List_sorted_polar_angle[2:]:
        while len(convex) > 2 and ccw(convex[-2], convex[-1], kick) != 2:
            convex.pop()
        convex.append(kick)

    for kickIdx in range(len(convex)):
        convex[kickIdx].set_is_border(kickIdx)
        #print(convex[kickIdx].json_return_convex())


    return convex

def convex_call(kickboard_info_list):
    kickboard_cluster_id_dic = {}
    for kick in kickboard_info_list:
        if kick.cluster_id != -1:
            if kick.cluster_id in kickboard_cluster_id_dic.keys():
                kickboard_cluster_id_dic[kick.cluster_id].append(kick)
            else:
                kickboard_cluster_id_dic[kick.cluster_id] = [kick]
    for cluster_id in kickboard_cluster_id_dic.keys():
        cluster_list = kickboard_cluster_id_dic[cluster_id] # dictionary 각 cluster_id마다 배열이 존재
        result = graham_scan(cluster_list) # cluster_list는 각 cluster_id 마다의 list가 for를 통해 입력
    return sorted(kickboard_info_list, key=lambda kick: kick.cluster_id)