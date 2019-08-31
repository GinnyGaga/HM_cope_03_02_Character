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
    # 针对子类特有的需求，编写代码
    def bark(self):
        print("神一样的叫。。")
    # 使用 super()，调用原本在父类中封装的方法
    #     super().bark()
    # 使用父类.方法(self) 调用(不推荐)
        Dog.bark(self)
    # 如果使用子类调用方法，会出现递归调用--死循环
    #     XiaoTianQie.bark(self)
    # 增加其他子类的代码
        print("%%&&&")

xtq = XiaoTianQie()
xtq.bark()