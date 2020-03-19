word = 'balafbdlkfbdk'

d = dict()
for c in word:
    #using get method
    '''
    if c in d:
        d[c] += 1
    else:
        d[c] = 0
    '''
    d[c] = d.get(c, 0) + 1

print(d)