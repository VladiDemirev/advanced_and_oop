def fill_the_box(*args):
    box_area = int(args[0]) * int(args[1]) * int(args[2])
    cubes_area = 0
    for arg in args[3:]:
        if arg == "Finish":
            break
        cubes_area += int(arg)
    if cubes_area <= box_area:
        return f"There is free space in the box. You could put {box_area - cubes_area} more cubes."
    return f"No more free space! You have {cubes_area - box_area} more cubes."


#  TEST CODE

print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print()
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print()
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
