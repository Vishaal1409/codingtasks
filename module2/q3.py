import random
def check_binary_digit(n):
    if not isinstance(n, int):
        print("Input must be an integer.")
        return
    binary_string = format(n, 'b')
    print(f"The integer {n} in binary is: {binary_string}")
    if not binary_string:
        print("Cannot check a position for this integer.")
        return
    random_position = random.randint(0, len(binary_string) - 1)
    digit = binary_string[random_position]
    print(f"The random position selected is: {random_position}")
    print(f"The digit at this position is: {digit}")
    if digit == '0' or digit == '1':
        print(True)
    else:
        print(False)
check_binary_digit(42)