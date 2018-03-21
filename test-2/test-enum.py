from enum import Enum

Ind = Enum('Ind', ('Y', 'N'))

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

print(Ind)
print(Month)

for name, member in Ind.__members__.items():
    print(name, member)
