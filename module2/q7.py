import math
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
def closest_pair(points):
    n = len(points)
    if n <= 3:
        min_dist = float('inf')
        for i in range(n):
            for j in range(i + 1, n):
                dist = euclidean_distance(points[i], points[j])
                if dist < min_dist:
                    min_dist = dist
        return min_dist
    mid = n // 2
    mid_point = points[mid]
    d_left = closest_pair(points[:mid])
    d_right = closest_pair(points[mid:])
    d_min = min(d_left, d_right)
    strip = [p for p in points if abs(p[0] - mid_point[0]) < d_min]
    strip.sort(key=lambda p: p[1])
    min_dist_in_strip = float('inf')
    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            if (strip[j][1] - strip[i][1]) >= d_min:
                break
            dist = euclidean_distance(strip[i], strip[j])
            if dist < min_dist_in_strip:
                min_dist_in_strip = dist
    return min(d_min, min_dist_in_strip)
points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
points.sort()
min_distance = closest_pair(points)
print(f"The minimum distance between any two points is: {min_distance}")