#
#   Tile 0, 1, X or W
#
class Tile(object):
    '''One tile'''
    TILE_TYPE = dict(EMPTY = 0, SHIP_HULL = 1, HIT = 2, MISS = 3)
    #constructor
    def __init__(self, type):
        if type == self.TILE_TYPE['EMPTY']:
            self.__m_type = '0'
        elif type == self.TILE_TYPE['SHIP_HULL']:
            self.__m_type = '1'
        elif type == self.TILE_TYPE['HIT']:
            self.__m_type = 'X'
        elif getType == self.TILE_TYPE['MISS']:
            self.__m_type = 'W'
    #rep for print
    def __str__(self):
        if getType == self.TILE_TYPE['EMPTY']:
            rep = "0"
        elif getType == self.TILE_TYPE['SHIP_HULL']:
            rep = "1"
        elif getType == self.TILE_TYPE['HIT']:
            rep = "X"
        elif getType == self.TILE_TYPE['MISS']:
            rep = "W"
        return rep
    #sets
    def setTile(self, type):
        if type == self.TILE_TYPE['EMPTY']:
            self.__m_type = '0'
        elif type == self.TILE_TYPE['SHIP_HULL']:
            self.__m_type = '1'
        elif type == self.TILE_TYPE['HIT']:
            self.__m_type = 'X'
        elif getType == self.TILE_TYPE['MISS']:
            self.__m_type = 'W'
    #gets
    @property
    def getType(self):
        return self.__m_type;

