new = ""
having = "23571113171923"
enter = "1 4 11"
idxs = enter.split()
for idx in idxs:
    i = int(idx) - 1
    el = having[i]
    new += el
print(new)
