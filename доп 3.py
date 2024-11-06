data_structure = [
     [1, 2, 3],
    {'a': 4, 'b': 5},
      (6, {'cube': 7, 'drum': 8}),
     "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
    ]


def calculate_structure_sum(*items):
    summa = 0
    for item in items:
        if isinstance(item, (float,int)):
            summa += item
        elif isinstance(item, str):
            summa += len(item)
        elif isinstance(item, (list, tuple, set)):
            summa += calculate_structure_sum(*item)
        elif isinstance(item, dict):
            for key in item.items():
                summa += calculate_structure_sum(*item)
            for value in item.items():
                summa += calculate_structure_sum(*item)
     return summa



f = calculate_structure_sum(data_structure)
print(f)
