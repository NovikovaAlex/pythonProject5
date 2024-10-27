def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    return inner_function()

test_function() # функция вызвана, все в порядке
inner_function() #функция не может быть вызвана, так она существует только внутри test_function()