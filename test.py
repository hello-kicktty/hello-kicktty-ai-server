import math

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
        while len(convex) > 1 and ccw(convex[-2], convex[-1], point) != 2:
            convex.pop()
        convex.append(point)

    return convex

# 예제 사용
positions = [
    {"id": 1, "lat": 0, "lon": 3},
    {"id": 2, "lat": 1, "lon": 1},
    {"id": 3, "lat": 2, "lon": 2},
    {"id": 4, "lat": 4, "lon": 4},
    {"id": 5, "lat": 0, "lon": 0},
    {"id": 6, "lat": 1, "lon": 2},
    {"id": 7, "lat": 3, "lon": 1},
    {"id": 8, "lat": 3, "lon": 3}
]

result = graham_scan(positions)

# Convex Hull 출력
print("Convex Hull:")
for point in result:
    print(f"({point['lat']}, {point['lon']})", end=" ")