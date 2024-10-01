first_name=int(input('Введите первое число: '))
second_name=int(input('Введите второе число: '))
third_name=int(input('Введите третье число: '))
if first_name==second_name==third_name:
    print(3)
elif first_name==second_name or first_name==third_name or second_name==third_name:
    print(2)
else:
    print(0)
