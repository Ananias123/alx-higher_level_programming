#!/usr/bin/python3

'''this is the class named Base'''


class Base:

    '''Private class attribute'''
    __nb_objects = 0

    def __init__(self, id=None):

        '''The class constructor'''

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
