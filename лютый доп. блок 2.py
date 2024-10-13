print('Введите любое число от 3 до 20: ')
x = int(input())
key = []
print('Ваш код: ')
for i in range(1,x):
    for j in range(i,x):
        if x % (i + j) == 0 and i != j :
            key.append(str(i))
            key.append(str(j))
print(int(x),'-',*key, sep ='')







