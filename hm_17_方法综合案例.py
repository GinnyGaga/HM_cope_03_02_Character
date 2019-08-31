class Game(object):
    # 定义类属性
    top_score = 0
    # 定义实例属性
    def __init__(self,player_name):
        self.player_name = player_name
        print("玩家的名字是 %s" % self.player_name)
    # 静态方法显示游戏帮助信息
    @staticmethod
    def show_help():
        print("游戏说明……")
    # 类方法显示历史最高分
    @classmethod
    def show_top_score(cls):
        print("历史最高分…… %d " % cls.top_score)
    # 实例方法
    def start_game(self):
        print("%s 开始游戏……" % self.player_name)


Game.show_help()
Game.show_top_score()
gm = Game("金妮")
gm.start_game()
