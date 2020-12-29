import time
from User import User
from GameField import GameField

class Game:
    def __init__(self, player1, player2):
        self.__player1 = player1
        self.__player2 = player2
        self.__gamefield = GameField(15,50)

    def keyPressed(self, key):
        if(key=='key.left'):
            self.__gamefield.moveSnake('LEFT')
        elif(key=='key.right'):
            self.__gamefield.moveSnake('RIGHT')
        elif(key=='key.up'):
            self.__gamefield.moveSnake('UP')
        elif(key=='key.down'):
            self.__gamefield.moveSnake('DOWN')
        elif(key=='key.esc'):
            pass # CHANGE THIS!

    def start(self):
        while(not self.gameOver()):
            self.__gamefield.printField()
            time.sleep(3)

    def gameOver(self):
        if(self.__player1.score()>=5 or self.__player2.score()>=5):
            print('Game over')
            return True  
        else:
            return False


#class PrintField:
    #while (True):
        #print(GameField(4,3).makeField())
        #time.sleep(1)


# Sources:
# Add delay: https://realpython.com/python-sleep/