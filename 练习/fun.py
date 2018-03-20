def userinfo(name, age, *, sex=None, city=None):
    # print(name)
    # print(age)
    # print(sex)
    # print(city)
    pass


userinfo('zhangsan', 18, city='beijing')


def list(l=[]):  # 函数定义时，已初始化l=[]，放在内存中
    l.append('end')
    print(l)


# list()
# list()


def list2(l=None):
    if l == None:
        l = []
        print('初始化：l')
    l.append('end')
    print(l)


# list2()
# list2()


def sum(*num):
    sum = 0
    for n in num:
        sum += n

    print(sum)


sum(1, 2, 3, 4, 5)  # 类似java sum(String... strs)


def userinfo2(name, age, **kw):
    print(name)
    print(age)
    print(type(kw), kw)
    print(kw['sex'])
    print(kw['isChannelSend'])
    if 'idNo' in kw:
        print(kw['idNo'])


userinfo2('zhangsan', '19', sex='M', city='beijing', isChannelSend=False)

extends = {'idNo': '220101199001010011'}
userinfo2('zhangsan', '19', sex='M', city='beijing', isChannelSend=False, **extends)

