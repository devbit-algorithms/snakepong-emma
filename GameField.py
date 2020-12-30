from Snake import Snake
from Ball import Ball
from Pong import Pong
from Coordinates import Coordinates
from User import User
import numpy as np
import os
import time

class GameField:
    def __init__(self, height, width, player1, player2):
        self.__height = height
        self.__width = width
        self.__player1 = player1 # USER
        self.__player2 = player2 # CPU
        self.initializeGameField()
        self.__field = self.makeField()

    def initializeGameField(self):
        self.__ball = Ball(Coordinates(round(self.__width/2),round(self.__height/2)))
        self.__xDirectionBall = 'LEFT'
        self.__yDirectionBall = 'UP'
        self.__snake = Snake(4,round(self.__width*2/3),round(self.__height/2))
        self.__snakeDirection = 'LEFT'
        self.__pong = Pong(4,Coordinates(2,round(self.__height/2)-1),1,self.__height-2)

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
        if(not self.__snake.contains(self.__snake.newCoordinates(direction))):
            self.__snakeDirection = direction
        # else: snake just keeps the same direction

    def moveSnake(self):
        # check if snake hits any wall
        newCoordinates = self.__snake.newCoordinates(self.__snakeDirection)
        if(newCoordinates.x() == 0 or newCoordinates.y() == 0 or newCoordinates.x() == self.__width-1 or newCoordinates.y() == self.__height-1):
            self.__player2.addPoint()
            time.sleep(1)
            self.resetField()
        # check if snake hits itself
        if(self.__snake.contains(newCoordinates)):
            self.__player2.addPoint()
            time.sleep(1)
            self.resetField()
        else:
            self.__snake.move(self.__snakeDirection) 


    def moveBall(self):
        # check if ball hits wall (left or right) --> add point to player1/player2
        if(self.__ball.x()==1 and self.__xDirectionBall == 'LEFT'):
            self.__player1.addPoint()
            self.resetField()
        elif(self.__ball.x()==self.__width-2 and self.__xDirectionBall == 'RIGHT'):
            self.__player2.addPoint()
            self.resetField()

        # check if ball hits wall (top or bottom)
        if(self.__ball.y()==1 and self.__yDirectionBall == 'UP'):
            self.__yDirectionBall = 'DOWN'
        elif(self.__ball.y()==self.__height-2 and self.__yDirectionBall == 'DOWN'):
            self.__yDirectionBall = 'UP'
        
        # check if ball hits pong
        if(self.__pong.contains(Coordinates(self.__ball.x()-1,self.__ball.y())) and self.__xDirectionBall == 'LEFT'):
            self.__xDirectionBall = 'RIGHT'

        # check if ball hits snake
        if(self.__snake.contains(Coordinates(self.__ball.x()-1,self.__ball.y())) and self.__xDirectionBall == 'LEFT'):
            self.__xDirectionBall = 'RIGHT'

        elif(self.__snake.contains(Coordinates(self.__ball.x()+1,self.__ball.y())) and self.__xDirectionBall == 'RIGHT'):
            self.__xDirectionBall = 'LEFT'

        if(self.__snake.contains(Coordinates(self.__ball.x(),self.__ball.y()-1)) and self.__yDirectionBall == 'UP'):
            self.__yDirectionBall = 'DOWN'

        elif(self.__snake.contains(Coordinates(self.__ball.x(),self.__ball.y()+1)) and self.__yDirectionBall == 'DOWN'):
            self.__yDirectionBall = 'UP'

        # move ball
        self.__ball.move(self.__xDirectionBall, self.__yDirectionBall)

    def updateField(self):
        self.moveBall() # set x & set y ball
        self.moveSnake() # move snake
        self.__pong.move(self.__ball.coordinates()) # move pong
        
        self.__field = self.makeField()


    def printField(self):
        self.updateField()
        self.clearTerminal()
        self.printPlayerScores()
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

    def printPlayerScores(self):
        print("# Player 1: " + self.__player1.username() + " ## Score: " + str(self.__player1.score()))
        print("# Player 2: " + self.__player2.username() + " ## Score: " + str(self.__player2.score()))


# Sources:
# Add type to numpy empty array: https://stackoverflow.com/questions/13717554/weird-behaviour-initializing-a-numpy-array-of-string-data
# Print without new line: https://careerkarma.com/blog/python-print-without-new-line/#:~:text=In%20order%20to%20print%20without,is%20a%20great%20day.%22)&text=print(%22It%20is%20a%20great%20day.%22),-The%20output%20for
# Get length of numpy array: https://note.nkmk.me/en/python-numpy-ndarray-ndim-shape-size/#:~:text=To%20get%20the%20number%20of,size%20of%20the%20first%20dimension.