import pandas as pd

def ccw(x1, y1, x2, y2, x3, y3):
    c = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
    return c < 0

def convex_hull(positions):
    convex = []  # set으로 변경
    non_convex = []
    for p3 in positions:
        while len(convex) >= 3:
            p1, p2 = convex[-2], convex[-1]
            if ccw(p1['lat'], p1['lon'], p2['lat'], p2['lon'], p3['lat'], p3['lon']):
                break
            non_convex.append(convex.pop())
        convex.append(p3)  # set에 추가하는 방식으로 변경

    return [convex, non_convex]  # set을 다시 list로 변환하여 반환

def convex_call(k_tmp):
    returnArray = []
    kickboard_dic_arr_dic = {}
    for i in k_tmp:
        if i['cluster_num'] == -1:
            continue
        else:
            if i['cluster_num'] in kickboard_dic_arr_dic:
                kickboard_dic_arr_dic[i['cluster_num']].append(i)
            else:
                kickboard_dic_arr_dic[i['cluster_num']] = [i]
    for i in kickboard_dic_arr_dic.keys():
        positions = kickboard_dic_arr_dic[i]
        #print(positions)
        positions = sorted(positions, key=lambda x: (x['lat'], x['lon']))
        tmp1 = convex_hull(positions)
        #tmp2 = convex_hull(positions[::-1])
        sh = tmp1[0]# + tmp2[0]
        #sh = list({v['id']: v for v in shx}.values())
        none_sh = tmp1[1]# + tmp2[1]
        #none_sh = list({v['id']: v for v in none_shx}.values())
        #for i in sh:
            #if i in none_sh:
                #none_sh.remove(i)
    #positions = [(0,3), (1,1), (2,2), (4,4), (0,0), (1,2), (3,1), (3,3)]
    #positions = sorted(positions, key=lambda pos: (pos[0], pos[1]))
    #sh = convex_hull(positions) + convex_hull(positions[::-1])
        sorted_sh = sorted(sh, key=lambda x: (x['lat'], x['lon']))
        for i in range(len(sorted_sh)):
            tmpData = sorted_sh[i]
            tmpData['border'] = True
            returnArray.append(tmpData)
        for i in range(len(none_sh)):
            tmpData = none_sh[i]
            tmpData['border'] = False
            returnArray.append(tmpData)

    return returnArray