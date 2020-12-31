# Snakepong

Name: Emma Dossche

## Installed libraries
* Numpy : `pip install numpy`
* Pynput: `pip install pynput`

## How does the game works?
Start the application by running the UserIO.py file. Enter your name and press enter to start the game.

The pong is controlled automatically. The snake moves forward automatically, you can control the direction with the arrow keys.

You can score a point by pushing the ball to the left wall on the field. Your opponent gets a point when the ball gets to the right side of the field.

If someone scores 5 points the game is over.

Your opponent also gets a point when you crash your snake into a wall or if the snake hits itself. It is not possible to go down when the snake is going up or vice versa, go left when the snake is going right or vice versa so you won't lose points in that way.

Click on the ESC button to give up.

## Game analysis
The goal is to create an application so a user can play Snakepong. The game can be played in the console.

I used some classes to make the code more structured: an overview can be found below. For the game logic I used classes like Pong, Snake, Ball, Coordinates, ... For most of those classes, I have provided tests. To print the game in the console, I used the GameField class.

Pong and Snake inherit from the SingleLinkedList class. To use a single linked list proved to be a good solution for the Pong and Snake. The elements that the nodes contain are actually objects of the coordinates class.

I created the Coordinates class because I used to keep the coordinates in an array like this: `[x,y]`, but this made everything very difficult.

## Classes: methods & attributes

```
########################################################
Game
########################################################
- self.__player1
- self.__player2
- self.__gamefield
########################################################
+ __init__(self, player1, player2)
+ keypressed(self, key)
+ start(self)
+ gameOver(self)
########################################################
```

```
########################################################
User
########################################################
- self.__name
- self.__score
########################################################
+ __init__(self, name, score)
+ addPoint(self, points)
+ score(self)
+ username(self)
########################################################
```

```
########################################################
GameField
########################################################
- self.__height
- self.__width
- self.__player1
- self.__player2
- self.__field
- self.__ball
- self.__xDirectionBall
- self.__yDirectionBall
- self.__snake
- self.__snakeDirection
- self.__pong
########################################################
+ __init__(self, height, width, player1, player2)
+ initializeGameField(self)
+ makeField(self)
+ changeSnakeDirection(self, direction)
+ moveSnake(self)
+ moveBall(self)
+ updateField(self)
+ clearTerminal(self)
+ printField(self)
+ resetField(self)
+ printPlayerScores(self)
+ height(self)
+ width(self)
########################################################
```

```
########################################################
Snake(SingleLinkedList)
########################################################
- self.__length
########################################################
+ __init__(self, length, startX, startY)
+ getLength(self)
+ getSnake(self)
+ createSnake(self, startCoordinates)
+ newCoordinates(self, direction)
+ move(self, direction)
+ contains(self, element)
########################################################
```

```
########################################################
_Node
########################################################
- self.__element
- self.__next
########################################################
+ __init__(self, element, nextNode)
+ get(self)
+ next(self)
+ set_next(self, nextNode)
########################################################
```

```
########################################################
SingleLinkedList
########################################################
- self.__head
########################################################
+ __init__(self, first)
+ isEmpty(self)
+ head(self)
+ headNode(self)
+ tail(self)
+ prepend(self, element)
+ removeLast(self)
+ removeFirst(self)
+ append(self, element)
+ contains(self, element)
########################################################
```

```
########################################################
Coordinates
########################################################
- self.__x
- self.__y
########################################################
+ __init__(self,x,y)
+ x(self)
+ y(self)
+ setX(self, x)
+ setY(self, y)
########################################################
```

```
########################################################
Ball
########################################################
- self.__coordinates
########################################################
+ __init__(self, startCoordinates)
+ coordinates(self)
+ x(self)
+ y(self)
+ move(self, xDirection, yDirection)
########################################################
```

```
########################################################
Pong(SingleLinkedList)
########################################################
- self.__length
- self.__topLimit
- self.__bottomLimit
########################################################
+ __init__(self, length, startCoordinates, limitTop, limitBottom)
+ createPong(self, startCoordinates)
+ getPong(self)
+ move(self, ballCoordinates)
- _move(self,direction)
+ contains(self,element)
########################################################
```

## Sources
Sources are added at the bottom of each file.