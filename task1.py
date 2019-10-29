new_dict = {}
a = []
size = int(input('enter dict size: '))
item = 0

while item < size:
    key = input('enter name: ')
    value = int(input('enter value: '))
    new_dict.update({key: value})
    item += 1

for i in new_dict.values():
    a.append(i)
a.sort()
for i, j in new_dict.items():
    while a[1] == j or a[2] == j:
        print('student {} has value {}'.format(i, j))
        break
print('dictionary = {} \nsort_list = {}'.format(new_dict, a))
