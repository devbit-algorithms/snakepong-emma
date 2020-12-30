from User import User
from pynput import keyboard
from Game import Game

print("Welcome to the snakepong application.\n")

username = input("Please enter your name: ")
player = User(username)
cpu = User("CPU")

game = Game(player, cpu)

print("\nUse the arrow keys to control the snake.\nTry to get the ball to the left side of the board.\nDefend your side (the right side of the board).\nGood Luck!")
userinput = input("\nPress enter to start")

def on_release(key):
    #print('{0} released'.format(key))
    game.keyPressed('{0}'.format(key))
    
    if key == keyboard.Key.esc:
        # Stop listener
        return False

listener = keyboard.Listener(
    on_release=on_release)
listener.start()

game.start()


# Sources:
# key listener: https://stackoverflow.com/questions/11918999/key-listeners-in-python 
# pynput: https://pypi.org/project/pynput/
# pynput docs: https://pynput.readthedocs.io/en/latest/
