d = {'Harry': 37, 'Berry': 38, 'Tina': 36, 'Akriti': 41, 'Harsh': 39}
a = []
for i in d.values():
    a.append(i)
print(a)
a.sort()
print(a)
for i, j in d.items():
    while a[1] == j or a[2] == j:
        print(i, j)
        break
