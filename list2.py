a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0,]
b = []

for x in a:
    if x not in b:
        b.append(x)
print(b)
