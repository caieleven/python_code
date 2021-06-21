from typing import Sequence


class Customer:
    def __init__(self):
        pass

    def placeOrder(self, myEmployee):
        myEmployee.ShowFood()
        self.myfood = myEmployee.takeOrder()
        myEmployee.ShowOrder(self.myfood)
        #self.myfood.ShowSelected()



class Employee:
    #接收一个customer
    def __init__(self):
        pass

    def ShowFood(self):
        print("这是我们的菜单：")
        Food.ShowAllfood()

    def takeOrder(self):
        print("请点单：")
        order = Food()
        sequence = int(input("请选择您的菜品："))
        num = int(input("请输入份数："))
        order.ChooseDisher(sequence, num)
        print("\n")
        return order

    def ShowOrder(self, order):
        print("这是您所点的食物：")
        order.ShowSelected()

class Lunch:
    #应该包含1个顾客1个服务员，一个食物
    def __init__(self):
        self.thisCustomer = Customer()
        self.thisEmployee = Employee()

    def order(self):
        print("欢迎光临！请开始点单！")
        print("\n")
        self.thisCustomer.placeOrder(self.thisEmployee)
        print("点单已完成！请稍等！")
        print("\n")
        



class Food:
    fooddict = {1:"红烧肉", 2:"小炒肉", 3:"土豆片", 4:"剁椒鱼头"}

    def __init__(self):
        self.__order = {}
        #键表示对应菜品，值为份数

    def ChooseDisher(self, sequence, num):
        if sequence not in self.__order:
            self.__order[sequence] = num
        else:
            self.__order[sequence] += num

    @classmethod
    def ShowAllfood(cls):
        print("1:红烧肉\t2:小炒肉\t3:土豆片\t4:剁椒鱼头")
    

    def ShowSelected(self):
        for key, val in self.__order.items():
            print(Food.fooddict[key],"*",val, end="\t")
        print("\n")



'''
一个lunch类表示一份交易
一份交易开始，一个customer类
如何识别是不同的客人，需要在customer里面加上客人名字吗？

'''


if __name__ == "__main__":

    LunchList = []
    flag = 'Y'
    while flag == "Y" or flag == "y":
        print("客人到了！")
        temp = Lunch()
        temp.order()
        LunchList.append(temp)
        flag = input("是否还有客人？(Y/N):")

