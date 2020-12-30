from Pong import Pong
from Coordinates import Coordinates

def test_createPong():
    list = Pong(4,Coordinates(2,2),1,20)
    assert list.head().x() == 2 and list.head().y() == 2
    assert list.tail().head().x() == 2 and list.tail().head().y() == 3
    assert list.tail().tail().head().x() == 2 and list.tail().tail().head().y() == 4
    assert list.tail().tail().tail().head().x() == 2 and list.tail().tail().tail().head().y() == 5
