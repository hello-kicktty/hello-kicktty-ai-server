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

    #for kick in convex:
    #    kick.set_is_border(True)
    #print(convex)


    return convex

#
def sort_points_clockwise(center, points):
    # center를 기준으로 각도에 따라 정렬하는 함수
    def angle_key(point):
        x, y = point.lat - center.lat, point.lng - center.lng
        return math.atan2(y, x)

    # center를 기준으로 각도에 따라 정렬
    sorted_points = sorted(points, key=angle_key)
    for kickIdx in range(len(sorted_points)):
        sorted_points[kickIdx].set_is_border(kickIdx)

    #print([i.id for i in sorted_points])
    #print([i.border for i in sorted_points])
    return sorted_points



def convex_call(kickboard_info_list):
    kickboard_cluster_id_dic = {}
    for kick in kickboard_info_list:
        if kick.cluster_id != -1:
            if kick.cluster_id in kickboard_cluster_id_dic.keys():
                kickboard_cluster_id_dic[kick.cluster_id].append(kick)
            else:
                kickboard_cluster_id_dic[kick.cluster_id] = [kick]
    for cluster_id in kickboard_cluster_id_dic.keys():
        #print("id: " + str(cluster_id))
        cluster_list = kickboard_cluster_id_dic[cluster_id] # dictionary 각 cluster_id마다 배열이 존재
        result = graham_scan(cluster_list) # cluster_list는 각 cluster_id 마다의 list가 for를 통해 입력
        # 스택의 첫 번째 원소를 기준으로 시계 방향으로 정렬
        result_sort = sorted(result, key=lambda kick: kick.lng)
        center_point = result_sort[0]
        sorted_clockwise = sort_points_clockwise(center_point, result_sort)
    return sorted(kickboard_info_list, key=lambda kick: kick.cluster_id)