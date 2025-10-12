import itertools
distances = [
    [0, 10, 8, 12, 15],  # A to A, B, C, D, E
    [10, 0, 9, 11, 14],  # B to A, B, C, D, E
    [8, 9, 0, 13, 10],   # C to A, B, C, D, E
    [12, 11, 13, 0, 16], # D to A, B, C, D, E
    [15, 14, 10, 16, 0]  # E to A, B, C, D, E
]
def solve_tsp_brute_force(cities, dist_matrix):
    start_city = cities[0]
    other_cities = cities[1:]
    all_permutations = list(itertools.permutations(other_cities))
    min_distance = float('inf')
    optimal_route = None
    for p in all_permutations:
        current_route = [start_city] + list(p) + [start_city]
        current_distance = 0
        for i in range(len(current_route) - 1):
            city1 = current_route[i]
            city2 = current_route[i+1]
            current_distance += dist_matrix[city1][city2]
        if current_distance < min_distance:
            min_distance = current_distance
            optimal_route = current_route
    return min_distance, optimal_route
cities = [0, 1, 2, 3, 4]
min_dist, best_route = solve_tsp_brute_force(cities, distances)
city_names = ['A', 'B', 'C', 'D', 'E']
readable_route = ' -> '.join([city_names[city] for city in best_route])
print(f"The minimum distance is: {min_dist}")
print(f"The optimal route is: {readable_route}")