from time import time
from random import randint

if __name__ == "__main__":
    m = int(input("请输入班级数："))
    n = int(input("请输入各班人数："))
    ti = time()






    print(len([i for i in range(0, m) if len({randint(1, 365) for j in range(0,n)}) < n ])/m)







    
    print(time() - ti)
    
    while True:
        if time() - ti ==1000:
            break

   
