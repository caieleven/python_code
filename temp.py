import re
str = "I have an apple, I have nothing!"
p1 = re.compile("\s+")
p2 = re.compile("(I)( )(have)")
p3 = re.compile("I have")
c1 = re.match(p2, str)
c2 = re.findall(p2, str)
print(p3.findall(str))
c3 = re.search(p2, str)
print(c1.end())
print(c3.group(3))
print(c2)

class A:
    def __init__(self, pp = 0):
        self._p = pp
    
    @property
    def p(self):
        return self._p
    
    @p.setter
    def p(self, value):
        self._p = value

    @p.getter
    def p(self):
        return self._p

    

a = A()
print(a.p)
a.p = 55
a.p = 44
print(a.p)