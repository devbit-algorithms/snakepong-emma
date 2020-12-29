class Coordinates:
    def __init__(self,x,y):
        self.__x = x
        self.__y = y
    
    def x(self):
        return self.__x
    
    def y(self):
        return self.__y

    def setX(self, x):
        self.__x = x
    
    def setY(self, y):
        self.__y = y