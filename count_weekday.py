fhand = open('mbox-short.txt')

# count week days
'''
days = dict()
for line in fhand:
    if line.startswith('From '):
        words = line.split()
        days[words[2]] = days.get(words[2], 0) + 1

for key in days.keys():
    print(key, days[key])
'''

'''
# count senders
senders = dict()

for line in fhand:
    if line.startswith('From '):
        words = line.split()
        senders[words[1]] = senders.get(words[1], 0) + 1

freq = list()
for key, val in list(senders.items()):
    freq.append((val, key))

freq.sort(reverse=True)
print(freq[0])
'''

'''
# count domain names
domains = dict()
for line in fhand:
    if line.startswith('From '):
        words = line.split()
        e_addr = words[1].split('@')
        domain = e_addr[1]
        domains[domain] = domains.get(domain, 0) + 1

print(domains)
'''

#count hour distribution
hours = dict()

for line in fhand:
    if line.startswith('From '):
        words = line.split()
        time_point = words[len(words) - 2].split(':')
        hour = time_point[0]
        hours[hour] = hours.get(hour, 0) + 1

hours_tup = list()
for key, val in list(hours.items()):
    hours_tup.append((key, val))
hours_tup.sort()
for key, val in hours_tup:
    print(key, val)
