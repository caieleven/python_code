##### 1. 迭代器是一个可以记住遍历位置的对象。迭代器对象只能往前不会后退，迭代器有两个基本方法` iter()  and  next() ` ，字符串、列表、元组都可以用来创建迭代器。

##### 2. 使用了yield的函数被称为生成器，生成器是一个返回迭代器的函数，只能用于迭代操作

[相关博客]:https://blog.csdn.net/mieleizhi0522/article/details/82142856

```python
import sys

def fibonacci(n): # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): 
            return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(10) # f 是一个迭代器，由生成器返回生成

while True:
    try:
        print (next(f), end=" ")
    except StopIteration:
        sys.exit()
```

##### 3. 列表的删除有三种方式：del，pop，remove