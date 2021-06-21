num = 0

file_path = ("words.txt")
with open(file_path, 'r') as f:
    file = f.read()
#file = file.replace(',', '').replace('.', '')
file = file.split()
len = len(file)
#print(type(range(len)))
for i in range(int(len/2)):
    for j in range(len-1, i,-1):
        if file[i] == file[j][::-1]:
            print(file[i], '和', file[j], '互为反向对')
            num+=1
            break
print(num)
