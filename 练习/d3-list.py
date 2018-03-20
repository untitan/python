list = [123, 456]
list2 = [456, 789]

print(list > list2)

if list < list2 and list[1] > 123:
    print(111)
else:
    print(222)

print(list + list2)
print(list.append(list2))
print(list.extend(list2))

print(456 in list)

print(list)
print(len(list))


def arg():
    mix = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    mix.append('a')
    mix.extend(['b', 'c', 'd'])

    print(mix)

    name = mix.pop()
    print(name)
    print(mix)

    m = mix.copy()
    print(m)


arg()