import re
def rotateword(strsrc, n):
    newstring = [chr((ord(ch) + n) % ord('z')) for ch in strsrc]
    return "".join(newstring)


def avoids(word, avoidword):
    return True if re.search(r'[^' + avoidword + ']',  word) else False


def useonly(word, perword):
    return re.fullmatch(r'[' + perword + ']+', word) == None


def useall(word, needwords):
    return re.search(r'[' + needwords + ']') == None

def hasone(word):
    return re.search(r'e', word) == None




if __name__=='__main__':
    a = "Keifei"
    # print(rotateword(a, 2))
    # print(avoids(a, "ei"))
    # print(useonly(a, "Kei"))
    print(useonly(a, "keKifei"))
    print(hasone(a))