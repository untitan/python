try:
    raise ValueError('啥玩意')
    print(f.read())
except (OSError, ValueError) as err:
    print(err)
finally:
    print('完成了')
