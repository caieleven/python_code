from time import time
from random import randint

if __name__ == "__main__":
    m = int(input("请输入班级数："))
    n = int(input("请输入各班人数："))
    ti = time()
    
    stu = [[randint(1, 12)*100+randint(1, 31) for j in range(0,n)] for i in range(0, m)]
    date = [i*100+j for i in range(1,13) for j in range(1, 32)]

    c = set()
    for t in date:
        tc = [k for k in range(len(stu)) if t in stu[k]]
        if len(tc) > 1:
            c = c | set(tc)

    print("概率 p = ", len(c)/m)

    print(time() - ti)

    while True:
        if time() - ti ==1000:
            break
