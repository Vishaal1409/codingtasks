def get_combinations(elements):
    result = [[]]
    for item in elements:
        result.extend([combo + [item] for combo in result])
    return result[1:] 
def solve_knapsack_combinations(items, capacity):
    max_value = 0
    best_combination = []
    all_combinations = get_combinations(items)
    for combo in all_combinations:
        current_weight = 0
        current_value = 0
        for weight, value in combo:
            current_weight += weight
            current_value += value
        if current_weight <= capacity and current_value > max_value:
            max_value = current_value
            best_combination = combo
    return max_value, best_combination
items = [(1, 10), (2, 20), (3, 30), (4, 40), (5, 50), (6, 60)]
knapsack_capacity = 10
max_val, optimal_items = solve_knapsack_combinations(items, knapsack_capacity)
print(f"The maximum value that can be obtained is: {max_val}")
print(f"The optimal combination of items is: {optimal_items}")