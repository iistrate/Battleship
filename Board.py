#
# Board of tiles
#
class Board(object):
    '''Board of tile objects'''
    #constructor
    def __init__(self, type):
        self.__m_width = 10
        self.__m_height = 10
        self.__m_type = type
    #rep for print
    def __str__(self):
        rep = "0"
        return rep

