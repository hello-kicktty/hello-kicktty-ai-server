def ccw(x1, y1, x2, y2, x3, y3):
    c = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
    return c < 0

def convex_hull(positions):
    convex = []  # set으로 변경
    for p3 in positions:
        while len(convex) >= 2:
            p1, p2 = convex[-2], convex[-1]
            if ccw(*p1, *p2, *p3):
                break
            convex.pop()
        convex.append(p3)  # set에 추가하는 방식으로 변경

    return convex  # set을 다시 list로 변환하여 반환

positions = [(0,3), (1,1), (2,2), (4,4), (0,0), (1,2), (3,1), (3,3)]
positions = sorted(positions, key=lambda pos: (pos[0], pos[1]))

sh = convex_hull(positions) + convex_hull(positions[::-1])
sorted_sh = sorted(set(sh), key=lambda pos: (pos[0], pos[1]))
print(sorted_sh)