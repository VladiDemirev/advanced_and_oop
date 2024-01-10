# def age_assignment(*args, **kwargs):
#   name_age_dict = {}
#   sorted_names = []
#   for name_letter, age in kwargs.items():
#     for name in args:
#       if name.startswith(name_letter):
#         name_age_dict[name] = age
#   sorted_dict = sorted(name_age_dict.items())
#   for name, age in sorted_dict:
#     sorted_names.append(f"{name} is {age} years old.")
#   return '\n'.join(sorted_names)


# OPTION 2

def age_assignment(*args, **kwargs):
    name_age_dict = {}
    sorted_names = []
    for name in args:
        name_age_dict[name] = kwargs[name[0]]
    sorted_dict = sorted(name_age_dict.items())
    for name, age in sorted_dict:
        sorted_names.append(f"{name} is {age} years old.")
    return '\n'.join(sorted_names)


print(age_assignment("Peter", "George", G=26, P=19))

print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
