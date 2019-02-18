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

    def __iter__(self):
        '''makes position iterable '''
        return iter(self.__list_positions)

    def __str__(self):
        '''method to represente the map if print(instance) in interpreter
        Not needed for the programme, only for debugging'''
        string = ""
        for value in self.__list_chars:
            string += value
        return string

    def __repr__(self):
        '''method to represente the instance from object if enter
         instance name in interpreter. Not needed for the programme,
         only for debugging '''
        string = "{"
        first_loop = True
        for key, value in self.items():
            if not first_loop:
                string += ","
            else:
                first_loop = False
            string += repr(key) + ":" + repr(value)
        string += "}"
        return string

    def __getitem__(self, position):
        ''' Return the value from the index of position when call map[x,y] '''
        for index, val in enumerate(self.__list_positions):
            if hash(val) == hash(position):
                return self.__list_chars[index]

    def items(self):
        ''' method to get all positions and values from index of lists.
        They are stored in generator  '''
        for index, position in enumerate(self.__list_positions):
            value = self.__list_chars[index]
            if value != "\n":
                yield(position, value)


def main():
    ''' main test '''
#    map = Map("map.txt")
#    print(map)
#    print(map[(0,0)])
#    map[2,5]
#    print(map[2,5])
#    for position, value in map.items():
#        print(position, value)


if __name__ == "__main__":
    main()
