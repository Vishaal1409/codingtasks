def get_permutations(elements):
    if len(elements) <= 1:
        return [elements]
    all_perms = []
    for i, first_element in enumerate(elements):
        remaining_elements = elements[:i] + elements[i+1:]
        for perm in get_permutations(remaining_elements):
            all_perms.append([first_element] + perm)
    return all_perms
print("Permutations for numbers:")
print(get_permutations([1, 2, 3]))