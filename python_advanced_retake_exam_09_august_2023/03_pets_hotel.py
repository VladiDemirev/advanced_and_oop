#  OPTION 1 (NOT MINE) - 100/100

# def accommodate_new_pets(*args, **kwargs):
#     result = []
#     information_gather = {}
#     available_capacity = int(args[0])
#     maximum_weight_limit = float(args[1])
#     pet_information = args[2:]
#     pets_counter = 0
#     for information in pet_information:
#         type_of_pet = information[0]
#         weight = float(information[1])
#         if available_capacity:
#             if maximum_weight_limit >= weight:
#                 available_capacity -= 1
#                 if type_of_pet not in information_gather:
#                     information_gather[type_of_pet] = 0
#                 information_gather[type_of_pet] += 1
#             pets_counter += 1
#         if not available_capacity:
#             break
#     if pets_counter == len(pet_information):
#         result.append(f"All pets are accommodated! Available capacity: {available_capacity}.")
#     else:
#         result.append("You did not manage to accommodate all pets!")
#     result.append("Accommodated pets:")
#     for pet, weight in sorted(information_gather.items(), key=lambda x: x[0]):
#         result.append(f"{pet}: {weight}")
#     return '\n'.join(result)


#  OPTION 2 (MINE REVISED) - 100/100

def accommodate_new_pets(hotel_capacity, max_weight, *args):
    pets = []
    for type, weight in args:
        pets.append([type, weight])
    accommodated_pets = {}
    pets_counter = 0

    while True:
        for pet_type, pet_weight in pets:

            if pet_weight <= max_weight:
                if pet_type not in accommodated_pets:
                    accommodated_pets[pet_type] = 0
                accommodated_pets[pet_type] += 1
                hotel_capacity -= 1
            pets_counter += 1
            if not hotel_capacity:
                break
        if pets_counter == len(pets):
            result = f"All pets are accommodated! Available capacity: {hotel_capacity}."
        else:
            result = "You did not manage to accommodate all pets!"
        break

    result += f"\nAccommodated pets:"
    for pet, count in sorted(accommodated_pets.items()):
        result += f"\n{pet}: {count}"

    return result




# 66/100 in JUDGE - 100/100 when added used_capacity == 0 in line 77

# def accommodate_new_pets(hotel_capacity, max_weight, *args):
#     pets = []
#     # max_capacity = hotel_capacity
#     for type, weight in args:
#         pets.append([type, float(weight)])
#     accomodated_pets = {}
#     used_capacity = len(pets)
#
#     while hotel_capacity > 0 or used_capacity == 0:
#         if used_capacity == 0:
#             result = f"All pets are accommodated! Available capacity: {hotel_capacity}."
#             break
#         for pet_type, pet_weight in pets:
#             if hotel_capacity == 0:
#                 break
#             if pet_weight > max_weight:
#                 used_capacity -= 1
#                 continue
#             elif pet_type not in accomodated_pets:
#                 accomodated_pets[pet_type] = 0
#             accomodated_pets[pet_type] += 1
#             hotel_capacity -= 1
#             used_capacity -= 1
#     else:
#         result = "You did not manage to accommodate all pets!"
#
#     result += f"\nAccommodated pets:"
#     for pet, count in sorted(accomodated_pets.items()):
#         result += f"\n{pet}: {count}"
#
#     return result

print(accommodate_new_pets(
    10,
    15.0,
    ("cat", 5.8),
    ("dog", 10.0),
))

print(accommodate_new_pets(
    10,
    10.0,
    ("cat", 5.8),
    ("dog", 10.5),
    ("parrot", 0.8),
    ("cat", 3.1),
))

print(accommodate_new_pets(
    2,
    15.0,
    ("dog", 10.0),
    ("cat", 5.8),
    ("cat", 2.7),
))