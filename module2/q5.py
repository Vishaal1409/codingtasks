def solve_knapsack_brute_force(items, capacity):
    num_items = len(items)
    max_value = 0
    best_combination = None
    num_combinations = 2**num_items
    for i in range(num_combinations):
        current_weight = 0
        current_value = 0
        binary_representation = format(i, f'0{num_items}b')
        current_combination = []
        for j in range(num_items):
            if binary_representation[j] == '1':
                weight, value = items[j]
                current_weight += weight
                current_value += value
                current_combination.append(items[j])
        if current_weight <= capacity and current_value > max_value:
            max_value = current_value
            best_combination = current_combination
    return max_value, best_combination
items = [(1, 10), (2, 20), (3, 30), (4, 40), (5, 50), (6, 60)]
knapsack_capacity = 10
max_val, optimal_items = solve_knapsack_brute_force(items, knapsack_capacity)
print(f"The maximum value that can be obtained is: {max_val}")
print(f"The optimal combination of items is: {optimal_items}")