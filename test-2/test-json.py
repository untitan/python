import json
import uuid

# 构造字典
python2json = {}
# 构造list
listData = [1, 2, 3]
python2json["listData"] = listData
python2json["strData"] = "test python obj 2 json"

# 转换成json字符串
json_str = json.dumps(python2json)
print(type(json_str), json_str)


class Pay(object):
    def __init__(self, channel, traceNo, txnAmt):
        self.txnAmt = txnAmt
        self.traceNo = traceNo
        self.channel = channel


def s2o(s):
    return Pay(s['txnAmt'], s['traceNo'], s['channel'])


pay = Pay('CUP', str(uuid.uuid1()), 100.00)

pay_json = json.dumps(pay, default=lambda p: p.__dict__)

print(pay_json)

pay = json.loads(pay_json, object_hook=s2o)

print(type(pay), pay)
