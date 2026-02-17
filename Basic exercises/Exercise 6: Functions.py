def is_even(number):
    return number % 2 == 0

def classify_triangle(a, b, c):
    if a == b == c:
        return "equilateral"
    elif a == b or a == c or b == c:
        return "isosceles"
    else:
        return "scalene"

print(is_even(4))
print(is_even(7))
print(is_even(0))
print(is_even(-3))
print(is_even(10))

print("classify_triangle(5, 5, 5) =", classify_triangle(5, 5, 5))  # equilateral
print("classify_triangle(3, 3, 4) =", classify_triangle(3, 3, 4))  # isosceles
print("classify_triangle(3, 4, 5) =", classify_triangle(3, 4, 5))  # scalene
