from Coordinates import Coordinates

class Ball:
    def __init__(self, startCoordinates):
        self.__coordinates = startCoordinates

    def coordinates(self):
        return self.__coordinates

    def move(self, xDirection, yDirection):
        if(xDirection == 'LEFT'):
            self.__coordinates.setX(self.__coordinates.x()-1)
        elif(xDirection == 'RIGHT'):
            self.__coordinates.setX(self.__coordinates.x()+1)
        if(yDirection == 'UP'):
            self.__coordinates.setY(self.__coordinates.y()-1)
        elif(yDirection == 'DOWN'):
            self.__coordinates.setY(self.__coordinates.y()+1)