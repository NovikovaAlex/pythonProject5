def is_prime(func):
    def wrapper(*args):
        res = func(*args)
        if res < 2:
            return f'Составное\n{res}'
        for i in range(2, int(res ** 0.5) + 1):
            if res % i == 0:
                return f'Составное\n{res}'
        return f'Простое \n{res}'
    return wrapper

@is_prime
def sum_three(*args):
    return sum(args)

result = sum_three(2, 3, 6)
print(result)
