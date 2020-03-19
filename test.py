d = {'a':10, 'b':1, 'c':22}
t = list(d.items())
res = list()
for key, value in t:
    res.append((value, key))
res.sort()
print(res)