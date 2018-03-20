class Animal(object):
    def run(self):
        print('%s is running' % self.name)


class Rabbit(Animal):
    def __init__(self, name):
        self.name = name


class Fish(Animal):
    def __init__(self, name):
        self.name = name


rabbit = Rabbit('兔子')

fish = Fish('鱼')

print(rabbit.run())
print(fish.run())

print(isinstance(rabbit, Animal))

print(hasattr(rabbit, 'name'))

print(setattr(rabbit, 'age', 20))

print(getattr(rabbit, 'age1', 404))


class C:
    def __init__(self, size=100):
        self.size = size

    def set_name(self, size):
        self.size = size
    def get_name(self):
        return self.size
    x = property(get_name, set_name, None)


c = C()
print(c.x)
c.x=19


class new_int(int):
    def __add__(self, other):
        return int.__sub__(self,other)

i = new_int()
