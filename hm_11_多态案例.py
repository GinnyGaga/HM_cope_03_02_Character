class Dog(object):
    def game(self):
        print("狗玩耍")

class Xiantianqian(Dog):
    def game(self):
        print("哮天犬在天上玩耍")

class Person(object):
    def __init__(self,name):
        self.name = name
    def play_with_dog(self):
        dog.game()

dog = Dog()
dog.game()

xtq = Xiantianqian()
xtq.game()

xm = Person("小明")
xm.play_with_dog()