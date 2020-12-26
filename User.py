class User:
    def __init__(self, name, score = 0):
        self.__name = name
        self.__score = score

    def addPoint(self):
        self.__score += 1

    def score(self):
        return self.__score()