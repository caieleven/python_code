from time import time
t = time()
f = open("words.txt")
words = { w.strip() for w in f }
result = { w for w in words if w[::-1] in words }
print(sorted(list(result)))
print(time()- t)
