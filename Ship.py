#
# Ship
#
SHIP_TYPE = dict(Carrier =  5, Battleship = 4, Cruiser = 3, Destroyer = 2, Submarine = 1)
class Ship(object):
    '''A ship object'''
    def __init__(self, type, posY, posX, orientation):
        if type == "Carrier":
            self.__m_type = SHIP_TYPE['Carrier']
            self.__m_hitpoints = SHIP_TYPE['Carrier']
        elif type == "Battleship":
            self.__m_type = SHIP_TYPE['Battleship']
            self.__m_hitpoints = SHIP_TYPE['Battleship']
        elif type == "Cruiser":
            self.__m_type = SHIP_TYPE['Cruiser']
            self.__m_hitpoints = SHIP_TYPE['Cruiser']
        elif type == "Destroyer":
            self.__m_type = SHIP_TYPE['Destroyer']
            self.__m_hitpoints = SHIP_TYPE['Destroyer']
        elif type == "Submarine":
            self.__m_type = SHIP_TYPE['Submarine']
            self.__m_hitpoints = SHIP_TYPE['Submarine']
        self.__m_posY = posY
        self.__m_posX = posX
        self.__m_orientation = orientation
        #for print purposes
        self.__m_stype = type
        #ship size
        self.__m_size = self.__m_hitpoints;

    def __str__(self):
        return self.__sm_type
    
    def takeDamage(self):
        self.__m_hitpoints = self.__m_hitpoints - 1 if self.__m_hitpoints > 0 else 0

    @property
    def getType(self):
        return self.__m_type
    @property
    def getHitpoints(self):
        return self.__m_hitpoints
    @property
    def getX(self):
        return self.__m_posX
    @property
    def getY(self):
        return self.__m_posY
    @property
    def getSize(self):
        return self.__m_size
    @property
    def getOrientation(self):
        return self.__m_orientation;