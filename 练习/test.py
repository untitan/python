class User():
    def __init__(self, name=None, score=None):
        self.name = name;
        self.score = score

    def print_user(self):
        print('%s : %d' % (self.name, self.score))


zhangsan = User('titan', 80)

print(zhangsan)
print(zhangsan.name, zhangsan.score)

print(zhangsan.print_user())
