def apply_all_func(int_list, *functions):
    results = {}
    for function in functions:
        res = function(int_list)
        results.update({function.__name__:res})

    return results


def mini(int_list):
    return min(int_list)

def maxy(int_list):
    return max(int_list)

def leny(int_list):
    return len(int_list)

def summ(int_list):
    return sum(int_list)

def sort(int_list):
    return sorted(int_list)

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))