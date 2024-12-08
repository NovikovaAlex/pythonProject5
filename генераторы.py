def all_variants(text):
    n = len(text)
    for i in range(1, 1 << n):
        a = ''
        for j in range(n):
            if i & (1 << j):
                a += text[j]
        yield a

a = all_variants("abc")
for i in a:
    print(i)