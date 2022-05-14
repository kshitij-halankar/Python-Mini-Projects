import sys
import random

n = 0
tries = 3

def randomNumber():
    global n
    n = random.randint(1,10)

def hint1():
    if(n%2 == 0):
        print("Even Number")
    else:
        print("odd number")

def hint2():
    if(n%5 == 0):
        print("Number is divisible by 5")
    else:
        if(n%3 == 0):
            print("Number is divisible by 3")
        else:
            if(n%4 == 0):
                print("Number is divisible by 4")
            else:
                print("Number is prime")
        

def hint3():
    global n
    sq = n * n
    print("The square of number is: ",sq) 

def hints():
    print("Tries remaining: ")

def guess():
    global n
    g = int(input("Guess :"))
    #print(n)
    #print(g)
    if(g == n):
        print("Congrats! Correct Answer")
        sys.exit()
    else:
        global tries
        tries = tries - 1
        print("Wrong! Number of tries remaining:",tries)
randomNumber()
print("Guess Number between 1 to 10")
#print(n)
print("Hint 1:")
hint1()
guess()

v = input("Press 'h' for hint or 'c' continue guessing")
if(v == 'h'):
    hint2()
guess()

v = input("Press 'h' for hint or 'c' continue guessing")
if(v == 'h'):
    hint3()
guess()
print("No more tries remaining")

