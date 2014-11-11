#
# Game class
# has 2 boards, one for the player one for the Ai
#
import Board

BOARD_TYPE = dict(Player = 0, Enemy = 1)
TILE_TYPE = dict(EMPTY = 0, SHIP_HULL = 1, HIT = 2, MISS = 3)

class Game(object):
    ''' Game Class '''
    def __init__(self):
        self.__m_brunning = True
        self.__m_turn = 0
        self.m_pBoard = 0
        self.m_eBoard = 0

    def __str__(self):
        rep = "<Battleship Game>"
        return rep
    
    @property
    def __isRunning(self):
        return self.__m_brunning; 

    def __setRunning(self, boolean):
        self.__m_brunning = boolean;

    def run(self):
        #generate player and enemy boards
        self.m_pBoard = Board.Board(BOARD_TYPE["Player"])
        #add 5 ships to the board
        self.m_eBoard = Board.Board(BOARD_TYPE["Enemy"])
        #game loop
        while self.__isRunning:
            #print board and menu
            print("Player Board: \n{}".format(self.m_pBoard))
            print("Enemy Board: \n{}".format(self.m_eBoard))
            print("Turn is {} Please enter 1 to fire or 0 to quit".format(self.__m_turn), end = ': ')

            uInput = input()
            if int(uInput) == 0:
                self.__setRunning(False)
            else:
                uInput = input("Call your shot!(ex:C5): ")
                self.shoot(self.letterToNumber(uInput[0]), uInput[1])
                self.__m_turn += 1
                del uInput

    def shoot(self, y, x):
        tile = self.m_eBoard.getTile(y, x)
        tileType = tile.getType
        tileType = tileType[1] if len(tileType) > 1 else 0
#test types
#        print(type(tileType), type(TILE_TYPE["EMPTY"]))
#        print(tileType, TILE_TYPE["EMPTY"])
#end test
        if tileType == TILE_TYPE["EMPTY"]:
            print("Shot Missed!")
            tile.setTile(TILE_TYPE["MISS"])
        elif tileType == TILE_TYPE["SHIP_HULL"]:
            print("Shot Hit!")
            tile.setTile(TILE_TYPE["HIT"])
            self.m_eBoard.hit(y, x)
        else:
            print("Already fired there! Obvious miss!")

    @staticmethod
    def letterToNumber(letter):
        labelLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        number = 0
        for l in labelLetters:
            if l.lower() == letter.lower():
                break
            number += 1
        return number