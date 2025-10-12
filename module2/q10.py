def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y
    n = max(len(str(x)), len(str(y)))
    k = n // 2
    a = x // (10**k)
    b = x % (10**k)
    c = y // (10**k)
    d = y % (10**k)
    p1 = karatsuba(a, c)
    p2 = karatsuba(b, d)
    p3 = karatsuba(a + b, c + d)
    result = p1 * (10**(2 * k)) + (p3 - p1 - p2) * (10**k) + p2
    return result
num1 = 123456789123456789
num2 = 987654321987654321
expected_result = num1 * num2
karatsuba_result = karatsuba(num1, num2)
print(f"Number 1: {num1}")
print(f"Number 2: {num2}")
print(f"Result using Karatsuba: {karatsuba_result}")
print(f"Result using standard multiplication: {expected_result}")
print(f"Match: {karatsuba_result == expected_result}")