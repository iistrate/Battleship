#
#   Game class
#   has 2 boards, one for the player one for the Ai

import Board

class Game(object):
    #constants
    BOARD_TYPE = dict(Player = 0, Enemy = 1)

    ''' Game Class '''
    def __init__(self):
        self.__m_brunning = True
        self.__turn = 0

    def __str__(self):
        rep = "<Battleship Game>"
        return rep
    
    @property
    def __isRunning(self):
        return self.__m_brunning; 

    def __setRunning(self, boolean):
        self.__m_brunning = boolean;

    def run(self):
        m_pBoard = Board.Board(self.BOARD_TYPE["Player"])
        m_eBoard = Board.Board(self.BOARD_TYPE["Enemy"])
        while self.__isRunning:
            print(m_pBoard)
            print(m_eBoard)
            ++self.__turn
            self.__setRunning(False)