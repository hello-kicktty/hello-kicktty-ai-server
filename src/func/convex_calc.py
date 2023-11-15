import math
from src.func.Kickboard import Kickboard



def ccw(p, q, r):
    val = (q['lon'] - p['lon']) * (r['lat'] - q['lat']) - (q['lat'] - p['lat']) * (r['lon'] - q['lon'])
    if val == 0:
        return 0
    return 1 if val > 0 else 2

def polar_angle(p, q):
    x_diff = q[0] - p[0]
    y_diff = q[1] - p[1]
    return math.atan2(y_diff, x_diff)

def graham_scan(points):
    n = len(points)
    if n < 3:
        return []
    # 점들 중 가장 아래에 있는 점을 찾음
    pivot = min(points, key=lambda p: (p['lon'], p['lat']))
    # 극각에 따라 점들을 정렬
    sorted_points = sorted(points, key=lambda p: polar_angle((pivot['lat'], pivot['lon']), (p['lat'], p['lon'])))
    # Graham's Scan 알고리즘 적용
    convex = [sorted_points[0], sorted_points[1]]
    for point in sorted_points[2:]:
        while len(convex) > 2 and ccw(convex[-2], convex[-1], point) != 2:
            convex.pop()
        point['border'] = True
        convex.append(point)
    print(convex)

    return convex

def organizeOtherKick(data):
    for i in range(len(data)):
        if 'border' in data[i].keys():
            pass
        else:
            data[i]['border'] = False

    return sorted(data, key=lambda x:x['cluster_num'])

def convex_call(k_tmp):
    returnArray = []
    kickboard_dic_arr_dic = {}
    for i in k_tmp:
        if i['cluster_num'] == -1:
            returnArray.append(i)
            continue
        else:
            if i['cluster_num'] in kickboard_dic_arr_dic:
                kickboard_dic_arr_dic[i['cluster_num']].append(i)
            else:
                kickboard_dic_arr_dic[i['cluster_num']] = [i]
    for i in kickboard_dic_arr_dic.keys():
        positions = kickboard_dic_arr_dic[i] # dictionary 각 키마다 배열이 존재
        result = graham_scan(positions)
        returnArray += result

    return organizeOtherKick(returnArray)