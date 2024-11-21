def custom_write(file_name, string):
    file = open(file_name, 'w', encoding='utf-8')
    strings_positions = {}

    for items in range(len(string)):
        a = file.tell()
        file.write(f'{string[items]}\n')
        strings_positions.update({(items + 1, a): string[items]})
    file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]
result = custom_write('Позиционирование в файле.txt', info)
for elem in result.items():
    print(elem)