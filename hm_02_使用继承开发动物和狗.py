class Animal:

    def eat(self):
        print("吃___")

    def drink(self):
        print("喝__")

    def play(self):
        print("玩__")

    def sleep(self):
        print("睡__")

class Dog(Animal):
    # def eat(self):
    #     print("吃")
    #
    # def drink(self):
    #     print("喝")
    #
    # def play(self):
    #     print("玩")
    #
    # def sleep(self):
    #     print("睡")

    def bark(self):
        print("吠")

Wangcai = Dog()
Wangcai.eat()
Wangcai.drink()
Wangcai.play()
Wangcai.sleep()
Wangcai.bark()
