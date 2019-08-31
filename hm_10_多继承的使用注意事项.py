class A:
    def test(self):
        print("test 方法1")
    def demo(self):
        print("demo 方法1")

class B:
    def test(self):
        print("test 方法2")
    def demo(self):
        print("demo 方法2")

class C(A,B):
    pass

c = C()
c.test()
c.demo()
# 确定C类对象调用方法的顺序
print(C.__mro__)
