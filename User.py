class User:
    def __init__(self, name, score = 0):
        self.__name = name
        self.__score = score

    def addPoint(self, points=1):
        self.__score += points

    def score(self):
        return self.__score

    def username(self):
        return self.__name