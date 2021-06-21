file_path = ("E:/code/python/experiments/1/passage_test.txt")   # 文件所在路径
with open(file_path, 'r') as f:     # 以'read'只读模式打开文件
    text = f.read()     # 读取文件为str格式
text = text.replace(',', '').replace('.', '')   # 将文本中所有的逗号以及句号替换为空格
text = text.split()     # 将文本断成单词的列表
setword = set(text)     # 将断好的文本组成set，一组key的集合但没有value,特性为没有重复的key，所以不用担心重复的问题
for i in setword:   # 对set内的每个key循环
    count = text.count(i)   # 计算每个key在文本中出现的次数
    print(i, '出现次数：', count)   # 输出
