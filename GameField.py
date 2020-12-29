from Snake import Snake
from Ball import Ball
import numpy as np
import os

class GameField:
    def __init__(self, height, width):
        self.__height = height
        self.__width = width
        self.__ball = Ball(round(self.__width/2),round(self.__height/2))
        self.__snake = Snake(4,4,4) # CHANGE THIS!
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

    def moveSnake(self, direction):
        pass

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


# Sources:
# Add type to numpy empty array: https://stackoverflow.com/questions/13717554/weird-behaviour-initializing-a-numpy-array-of-string-data
# Print without new line: https://careerkarma.com/blog/python-print-without-new-line/#:~:text=In%20order%20to%20print%20without,is%20a%20great%20day.%22)&text=print(%22It%20is%20a%20great%20day.%22),-The%20output%20for
# Get length of numpy array: https://note.nkmk.me/en/python-numpy-ndarray-ndim-shape-size/#:~:text=To%20get%20the%20number%20of,size%20of%20the%20first%20dimension.