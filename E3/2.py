# a、对象成员 hour，minute 和 second 的时间类 Time；
# b、重载__str__和__add__方法；
# c、方法 time2int：把时间对象转换为秒数；
# d、方法printtime：输出时间；
# e、方法 isafter：判断两个时间对象的先后；
# f、方法 increment：计算对象经过 n〉0 秒后时间；
# g、方法 isvalid：判断时间对象合法性。
# 在主函数设计代码验证 Time 各个方法的正确性。

class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second
        if not self.isvalid():
            print("time is not valid")
            self.clear()

    def __str__(self):
        return str(self.hour) + ":" + str(self.minute) + ":" + str(self.second)

    def __add__(self, other):
        if not isinstance(other, Time):
            print("other must be Time")
            return
        temp = (self.time2int() + other.time2int()) % (24 * 60 * 60)
        return Time(temp // (60 * 60), temp % (60 * 60) // 60, (temp % (60 * 60)) % 60)

    def time2int(self):
        return self.hour * 60 * 60 + self.minute * 60 + self.second

    def printtime(self):
        print(self.__str__())

    def isafter(self, other):  # 判断两个时间对象的先后；
        return self.time2int() > other.time2int()

    def iscrement(self, n):  # 计算对象经过 n〉0 秒后时间；
        if not isinstance(n, int):
            print("n must be integer")
            return
        temp = self.time2int() + n
        self.hour = temp // (60 * 60)
        self.minute = temp % (60 * 60) // 60
        self.second = (temp % (60 * 60)) % 60

    def isvalid(self):  # 判断时间对象合法性。
        return self.hour >= 0 and self.hour < 23 and self.minute >= 0 and self.minute < 59 and self.second >= 0 and self.second < 59

    def clear(self):
        self.hour = 0
        self.minute = 0
        self.second = 0


if __name__ == "__main__":
    t1 = Time(23, 59, 59)
    t2 = Time(1, 1, 1)
    t3 = t1 + t2
    t3.show()
