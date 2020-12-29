from Snake import Snake
from Coordinates import Coordinates
import numpy as np

def test_createSnake():
    list = Snake(4,1,1) # createSnake() is automatically called in __init__
    assert list.head().x() == 1 and list.head().y() == 1
    assert list.tail().head().x() == 1 and list.tail().head().y() == 2
    assert list.tail().tail().head().x() == 1 and list.tail().tail().head().y() == 3
    assert list.tail().tail().tail().head().x() == 1 and list.tail().tail().tail().head().y() == 4
    assert list.tail().tail().tail().tail().isEmpty()
    # assert len(list.head()) == len([1,1])
    # assert all([a == b for a, b in zip(list.head(),[1,1])])
    # assert len(list.tail().head()) == len([1,2])
    # assert all([a == b for a, b in zip(list.tail().head(),[1,2])])
    # assert len(list.tail().tail().head()) == len([1,3])
    # assert all([a == b for a, b in zip(list.tail().tail().head(),[1,3])])
    # assert len(list.tail().tail().tail().head()) == len([1,4])
    # assert all([a == b for a, b in zip(list.tail().tail().tail().head(),[1,4])])
    # assert list.tail().tail().tail().tail().isEmpty()

def test_move():
    list = Snake(4,1,1)
    list.move('RIGHT')
    assert list.head().x() == 2 and list.head().y() == 1
    assert list.tail().head().x() == 1 and list.tail().head().y() == 1
    assert list.tail().tail().head().x() == 1 and list.tail().tail().head().y() == 2
    assert list.tail().tail().tail().head().x() == 1 and list.tail().tail().tail().head().y() == 3
    assert list.tail().tail().tail().tail().isEmpty()
    # assert len(list.head()) == len([2,1])
    # assert all([a == b for a, b in zip(list.head(),[2,1])])
    # assert len(list.tail().head()) == len([1,1])
    # assert all([a == b for a, b in zip(list.tail().head(),[1,1])])
    # assert len(list.tail().tail().head()) == len([1,2])
    # assert all([a == b for a, b in zip(list.tail().tail().head(),[1,2])])
    # assert len(list.tail().tail().tail().head()) == len([1,3])
    # assert all([a == b for a, b in zip(list.tail().tail().tail().head(),[1,3])])
    # assert list.tail().tail().tail().tail().isEmpty()

def test_contains():
    list = Snake(4,1,1)
    assert list.contains(Coordinates(1,2))
    assert list.contains(Coordinates(1,1))
    assert not list.contains(Coordinates(1,5))
    # assert list.contains([1,2])
    # assert list.contains([1,1])
    # assert not list.contains ([1,5])

def test_getSnake():
    list = Snake(4,1,1)
    array = list.getSnake()
    assert array[0].x() == 1 and array[0].y() == 1
    assert array[1].x() == 1 and array[1].y() == 2
    assert array[2].x() == 1 and array[2].y() == 3
    assert array[3].x() == 1 and array[3].y() == 4
    

# Sources: 
# check arrays with pytest: https://stackoverflow.com/questions/46914222/how-can-i-assert-lists-equality-with-pytest
    