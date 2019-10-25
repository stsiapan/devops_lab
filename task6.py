a = 22
b = 33
while b != 0:
    a, b = b, a % b
print("NOD = {0}".format(a))
