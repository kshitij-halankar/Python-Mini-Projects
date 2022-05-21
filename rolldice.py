import sys
import random

def randomNumber():
    print("You rolled: ",random.randint(1,6))
    roll()

def roll():
    i = input("press 'r' to roll the dice and 'q' to quit: ")
    if(i == 'r'):
        randomNumber()
    else:
        print("Bye")
        sys.exit()
roll()
