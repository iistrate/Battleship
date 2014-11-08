class Tile(object):
    '''One tile'''
    TILE_TYPE = dict(EMPTY = 0, SHIP_HULL = 1, HIT = 2)
    #constructor
    def __init__(self, type):
        self__m_type = type
    #rep for print
    def __str__(self):
        if getType == TILE_TYPE['EMPTY']:
            rep = "0"
        elif getType == TILE_TYPE['SHIP_HULL']:
            rep = "1"
        elif getType == TILE_TYPE['HIT']:
            rep = "X"
    #sets
    def setTile(self, type):
        if type == TILE_TYPE['EMPTY']:
            self.__m_type = TILE_TYPE['EMPTY']
        elif type == TILE_TYPE['SHIP_HULL']:
            self.__m_type = TILE_TYPE['SHIP_HULL']
        elif type == TILE_TYPE['HIT']:
            self.__m_type = TILE_TYPE['HIT']
    #gets
    @property
    def getType(self):
        return __m_type;

