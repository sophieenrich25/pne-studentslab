student = {
    "name": "Carlos",
    "age": 22,
    "subjects": ["PNE", "Networks", "Databases"],
    "grades": {"PNE": 8.5, "Networks": 7.0, "Databases": 9.2}
}

print("Name:", student["name"])
print("Number of subjects:", len(student["subjects"]))
print("Enrolled in PNE:", "PNE" in student["subjects"])
print("Databases grade:", student["grades"]["Databases"])

grades = student["grades"].values()
average = round(sum(grades) / len(grades), 2)
print("Average grade:", average)

print("Subject grades:")
for subject, grade in student["grades"].items():
    print(f"  {subject}: {grade}")
