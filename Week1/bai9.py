students = {
    "John": 75,
    "Mary": 45,
    "David": 80,
    "Anna": 55
}

def find_passed_students(students):
    for name, score in students.items():
        if score >= 50:
            print(f"{name} : {score}")

find_passed_students(students)