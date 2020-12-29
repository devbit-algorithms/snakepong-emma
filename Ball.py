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