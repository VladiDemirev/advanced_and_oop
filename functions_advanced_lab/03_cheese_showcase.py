def sorting_cheeses(**kwargs):
    final_result = ""
    sorted_list = sorted(kwargs.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
    for cheese, quantities in sorted_list:
        quantities = sorted(quantities, reverse=True)
        result = cheese + '\n' + '\n'.join(str(x) for x in quantities) + '\n'
        final_result += result
    return final_result


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)

print(
    sorting_cheeses(
        Parmigiano=[165, 215],
        Feta=[150, 515],
        Brie=[150, 125]
    )
)
