def gather_credits(*args):
    needed_credits = int(args[0])
    courses_info = args[1:]
    enrolled_courses = []
    gathered_credits = 0

    # for course_name, course_credits in courses_info:
    for course_info in courses_info:
        course_name = course_info[0]
        course_credits = int(course_info[1])

        if gathered_credits >= needed_credits:
            break

        if course_name not in enrolled_courses:
            enrolled_courses.append(course_name)
            gathered_credits += course_credits

    if gathered_credits >= needed_credits:
        return f"Enrollment finished! Maximum credits: {gathered_credits}.\nCourses: {', '.join(sorted(enrolled_courses))}"
    return f"You need to enroll in more courses! You have to gather {needed_credits - gathered_credits} credits more."


#   100/100


# def gather_credits(*args):
#     needed_credits = int(args[0])
#     courses_info = args[1:]
#     enrolled_courses = []
#     gathered_credits = 0
#     result = ""
#
#     for course_name, course_credits in courses_info:
#
#         if gathered_credits >= needed_credits:
#             result = f"Enrollment finished! Maximum credits: {gathered_credits}.\nCourses: {', '.join(sorted(enrolled_courses))}"
#             break
#
#         if course_name not in enrolled_courses:
#             enrolled_courses.append(course_name)
#             gathered_credits += course_credits
#
#         if gathered_credits >= needed_credits:
#             result = f"Enrollment finished! Maximum credits: {gathered_credits}.\nCourses: {', '.join(sorted(enrolled_courses))}"
#             break
#
#     if gathered_credits >= needed_credits:
#         result = f"Enrollment finished! Maximum credits: {gathered_credits}.\nCourses: {', '.join(sorted(enrolled_courses))}"
#     else:
#         result = f"You need to enroll in more courses! You have to gather {needed_credits - gathered_credits} credits more."
#
#     return result


print(gather_credits(
    1,
    ("Basics", 0),
("Advanced", 2),
("Advanced", 2)
))

# print(gather_credits(
#     80,
#     ("Advanced", 30),
#     ("Basics", 27),
#     ("Fundamentals", 27),
# ))
#
# print(gather_credits(
#     60,
#     ("Basics", 27),
#     ("Fundamentals", 27),
#     ("Advanced", 30),
#     ("Web", 30)
# ))

