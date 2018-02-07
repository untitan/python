import random

s = random.randint(2, 9)
print("正确数字:", s)
isEnd = False
errCount = 0
while not isEnd:
    if errCount >= 3:
        print("错误太多了。滚")
        break
    i = int(input("输入数字："))
    if i == s:
        print("正确")
        isEnd = True
    elif i > s:
        print("大了")
        errCount = errCount + 1
    elif i < s:
        print("小了")
        errCount = errCount + 1
