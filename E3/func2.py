from random import randint


# dict是无序的，是否需要collections中的OrderedDict

def RemoveRepeat(obj):
    #很好的教材，看看为什么出错,for访问机制
    # if isinstance(obj, list):
    #     tempset = set()
    #     i = 0
    #     for x in iter(obj):
    #         if x in tempset:
    #             obj.pop(i)
    #         if x not in tempset:
    #             tempset.add(x)
    #             i += 1
    if isinstance(obj, dict):
        operdict(obj)
    elif isinstance(obj, list):
        operlist2(obj)
            

def operlist(listobj):
    tempset = set()
    for x in listobj:
        if x not in tempset:
            tempset.add(x)
            yield x

def operlist2(listobj):
    tempset = set()
    templist = list()
    for x in listobj:
        if x not in tempset:
            tempset.add(x)
            templist.append(x)
    return templist


def operdict(dictobj):
    tempset = set()
    klist = list(dictobj.keys())
    #不能直接使用：for k in obj.keys()
    for k in klist:
        if dictobj[k] in tempset:
            del dictobj[k]
        else:
            tempset.add(dictobj[k])

print("字典测试：")
y = {i:2 for i in range(10)}
print("原字典：", end = '')
print(y)
print("更改后：", end='')
RemoveRepeat(y)
print(y)


print("\n")
print("列表测试：")

x = [randint(1, 3) for i in range(10)]
print("原列表：", end='')
print(x)
x = list(operlist(x))
print("更改后：", end='')
print(x)




















# 在 Python中，序列类型包括字符串、列表、元组、集合和字典