#def password(*args):
print('Введите любое число от 3 до 20: ')
#pin = {'x': []}
 #   pin = []
x = int(input())
key = []
print('Ваш код: ')
for i in range(1,20):
    if i == 1:
        is_prime = True
    for j in range(i,20):
        if x % (i + j) == 0 and i != j:
            key.append(j)
            if is_prime:
                key.append(i)
                continue
print(int (x), (key))





#for i in range(1, 21):
 #   if x % y == 0:
  #      continue
#x % (a + b) == 0
#a != b
# через имя? "х": у






