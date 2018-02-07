# coding=utf-8
import random

# i = int(input("猜数字："))

x = random.choice(range(100))
y = random.choice(range(200))
if x > y:
    print("x[%s] > y[%s]" % (x, y))
elif x == y:
    print("x[%s] = y[%s]" % (x, y))
else:
    print("x[%s] < y[%s]" % (x, y))
