#
# Board of tiles
#
import Tile
import Ship

TILE_TYPE = dict(EMPTY = 0, SHIP_HULL = 1, HIT = 2, MISS = 3)
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
        #public
        self.m_Board = [[]]
        #init Board
        for i in range(0, self.__getHeight):
            self.m_Board.append([])
            for j in range(0, self.__getWidth):
                #init all to blank
                self.m_Board[i].append(Tile.Tile(TILE_TYPE['EMPTY']))
        if type == BOARD_TYPE["Player"]:
            ships = ["Carrier", "Battleship", "Cruiser", "Destroyer", "Submarine"]
            pShips = list()
            while len(ships) > 0:
                print(self)
                uInput = input("Place {} horizontal or vertical example A5H or A5V: ".format(ships[-1]))
                posY = self.letterToNumber(uInput[0])
                posX = int(uInput[1])
                orientation = uInput[2].lower()
                #add ship to fleet
                pShips.append(Ship.Ship(ships[-1], posY, posX, orientation))
                #add on map
                size = pShips[-1].getHitpoints
                while size > 0:
                    if orientation == "h":
                        self.m_Board[posY][posX+size].setTile('1')
                    else:
                        self.m_Board[posY+size][posX].setTile('1')
                    size -= 1
                #remove last item from list
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