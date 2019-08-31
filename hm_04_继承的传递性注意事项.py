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

class Cat(Animal):
    def catch(self):
        print("抓老鼠")

xtq = XiaoTianQie()
xtq.fly()
xtq.bark()
xtq.eat()
xtq.drink()
xtq.play()
xtq.sleep()

xtq.cat()