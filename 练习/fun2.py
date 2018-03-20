def fun1(i):
    for n in range(1, i):
        i *= n
    return i


print(fun1(5))


def fun2(n):
    if n == 1:
        return 1
    else:
        return n * fun1(n - 1)
n = fun2(5)
print(n)
