from SLL import SingleLinkedList
from Coordinates import Coordinates
import numpy as np

class Pong(SingleLinkedList):
    def __init__(self, length, startCoordinates, limitTop, limitBottom):
        super().__init__()
        self.__length = length
        self.__topLimit = limitTop
        self.__bottomLimit = limitBottom
        self.createPong(startCoordinates)

    def createPong(self, startCoordinates):
        self.prepend(startCoordinates)
        for offset in range(1, self.__length):
            self.append(Coordinates(startCoordinates.x(),startCoordinates.y()+offset))

    def getPong(self):
        array = np.empty([self.__length],dtype=Coordinates)
        cursor = self.headNode()
        for i in range(0,self.__length):
            array[i] = cursor.get()
            cursor = cursor.next()
        return array
        
    def move(self, ballCoordinates):
        if(ballCoordinates.y()>self.head().y()+round((self.__length-1)/2)):
            self.__move('DOWN')           
        elif(ballCoordinates.y()<self.head().y()+round((self.__length-1)/2)):
            self.__move('UP')         
        return self

    def __move(self, direction):
        if(direction == 'UP' and self.head().y()>self.__topLimit):
            self.prepend(Coordinates(self.head().x(),self.head().y()-1))
            self.removeLast()
        elif(direction == 'DOWN' and self.head().y()+self.__length-1<self.__bottomLimit):
            self.append(Coordinates(self.head().x(),self.head().y()+self.__length))
            self.removeFirst()

    def contains(self, element):
        elementInList = False
        cursor = self.headNode()
        while not cursor is None:
            if cursor.get().x() == element.x() and cursor.get().y() == element.y():
                elementInList = True
                break
            cursor = cursor.next()
        return elementInList