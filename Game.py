import numpy as np
import time
from User import User

class Game:
    def __init__(self, player1, player2):
        self.__player1 = player1
        self.__player2 = player2

    def keyPressed(self, key):
        pass

    def start(self):
        while(True):
            print("Game is started")
            time.sleep(3)

    def gameOver(self):
        if(self.__player1.score()>=5 or self.__player2.score()>=5):
            return True
        else:
            return False
        

class GameField:
    def __init__(self, height, width):
        self.__height = height
        self.__width = width

    def makeField(self):
        field = np.empty([self.__height,self.__width])
        #field = np.arange(self.__height*self.__width).reshape(self.__height, self.__width)
        return field

class Ball:
    def __init__(self, positionX, positionY):
        self.__positionX = positionX
        self.__positionY = positionY

    def getX(self):
        return self.__positionX

    def getY(self):
        return self.__positionY

    def setX(self, positionX):
        self.__positionX = positionX

    def setY(self, positionY):
        self.__positionY = positionY

class Pong:
    def __init__(self, positionX, positionY):
        self.__positionX = positionX
        self.__positionY = positionY

    def getX(self):
        return self.__positionX

    def getY(self):
        return self.__positionY

    def setX(self, positionX):
        self.__positionX = positionX

    def setY(self, positionY):
        self.__positionY = positionY

class Snake:
    def __init__(self, positionX, positionY):
        self.__positionX = positionX
        self.__positionY = positionY

    def getX(self):
        return self.__positionX

    def getY(self):
        return self.__positionY

    def setX(self, positionX):
        self.__positionX = positionX

    def setY(self, positionY):
        self.__positionY = positionY


#class PrintField:
    #while (True):
        #print(GameField(4,3).makeField())
        #time.sleep(1)


# Sources:
# Add delay: https://realpython.com/python-sleep/