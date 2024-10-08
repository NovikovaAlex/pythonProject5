print('Введите любое число от 3 до 20: ')
x = int(input())
key = []
print('Ваш код: ')
for i in range(1,20):
    if i == 1:
        is_prime = True
    for j in range(i,20):
        if x % (i + j) == 0 and i != j :
            key.append(i)
            if is_prime:
                key.append(j)
                continue

print(int (x),':', *(key))







