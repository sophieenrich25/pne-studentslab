def average(grades):
    return sum(grades) / len(grades)

def get_status(avg):
    if avg >= 5.0:
        return "PASS"
    else:
        return "FAIL"

students = [
    {"name": "Ana", "grades": [8.5, 7.0, 9.0]},
    {"name": "Luis", "grades": [5.0, 4.5, 6.0]},
    {"name": "Maria", "grades": [9.5, 9.0, 10.0]},
    {"name": "Pedro", "grades": [3.0, 4.0, 2.5]},
    {"name": "Sofia", "grades": [7.0, 7.5, 8.0]},
]

passed = 0
failed = 0
for student in students:
    avg = round(average(student["grades"]), 1)
    status = get_status(avg)

    print(f"{student['name']}: {avg} -> {status}")

    if status == "PASS":
        passed += 1
    else:
        failed += 1

print(f"Results: {passed} passed, {failed} failed")


