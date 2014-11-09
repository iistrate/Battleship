#
# Board of tiles
#
import Tile

TILE_TYPE = dict(EMPTY = 0, SHIP_HULL = 1, HIT = 2, MISS = 3)

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

    def getTile(self, letter, number):
        labelLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        y = 0
        x = int(number)
        for l in labelLetters:
            if l == letter.upper():
                break
            y += 1
#test case get tile
#        print(counter, "", number)
#end test
        return self.m_Board[y][x]