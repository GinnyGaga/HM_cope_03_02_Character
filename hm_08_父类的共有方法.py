class A:
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200

    def __test(self):
        print("私有方法 %d %d " % (self.num1,self.__num2))

    def test(self):
        print("父类的共有方法 %d " % self.__num2)
        self.__test()

class B(A):
    def demo(self):
        # print("访问父类的私有属性 %d " % self.__num2)
        # self.__test()
        print("子类的方法 %d " % self.num1)
        self.test()

b = B()
print(b)
b.demo()
# 在外界可以访问父类的共有属性和共有方法
# print(b.num1)
# print(b.test())
# # print(b.__num2)
# b.__test()