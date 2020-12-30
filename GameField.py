from Snake import Snake
from Ball import Ball
from Pong import Pong
from Coordinates import Coordinates
import numpy as np
import os

class GameField:
    def __init__(self, height, width):
        self.__height = height
        self.__width = width
        self.initializeGameField()
        self.__field = self.makeField()

    def initializeGameField(self):
        self.__ball = Ball(Coordinates(round(self.__width/2),round(self.__height/2)))
        self.__xDirectionBall = 'LEFT'
        self.__yDirectionBall = 'HORIZONTAL'
        self.__snake = Snake(4,round(self.__width*2/3),round(self.__height/2))
        self.__snakeDirection = 'LEFT'
        self.__pong = Pong(4,Coordinates(2,round(self.__height/2)-1),1,self.__height-1)

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
        field[self.__ball.coordinates().y()][self.__ball.coordinates().x()]='B'
        snake = self.__snake.getSnake()
        for i in range(0,len(snake)):
            field[snake[i].y()][snake[i].x()] = 'S'
        pong = self.__pong.getPong()
        for i in range(0,len(pong)):
            field[pong[i].y()][pong[i].x()] = 'P'
        return field

    def changeSnakeDirection(self, direction):
        # ... check if snake hits any wall
        # ... check if snake hits itself
        self.__snakeDirection = direction

    def moveBall(self):
        # check if ball hits wall (left or right) --> add point to player1/player2
        if(self.__ball.x()==1 and self.__xDirectionBall == 'LEFT'):
            self.resetField()
            # ... ADD point to player1
        elif(self.__ball.x()==self.__width-1 and self.__xDirectionBall == 'RIGHT'):
            self.resetField()
            # ... ADD point to player2

        # check if ball hits wall (top or bottom)
        if(self.__ball.y()==1 and self.__yDirectionBall == 'UP'):
            self.__yDirectionBall = 'DOWN'
        elif(self.__ball.y()==self.__height-1 and self.__yDirectionBall == 'DOWN'):
            self.__yDirectionBall = 'UP'
        
        # ... check if ball hits pong

        # ... check if ball hits snake

        # move ball
        self.__ball.move(self.__xDirectionBall, self.__yDirectionBall)

    def updateField(self):
        self.moveBall() # set x & set y ball
        self.__snake.move(self.__snakeDirection) # move snake
        #self.__pong.move(self.__ball.coordinates()) #... move pong
        
        self.__field = self.makeField()


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

    def resetField(self):
        # Set ball, pong & snake back to starting position
        self.initializeGameField()


# Sources:
# Add type to numpy empty array: https://stackoverflow.com/questions/13717554/weird-behaviour-initializing-a-numpy-array-of-string-data
# Print without new line: https://careerkarma.com/blog/python-print-without-new-line/#:~:text=In%20order%20to%20print%20without,is%20a%20great%20day.%22)&text=print(%22It%20is%20a%20great%20day.%22),-The%20output%20for
# Get length of numpy array: https://note.nkmk.me/en/python-numpy-ndarray-ndim-shape-size/#:~:text=To%20get%20the%20number%20of,size%20of%20the%20first%20dimension.