from SLL import SingleLinkedList
import numpy as np

class Snake(SingleLinkedList):
    def __init__(self, length, startX, startY):
        super().__init__()
        self.__length = length
        self.createSnake(startX,startY) 

    def get(self):
        return self

    def createSnake(self, startX, startY):
        self.prepend(np.array([startX,startY]))
        for offset in range(1, self.__length):
            self.append(np.array([startX,startY+offset]))
