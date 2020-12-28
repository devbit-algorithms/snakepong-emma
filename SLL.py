class _Node:
    def __init__(self, element, nextNode):
        self.__element = element
        self.__next = nextNode

    def get(self):
        return self.__element

    def next(self):
        return self.__next

class SingleLinkedList:
    def __init__(self, first = None):
        self.__head = first

    def isEmpty(self):
        return self.__head is None

    def head(self):
        if self.isEmpty():
            return None
        else:
            return self.__head.get()

    def tail(self):
        if self.isEmpty():
            return SingleLinkedList()
        else:
            return SingleLinkedList(self.__head.next())

    def prepend(self, element):
        self.__head = _Node(element, self.__head)
        return self

    def removeLast(self):
        if self.isEmpty() or self.__head.next() is None:
            return SingleLinkedList()
        else:
            cursor = self.__head
            while not cursor.next().next() is None:
                cursor = cursor.next()
            cursor.set_next(None)
            return self