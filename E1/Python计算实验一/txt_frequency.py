file_path = ("passage_test.txt")
with open(file_path, 'r') as f:
    text = f.read()
text = text.replace(',', '').replace('.', '')
text = text.split()
request = input("请输入想要查找频率的单词，以空格隔开：").split()
request = request.replace(',', '').replace('.', '')
setrequest = set(request)
for i in setrequest:
    count = text.count(i)   # 计算每个key在文本中出现的次数
    if count == 0:
        print(i, '没有在此文本文件中出现。')
    else:
        print(i, '出现次数：', count)   # 输出
