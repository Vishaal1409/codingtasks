def find_the_indices(user_string):
    user_string_lower = user_string.lower()
    pattern = "the"
    indices = []
    start = 0
    while True:
        index = user_string_lower.find(pattern, start)
        if index == -1:
            break
        indices.append(index)
        start = index + 1 
    return indices
if __name__ == "__main__":
    user_input = input("Enter a string: ")
    indices = find_the_indices(user_input)
    if indices:
        print("Indices where 'the' occurs:", indices)
    else:
        print("The word 'the' was not found in the given string.")