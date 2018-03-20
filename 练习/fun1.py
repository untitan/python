from types import MethodType


class User(object):
    def __init__(self):
        pass


def set_name(self, name):
    self.name = name


user1 = User()
user1.set_name = MethodType(set_name, user1)
user1.set_name('zhangsan')
print(user1.name)


def funX():
    x = 5

    def funY():
        # nonlocal x
        return x * x

    return funY()


print(funX())

_temp_fun = lambda x, y: x * y

print(_temp_fun(2, 9))

f = filter(lambda x: x % 2, range(10))
print(list(f))

f = map(lambda x: x + 100, range(10))
print(list(f))

