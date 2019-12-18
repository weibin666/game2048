"""
    界面逻辑
"""
import os

from bll import GameController


class GameConsoleView:

    def __init__(self):
        self.__controller = GameController()

    def main(self):
        self.__start()

        self.__update()

    def __start(self):
        self.__controller.generate_new_number()
        self.__controller.generate_new_number()
        self.__draw_map()

    def __draw_map(self):
        # 清空终端
        os.system("clear")
        for line in self.__controller.map:
            for item in line:
                print(item, end="\t")
            print()

    def __update(self):
        while True:
            dir = input("请输入：")
            self.__move_map(dir)
            self.__controller.generate_new_number()
            self.__draw_map()
            if self.__controller.is_game_over():
                print("游戏结束喽")

    def __move_map(self, dir):
        if dir == "w":
            self.__controller.move_up()
        elif dir == "s":
            self.__controller.move_down()
        elif dir == "a":
            self.__controller.move_left()
        elif dir == "d":
            self.__controller.move_right()
