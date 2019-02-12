#! /usr/bin/python3
# -*-coding: utf-8-*-
"""

"""
class Position:
    """This class receive in parameter attribut x an y and return
     Position(x,y) """
    def __init__(self,x,y):
        self._x = x
        self._y = y
        self.position = (self._x,self._y) #absisse/ordonee position

    def __repr__(self):
        """method to return position if enter instance in the
        interpreter"""
        return str(self.position)

    def __str__(self):
        """method to return position if enter print(instance) in the
        interpreter """
        return repr(self)

    def __hash__(self):
        '''method to convert position to hash value.
        Needed to accès to a dictionary with key '''
        return hash(self.position)

    def __eq__(self, pos):
        return self.position == pos.position

    def get_x(self):
        '''method to read the private variable _x'''
        return self._x

    def get_y(self):
        '''method to read the private variable _y'''
        return self._y

if __name__=="__main__":
    Position()
