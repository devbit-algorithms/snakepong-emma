import time
from User import User
from GameField import GameField

class Game:
    def __init__(self, player1, player2):
        self.__player1 = player1
        self.__player2 = player2
        self.__gamefield = GameField(15,50, self.__player1, self.__player2)

    def keyPressed(self, key):
        if(key=='Key.left'):
            self.__gamefield.changeSnakeDirection('LEFT')
        elif(key=='Key.right'):
            self.__gamefield.changeSnakeDirection('RIGHT')
        elif(key=='Key.up'):
            self.__gamefield.changeSnakeDirection('UP')
        elif(key=='Key.down'):
            self.__gamefield.changeSnakeDirection('DOWN')
        elif(key=='Key.esc'):
            self.__player2.addPoint(5)

    def start(self):
        while(not self.gameOver()):
            self.__gamefield.printField()
            time.sleep(3)

    def gameOver(self):
        if(self.__player1.score()>=5 or self.__player2.score()>=5):
            print('Game over')
            if(self.__player1.score()>=5):
                print(self.__player1.username() + " won.")
            elif(self.__player2.score()>=5):
                print(self.__player2.username() + " won.")
            return True  
        else:
            return False


#class PrintField:
    #while (True):
        #print(GameField(4,3).makeField())
        #time.sleep(1)


# Sources:
# Add delay: https://realpython.com/python-sleep/