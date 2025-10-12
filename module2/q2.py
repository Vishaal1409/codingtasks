def get_combinations(elements, k):
    if k == 0:
        return [[]]
    if not elements or k > len(elements):
        return []
    first_element = elements[0]
    remaining_elements = elements[1:]
    combinations_without_first = get_combinations(remaining_elements, k)
    combinations_with_first = []
    for combo in get_combinations(remaining_elements, k - 1):
        combinations_with_first.append([first_element] + combo)
    return combinations_without_first + combinations_with_first
print("Combinations of size 2 from [1, 2, 3, 4]:")
print(get_combinations([1, 2, 3, 4], 2))
print("\nCombinations of size 3 from ['a', 'b', 'c', 'd']:")
print(get_combinations(['a', 'b', 'c', 'd'], 3))