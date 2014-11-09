#
#   Tile 0, 1, X or W
#

TILE_TYPE = dict(EMPTY = 0, SHIP_HULL = 1, HIT = 2, MISS = 3)

class Tile(object):
    '''One tile'''
    #constructor
    def __init__(self, type):
        if type == TILE_TYPE['EMPTY']:
            self.__m_type = '0'
        elif type == TILE_TYPE['SHIP_HULL']:
            self.__m_type = '1'
        elif type == TILE_TYPE['HIT']:
            self.__m_type = 'X'
        elif getType == TILE_TYPE['MISS']:
            self.__m_type = 'W'
    #rep for print
    def __str__(self):
        rep = ""
        if self.getType == TILE_TYPE['EMPTY']:
            rep = "0"
        elif self.getType == TILE_TYPE['SHIP_HULL']:
            rep = "1"
        elif self.getType == TILE_TYPE['HIT']:
            rep = "X"
        elif self.getType == TILE_TYPE['MISS']:
            rep = "W"
        return rep
    #sets
    def setTile(self, type):
        if type == TILE_TYPE['EMPTY']:
            self.__m_type = '0'
        elif type == TILE_TYPE['SHIP_HULL']:
            self.__m_type = '1'
        elif type == TILE_TYPE['HIT']:
            self.__m_type = 'X'
        elif type == TILE_TYPE['MISS']:
            self.__m_type = 'W'
    #gets
    @property
    def getType(self):
        return self.__m_type;

