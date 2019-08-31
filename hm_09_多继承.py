class A:
    def test(self):
        print("test 方法")

class B:
    def demo(self):
        print("demo 方法")

class C(A,B):
    def aa(self):
        print("121")

c = C()
c.test()
c.demo()