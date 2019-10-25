import random
matrix = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(random.randint(0, 9))
    matrix.append(row)
for row in matrix:
    print(row)
a = (matrix[0][0] + matrix[1][1] + matrix[2][2])
b = (matrix[0][2] + matrix[1][1] + matrix[2][0])
summ = a - b
print("summa= ", summ)
