class Time:
    def __init__(self, hour= 0, minute = 0, second = 0):
        if not self.isvalid(hour, minute, second):
            print("时间不合法，构造失败")
            self.Sethour(0)
            self.Setminute(0)
            self.Setsecond(0)
        else:
            self.Sethour(hour)
            self.Setminute(minute)
            self.Setsecond(second)


    def Sethour(self, hour):
        self.__hour = hour

    
    def Setminute(self, minute):
        self.__minute = minute


    def Setsecond(self, second):
        self.__second = second
    

    @classmethod
    def construct_string(cls, string_data):
        hour, minute, second = string_data.split(':')
        hour  = int(hour)
        minute = int(minute)
        second = int(second)
        if cls.isvalid(hour, minute, second):
            time = cls(hour, minute, second)
            return time
        else:
            print("时间不合法，构造失败")
            return Time(0, 0, 0)


    @staticmethod
    def isvalid(h, m, s):
        return 0 <= h < 24 and 0 <= m < 60 and 0 <= s < 60



    def __str__(self):
        #s = str(self.__hour) + ":" + str(self.__minute) + ":" + str(self.__second)
        s = str(self.__hour) + "时" + str(self.__minute) + "分" + str(self.__second) + "秒"
        return s

    def __add__(self, rhs):
        #返回对象添加一个flag，表明是否进位
        rh = self.__hour + rhs.__hour
        rm = self.__minute + rhs.__minute
        rs = self.__second + rhs.__second
        rhf = False
        if rs > 59:
            rs %= 60
            
            rm += 1
        if rm > 59:
            rm %= 60
            rh += 1
        
        if rh > 23:
            rh %= 24
            rhf = True
        
        
        result = Time(rh, rm, rs)
        result.flag = rhf
        return result
    
    def timetoint(self):
        return (self.__hour*60 + self.__minute) * 60 + self.__second

    
    def printtime(self):
        s = str(self.__hour) + ":" + str(self.__minute) + ":" + str(self.__second)
        print(s)

    def isafter(self, tt):
        if not isinstance(tt, Time):
            print("比较的对象不是Time")
            return
        if self.__hour > tt.__hour:
            return True
        elif self.__hour == tt.__hour and self.__minute > self.__minute:
            return True
        elif self.__hour == tt.__hour and self.__minute == self.__minute and self.__second > tt.__second:
            return True
        else:
            return False

    def increment(self, n):
        if not isinstance(n, int) or n < 0:
            print("n不为整型数或n小于0")
            return
        result = self + Time(0, 0, n)
        return result
    



if __name__ == '__main__':
    time1 = Time.construct_string("12:13:12")
    time2 = Time.construct_string("9:24:50")
    print("time1:", end=' ')
    time1.printtime()
    print("time2:", end=' ')
    time2.printtime()
    print("\n")
    print("Test time1.timetoint()")
    print(time1.timetoint())
    print("\n")
    print("Test time1.increment(4)")
    time1.increment(4).printtime()
    print("\n")
    print("Test time1+time2 and __str__")
    time3=time1+time2
    print(time3)
    

    print("\n")
    



'''
这函数没用，因为如果前面每步操作都加上相应限制，不会出现不合法的Time实例

    def isvalid(self):
        if()

'''