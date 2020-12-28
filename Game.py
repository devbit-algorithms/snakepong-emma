import numpy as np
import time
from User import User
import os

class Game:
    def __init__(self, player1, player2):
        self.__player1 = player1
        self.__player2 = player2

    def keyPressed(self, key):
        pass

    def start(self):
        gamefield = GameField(15,50)
        while(True):
            gamefield.printField()
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
        self.__ball = Ball(round(self.__width/2),round(self.__height/2))
        self.__field = self.makeField()

    def height(self):
        return self.__height

    def width(self):
        return self.__width

    def makeField(self):
        field = np.empty([self.__height,self.__width],dtype = str)
        for row in range(0,self.__height):
            for col in range(0,self.__width):
                if row==0 or row==self.__height-1:
                    field[row][col]='-'
                elif col==0 or col==self.__width-1:
                    field[row][col]='|'
                else:
                    field[row][col]=' '
        field[self.__ball.getY()][self.__ball.getX()]='B'
        return field

    def updateField(self):
        #set x & set y ball
        self.__field[self.__ball.getY()][self.__ball.getX()]='B'

    def printField(self):
        self.updateField()
        self.clearTerminal()
        for row in range(0,self.__height):
            print()
            for col in range(0,self.__width):
                print(self.__field[row][col],end='')
        print()

    def clearTerminal(self):
        clear = lambda: os.system('cls')
        clear()

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