# num_students = int(input())
# students_record = {}
# for _ in range(num_students):
#   name, grade = tuple(input().split())
#   grade = float(grade)
#   if name not in students_record:
#     students_record[name] = []
#   students_record[name].append(grade)

# for name, grades in students_record.items():
#   avg_grade = sum(grades) / len(grades)
#   print(f"{name} -> {' '.join([str(f'{x:.2f}') for x in grades])} (avg: {avg_grade:.2f})")


# OPTION 2

# def students_register(students):
#     students_record = {}
#     for _ in range(students):
#         name, grade = tuple(input().split())
#         grade = float(grade)
#         if name not in students_record:
#             students_record[name] = []
#         students_record[name].append(grade)
#     return students_record
#
#
# def students_info(students):
#     students_record = students_register(students)
#     for name, grades in students_record.items():
#         avg_grade = sum(grades) / len(grades)
#         print(f"{name} -> {' '.join([str(f'{x:.2f}') for x in grades])} (avg: {avg_grade:.2f})")
#
#
# num_students = int(input())
# students_info(num_students)


# OPTION 3

from collections import defaultdict


def students_register(students):
    # students_record = defaultdict(lambda: []) OR
    students_record = defaultdict(list)
    for _ in range(students):
        name, grade = tuple(input().split())
        grade = float(grade)
        students_record[name].append(grade)
    return students_record


def students_info(students):
    students_record = students_register(students)
    for name, grades in students_record.items():
        avg_grade = sum(grades) / len(grades)
        print(f"{name} -> {' '.join([str(f'{x:.2f}') for x in grades])} (avg: {avg_grade:.2f})")


num_students = int(input())
students_info(num_students)

