#! /usr/bin/python3
# -*-coding: utf-8-*-


class Position:
    '''This class receive in parameter attribut x an y and return
     Position(x,y) '''

    def __init__(self, x, y):
        ''' Initialize the attributs'''
        self.__x = x
        self.__y = y
        self.__position = self.get_position()  # absisse/ordonee position

    def __eq__(self, position):
        '''This method is needed if want to compare a position with tuple
        self.__position == (x,y) '''
        return self.__position == position

    def get_x(self):
        '''method to read the private variable __x'''
        return self.__x

    def set_x(self, x):
        self.__x = x

    def get_y(self):
        '''method to read the private variable __y'''
        return self.__y

    def set_y(self, y):
        self.__y = y

    def get_position(self):
        '''method to read the private variable __position'''
        position = (self.__x, self.__y)
        return position

    def set_position(self, position):
        '''method to read the private variable __position'''
        self.__x, self.__y = position
