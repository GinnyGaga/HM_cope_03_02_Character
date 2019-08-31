class MusicPlayer(object):
    instance = None
    init_flat = False

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance
    def __init__(self):
        # 1、判断是否执行过初始化动作
        if MusicPlayer.init_flat:
            return
        # 2、如果没有执行过，则再执行初始化动作
        print("初始化动作一次")
        # 3、修改类属性的标志
        MusicPlayer.init_flat = True

player1 = MusicPlayer()
print(player1)
player2 = MusicPlayer()
print(player2)