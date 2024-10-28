

data_structure = [
     [1, 2, 3],
    {'a': 4, 'b': 5},
      (6, {'cube': 7, 'drum': 8}),
     "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
    ]
print(type([1, 2, 3]))
print(type({'a': 4, 'b': 5}))
print(type((6, {'cube': 7, 'drum': 8})))
print(type( 'Hello'))
print(type(((), [{(2, 'Urban', ('Urban2', 35))}])))
print(type(7))

def stroka (i):
    if isinstance(i, str):
        return len (i)
a = stroka('Hello')
print(a)

def spisok (i):
    if len(i) == 0:
        return i
    if len(i) == 1:
        return i[0]
    return i[0] + spisok(i[1:])

c = spisok([1, 2, 3])
print(c)

def slovar(i):
    spis = []
    spis_2 = []
    for keys, values in i.items():
        spis.append([keys,values])
    for sublist in spis:
        for items in sublist:
            spis_2.append(items)
    return ''.join(map(str, spis_2))
    



b = {'a': 4, 'b': 5}

print(slovar(b))