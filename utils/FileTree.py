from colorama import Fore
from colorama import Style


class FileTree():
    def __init__(self):
        self.__current_level = 0
        self.__last_is_file = None

    def print(self, str, dir_level, color=Fore.WHITE):
        if dir_level >= 0:
            self.__current_level = dir_level
            self.__last_is_file = False
            print("│   " * self.__current_level + "├───" + color + str + '/' + Style.RESET_ALL)
        else:
            if not self.__last_is_file:
                self.__current_level += 1
            self.__last_is_file = True
            print("│   " * self.__current_level + "├───" + color + str + Style.RESET_ALL)


file_tree = FileTree()
