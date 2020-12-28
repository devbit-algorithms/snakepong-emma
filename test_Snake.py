from Snake import Snake
import numpy as np

def test_createSnake():
    list = Snake(4,1,1) # createSnake() is automatically called in __init__
    assert len(list.head()) == len([1,1])
    assert all([a == b for a, b in zip(list.head(),[1,1])])
    assert len(list.tail().head()) == len([1,2])
    assert all([a == b for a, b in zip(list.tail().head(),[1,2])])
    assert len(list.tail().tail().head()) == len([1,3])
    assert all([a == b for a, b in zip(list.tail().tail().head(),[1,3])])
    assert len(list.tail().tail().tail().head()) == len([1,4])
    assert all([a == b for a, b in zip(list.tail().tail().tail().head(),[1,4])])
    assert list.tail().tail().tail().tail().isEmpty()


# Sources: 
# check arrays with pytest: https://stackoverflow.com/questions/46914222/how-can-i-assert-lists-equality-with-pytest
    