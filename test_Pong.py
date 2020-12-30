from Pong import Pong
from Coordinates import Coordinates

def test_createPong():
    list = Pong(4,Coordinates(2,2),1,20)
    assert list.head().x() == 2 and list.head().y() == 2
    assert list.tail().head().x() == 2 and list.tail().head().y() == 3
    assert list.tail().tail().head().x() == 2 and list.tail().tail().head().y() == 4
    assert list.tail().tail().tail().head().x() == 2 and list.tail().tail().tail().head().y() == 5

def test_move():
    list = Pong(4,Coordinates(2,2),1,20)
    list.move(Coordinates(10,10))
    assert list.head().x() == 2 and list.head().y() == 3
    list.move(Coordinates(10,10))
    assert list.head().x() == 2 and list.head().y() == 4

    # Test limits top
    list.move(Coordinates(10,1))
    assert list.head().x() == 2 and list.head().y() == 3
    list.move(Coordinates(10,1))
    assert list.head().x() == 2 and list.head().y() == 2
    list.move(Coordinates(10,1))
    assert list.head().x() == 2 and list.head().y() == 1
    list.move(Coordinates(10,1))
    assert list.head().x() == 2 and list.head().y() == 1

    # Test limits bottom
    secondList = Pong(4,Coordinates(2,16),1,20)
    secondList.move(Coordinates(10,20))
    assert secondList.head().x() == 2 and secondList.head().y() == 17
    secondList.move(Coordinates(10,20))
    assert secondList.head().x() == 2 and secondList.head().y() == 17

def test_getPong():
    list = Pong(4,Coordinates(2,2),1,20)
    array = list.getPong()
    assert array[0].x() == 2 and array[0].y() == 2
    assert array[1].x() == 2 and array[1].y() == 3
    assert array[2].x() == 2 and array[2].y() == 4
    assert array[3].x() == 2 and array[3].y() == 5

def test_contains():
    list = Pong(4,Coordinates(2,2),1,20)
    assert list.contains(Coordinates(2,2))
    assert list.contains(Coordinates(2,3))
    assert list.contains(Coordinates(2,4))
    assert list.contains(Coordinates(2,5))