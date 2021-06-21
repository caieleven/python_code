from time import time

global Max_word
x = []
y = {"i", "a"}

def Find_Cutable():
        global Max_word
        Max_word = ""
        for i in range(len(x)):
                if ifCutable(x[i]):
                        Max_word = x[i] if len(x[i])>len(Max_word) else Max_word
                        y.add(x[i])
        return Max_word
                
def ifCutable(x):
        for i in range(len(x)):
                if x[0:i]+x[i+1:len(x)] in y:
                        return True
        return False

def Show_cut(x):
        for i in range(len(x)):
                x_c = x[0:i]+x[i+1:len(x)]
                if x_c in y:
                        print(x_c)
                        Show_cut(x_c)
        return

if __name__ == "__main__":
        fuc_time =time()
        
        file = open("D:\\codefile\\python_code\\E2\\words.txt")   #读入文件
        x = file.read().split()
        file.close()
        x.sort(key = lambda x:len(x))

        print(Find_Cutable())
        Show_cut(Max_word)
        print(time()-fuc_time)
