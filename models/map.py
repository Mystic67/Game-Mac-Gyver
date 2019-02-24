#! /usr/bin/python3
# -*-coding: utf-8-*-


from models.position import Position as pos


class Map:
    ''' This class extract the positions and chars and stored them in lists'''

    def __init__(self, filename):
        ''' Initialize the attributs'''
        self.__filename = filename
        self.__list_positions = []
        self.__list_chars = []
        self.__load_from_file()

    def __load_from_file(self):
        with open(self.__filename, "r") as file:
            for x, line in enumerate(file):
                for y, char in enumerate(line):
                    self.__list_positions.append(pos(x, y))
                    self.__list_chars.append(char)

    def __getitem__(self, position):
        ''' Return the value from the index of position when call map[x,y] '''
        for index, val in enumerate(self.__list_positions):
            if val == position:
                return self.__list_chars[index]

    def items(self):
        ''' method to get all positions and values from index of lists.
        They are stored in generator  '''
        for index, position in enumerate(self.__list_positions):
            value = self.__list_chars[index]
            if value != "\n":
                yield(position, value)
