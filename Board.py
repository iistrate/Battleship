#
# Board of tiles
# has tiles and ships

import Tile
import Ship

import random

TILE_TYPE = dict(EMPTY = 0, SHIP_HULL = 1, HIT = 2, MISS = 3, HIDDEN = 4)
BOARD_TYPE = dict(Player = 0, Enemy = 1)

class Board(object):
    '''Board of tile objects'''
    #constructor
    def __init__(self, type):
        #member vars
        #private
        self.__m_width = 10
        self.__m_height = 10
        self.__m_type = type
        self.__m_Ships = list()
        #public
        self.m_Board = [[]]
        #init Board
        for i in range(0, self.__getHeight):
            self.m_Board.append([])
            for j in range(0, self.__getWidth):
                #init all to blank
                self.m_Board[i].append(Tile.Tile(TILE_TYPE['EMPTY']))
        if type == BOARD_TYPE["Player"] or type == BOARD_TYPE["Enemy"]:
            ships = ["Carrier", "Battleship", "Cruiser", "Destroyer", "Submarine"]
            dice = random.randrange(1,4,1)
            dice = 1
#test dice
#            print(dice)
#end test
            #enemy ship pre determined positions
            if dice == 1:
                aiships = [(0,0,"v"), (0,2,"h"), (6,0,"v"), (3,6,"v"), (0,7,"v")]
            elif dice == 2:
                aiships = [(3,2,"v"), (9,2,"h"), (5,0,"v"), (3,6,"h"), (7,7,"v")]
            elif dice == 3:
                aiships = [(6,0,"h"), (0,2,"h"), (4,9,"v"), (9,4,"h"), (4,5,"v")]

            while len(ships) > 0:
                if type == BOARD_TYPE["Player"]:
                    print(self)
                    uInput = input("Place {} horizontal/vertical example D4H or D4V: ".format(ships[-1]))
                    posY = self.letterToNumber(uInput[0])
                    posX = int(uInput[1])
                    orientation = uInput[2].lower()
                else:
                    ship = aiships.pop()
                    posY = ship[0]
                    posX = ship[1]
                    orientation = ship[2]
#test enemy positions placement 
#                    print(ship)
#end test
                #add ship to fleet
                self.__m_Ships.append(Ship.Ship(ships[-1], posY, posX, orientation))
                #add on map
                size = self.__m_Ships[-1].getHitpoints

                #if player show hull, if enemy hide
                if type == BOARD_TYPE['Player']:
                    shipHull = TILE_TYPE['SHIP_HULL']
                else:
                    shipHull = TILE_TYPE['HIDDEN']

                while size > 0:
                    if orientation == "h":
                        self.m_Board[posY][posX+size-1].setTile(shipHull)
                    else:                        
                        self.m_Board[posY+size-1][posX].setTile(shipHull)
                    size -= 1
                #remove last ship from ship list
                ships.pop(-1)
    #rep for print
    def __str__(self):
        labelLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        labelNumbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,]
        rep = " "
        for number in labelNumbers:
            rep += str(number)
        for i in range(0, self.__getHeight):
            rep += '\n'
            rep += labelLetters[i]
            for j in range(0, self.__getWidth):
                rep += self.m_Board[i][j].getType[0]
        rep += '\n'
        return rep
    
    @property
    def __getWidth(self):
        return self.__m_width
    @property
    def __getHeight(self):
        return self.__m_height

    def getTile(self, y, x):
#test case get tile
#        print(y, "", x)
#end test
        return self.m_Board[int(y)][int(x)]

    def setTile(self, y, x, tile):
        self.m_Board[y][x] = tile

    @staticmethod
    def letterToNumber(letter):
        labelLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        number = 0
        for l in labelLetters:
            if l.lower() == letter.lower():
                break
            number += 1
        return number

    def getFleet(self):
        return self.__m_Ships

    @property
    def getFleetSize():
        return len(self.__m_Ships)

    def hit(self, y, x):
        #iterate through fleet
        for ship in self.__m_Ships:
            #find ship that was hit
            if int(x) >= ship.getX - ship.getSize and int(x) <= ship.getX + ship.getSize:
                if int(y) >= ship.getY - ship.getSize and int(y) <= ship.getY + ship.getSize: 
#test ship, ship type
#                    print(type(ship))
#                    print(ship)
#end test
                    #found ship
                    ship.takeDamage()
                    hitpoints = ship.getHitpoints
#test hitpoints
#                   print("Hitpoints {}".format(hitpoints))
#end test
                    if (hitpoints == 0):
                        self.__m_Ships.remove(ship)
                        fleetSize = len(self.__m_Ships)
                        if fleetSize > 0:
                            print("Ship destroyed! {} ships remaining".format(fleetSize))
                        else:
                            print("Well done, Enemy fleet obliterated!")
                            return True