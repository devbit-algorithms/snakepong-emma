from SLL import SingleLinkedList
from Coordinates import Coordinates
import numpy as np

class Snake(SingleLinkedList):
    def __init__(self, length, startX, startY):
        super().__init__()
        self.__length = length
        self.createSnake(Coordinates(startX,startY))

    def getLength(self):
        return self.__length

    def getSnake(self):
        array = np.empty([self.__length],dtype=Coordinates)
        cursor = self.headNode()
        for i in range(0,self.__length):
            array[i] = cursor.get()
            cursor = cursor.next()            
        return array

    def createSnake(self, startCoordinates):
        self.prepend(startCoordinates)
        for offset in range(1, self.__length):
            self.append(Coordinates(startCoordinates.x(),startCoordinates.y()+offset))

    #def createSnake(self, startX, startY):
    #    self.prepend(np.array([startX,startY]))
    #    for offset in range(1, self.__length):
    #        self.append(np.array([startX,startY+offset]))

    #def move(self, direction):
    #    lastHeadValue = self.head()
    #    if(direction=='UP'):
    #        self.prepend(np.array([lastHeadValue[0],lastHeadValue[1]-1]))
    #    elif(direction=='DOWN'):
    #        self.prepend(np.array([lastHeadValue[0],lastHeadValue[1]+1]))
    #    elif(direction=='LEFT'):
    #        self.prepend(np.array([lastHeadValue[0]-1,lastHeadValue[1]]))
    #    elif(direction=='RIGHT'):
    #        self.prepend(np.array([lastHeadValue[0]+1,lastHeadValue[1]]))
    #    self.removeLast()
    #    return self

    def move(self, direction):
        lastHeadCoordinates = self.head()
        if(direction=='UP'):
            newCoordinates = Coordinates(lastHeadCoordinates.x(),lastHeadCoordinates.y()-1)
            if(not self.contains(newCoordinates)):
                self.prepend(newCoordinates)
        elif(direction=='DOWN'):
            newCoordinates = Coordinates(lastHeadCoordinates.x(),lastHeadCoordinates.y()+1)
            if(not self.contains(newCoordinates)):
                self.prepend(newCoordinates)
        elif(direction=='LEFT'):
            newCoordinates = Coordinates(lastHeadCoordinates.x()-1,lastHeadCoordinates.y())
            if(not self.contains(newCoordinates)):
                self.prepend(newCoordinates)
        elif(direction=='RIGHT'):
            newCoordinates = Coordinates(lastHeadCoordinates.x()+1,lastHeadCoordinates.y())
            if(not self.contains(newCoordinates)):
                self.prepend(newCoordinates)
        self.removeLast()
        return self

    #def contains(self, element): # contains method for arrays like [x,y]
    #    elementInList = False
    #    cursor = self.headNode()
    #    while not cursor is None:
    #        if cursor.get()[0] == element[0] and cursor.get()[1] == element[1]:
    #            elementInList = True
    #            break
    #        cursor = cursor.next()
    #    return elementInList

    def contains(self, element): # contains method for coordinates object
        elementInList = False
        cursor = self.headNode()
        while not cursor is None:
            if cursor.get().x() == element.x() and cursor.get().y() == element.y():
                elementInList = True
                break
            cursor = cursor.next()
        return elementInList
