dict1 = {}
dict1 = dict1.fromkeys((1, 2, 3, 4, 5))

print(dict1)

dict1 = dict1.fromkeys((1, 3, 5), True)
print(dict1)

for k in dict1.keys():
    print(k)

for v in dict1.values():
    print(v)

for k, v in dict1.items():
    print(k, v)

s = dict1.get(33, 404)
print(s)

dict2 = {1, 2, 2, 3, 3, 3}
print(dict2)

set1 = set([2, 1, 3, 4, 5,5,5,5])
print(set1)
