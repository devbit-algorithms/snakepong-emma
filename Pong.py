from SLL import SingleLinkedList
from Coordinates import Coordinates
import numpy as np

class Pong(SingleLinkedList):
    def __init__(self, length, startCoordinates):
        super().__init__()
        self.__length = length
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
            self.prepend(Coordinates(self.head().x(),self.head().y()+1))
        elif(ballCoordinates.y()<self.head().y()+round((self.__length-1)/2)):
            self.prepend(Coordinates(self.head().x(),self.head().y()-1))
        self.removeLast()
        return self
