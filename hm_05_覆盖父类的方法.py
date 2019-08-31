class Animal:
    def eat(self):
        print("吃")

    def drink(self):
        print("喝__")

    def play(self):
        print("玩__")

    def sleep(self):
        print("睡__")

class Dog(Animal):
    def bark(self):
        print("汪叫")

class XiaoTianQie(Dog):
    def fly(self):
        print("飞")
    # 若子类中重写了父类的方法，
    # 在使用子类对象调用方法时，会调用子类中重写的方法
    def bark(self):
        print("叫得跟神一样。。。")

xtq = XiaoTianQie()
xtq.bark()