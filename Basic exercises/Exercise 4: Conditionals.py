def scores(score):
    if 9 <= score <= 10:
        result = "A"
    elif 7.0 <= score <= 8.9:
        result = "B"
    elif 5.0 <= score <= 6.9:
        result = "C"
    elif 3.0 <= score <= 4.9:
        result = "D"
    elif 0.0 <= score <= 2.9:
        result = "E"
    return result

print("Score 9.5 -> ", scores(9.5))
print("Score 7.0 -> ", scores(7.0))
print("Score 5.5 -> ", scores(5.5))
print("Score 3.2 -> ", scores(3.2))
print("Score 1.0 -> ", scores(1.0))
