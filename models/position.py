#! /usr/bin/python3
# -*-coding: utf-8-*-

class Position:

    
    """This class receive in parameter attribut x an y and return
     Position(x,y) """
    def __init__(self,x,y):
        self.__x = x
        self.__y = y
        self.__position = (self.__x,self.__y) #absisse/ordonee position


    def __repr__(self):
        """method to return position if enter instance in the
        interpreter"""
        return str(self.__position)


    def __str__(self):
        """method to return position if enter print(instance) in the
        interpreter """
        return repr(self)


    def __hash__(self):
        '''method to convert position to hash value.
        Needed to accès to a dictionary with key '''
        return hash(self.__position)


    def __eq__(self, pos):
        return self.__position == pos.position


    def get_x(self):
        '''method to read the private variable __x'''
        return self.__x


    def get_y(self):
        '''method to read the private variable __y'''
        return self.__y


    def get_position(self):
        '''method to read the private variable __position'''
        return self.__position
