import re


# 编写函数 rotateword，接收一个字符串 strsrc 以及一个整数 n 作为参数，返回新字符串 strdes，
# 其各个字母是 strsrc 中对应位置各个字母在字母表中“轮转”n 字符后得到的编码。
def rotateword(strsrc, n=0):
    result = re.findall(r'.{' + str(n) + '}', strsrc)
    result.reverse()
    return ''.join(result)


def rotateword2(strsrc, n):
    newstring = [chr((ord(ch) + n) % ord('z')) for ch in strsrc]
    return "".join(newstring)




# 编写函数 avoids，接收一个单词和一个含有禁止字母的字符串，判断该单词是否含有禁止字母。
def avoids(strsrc, s):
    return re.search(r'[' + s + ']', strsrc) == None


# 编写函数 useonly，接收一个单词和一个含有允许字母的字符串，判断该单词是否仅仅由允许字母组成。
def useonly(strsrc, s):
    return re.search(r'[^' + s + ']', strsrc) == None


# 编写函数 useall，接收一个单词和一个含有需要字母的字符串，判断该单词是否包含了所有需要字母至少一个，
# 并输出 words.txt 中使用了所有元音字母 aeiou 的单词。
def useall(strsrc, s):
    return re.search(r'[' + s + ']', strsrc) == None


# 编写函数 hasnoe，判断一个英语单词是否包含字母 e，并计算 words.txt中不含 e 的单词在整个字母表中的百分比。
def hasnoe(strsrc):
    return useall(strsrc, 'e')


# 编写函数 isabecedarian，判断一个英语单词中的字母是否符合字母表序，并且输出 words.txt 中所有这样的单词。
def isabecedarian(strsrc):
    return re.match(r'^a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z*$', strsrc) != None


if __name__ == '__main__':

    s = "abc"
    print(rotateword2(s, 1))
    print(rotateword(s, 2))
    print(avoids(s, "abc"))

    # x = [i for i in open("D:\\codefile\\python_code\\E4\\words.txt").read().split() if useall(i, "aeiou")]
    # print(x)

    # y = [i for i in open("D:\\codefile\\python_code\\E4\\words.txt").read().split() if hasnoe(i)]
    # print(len(y) / len(open("D:\\codefile\\python_code\\E4\\words.txt").read().split()))

    # z = [i for i in open("D:\\codefile\\python_code\\E4\\words.txt").read().split() if isabecedarian(i)]
    # print(z)
