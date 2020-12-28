from SLL import *

def test_isEmpty():
    list = SingleLinkedList()
    assert list.isEmpty() == True

def test_prepend():
    list = SingleLinkedList()
    list.prepend(5)
    assert list.head() == 5
    list.prepend(6)
    assert list.head() == 6
    assert list.tail().head() == 5

def test_tail():
    list = SingleLinkedList()
    list.prepend(5).prepend(4).prepend(3)
    assert list.tail().head() == 4
    assert list.tail().tail().head() == 5
    assert list.tail().tail().tail().isEmpty() == True

def test_removeLast():
    list = SingleLinkedList()
    list.prepend(5).prepend(4).prepend(3)
    list = list.removeLast()
    assert list.tail().tail().isEmpty() == True