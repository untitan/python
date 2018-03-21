list = 'hello'

for l in list:
    print(l, list.index(l))

for y in 'ABC':
    print(y)

for i, value in enumerate('ABC', 1):
    print(i, value)

#print(x * x for x in range(10))

dt = {
    "exSystem": "111",
    "exBizOrderId": "20180501{{$randomInt}}",
    "exMerTxnSeq": "20180501{{$randomInt}}",
    "vCardNo": 1111,
    "txnBrief": "一箱大可乐",
    "txnAmt": "100",
    "txnTime": "{{$timestamp}}",
    "terminalType": "WECHAT"
}

for k, v in dt.items():
    #print(k, v)
    pass


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'Done'

f = fib(6)

print(f)