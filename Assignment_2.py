#import numpy as np
import math
import random


column = 3
initialState_ = ((9,8,7),(6,5,4),(3,2,1))
goalState = (1,2,3,4,5,6,7,8,9)

def toBigTuple(tup):
    bigTuple = []
    for x in range(3):
        for y in range(3):
            bigTuple.append(tup[x][y])
    return tuple(bigTuple) 

def movingRight(tup, i):
    if (i % column ) < (column - 1 ):     
        possibleMove = list(tup) 
        temp = possibleMove[i + 1] # for swapping positions
        possibleMove[i + 1] = possibleMove[i]
        possibleMove[i] = temp
        tup = tuple(possibleMove)
    else:
        print("No Move\n")
    printTuple(tup)

def movingLeft(tup, i):
    if (i % column ) > 0:
        possibleMove = list(tup)
        temp = possibleMove[i - 1] # for swapping positions
        possibleMove[i -1] = possibleMove[i]
        possibleMove[i] = temp
        tup = tuple(possibleMove)
    else:
        print("No Move\n")
    printTuple(tup)

def movingUp(tup, i):
    if (i - column ) >= 0:
        possibleMove = list(tup)
        temp = possibleMove[i - 3] # for swapping positions
        possibleMove[i - 3] = possibleMove[i]
        possibleMove[i] = temp
        tup = tuple(possibleMove)
    else:
        print("No Move\n")
    printTuple(tup)

def movingDown(tup, i):
    if (i + column ) < len(tup):
        possibleMove = list(tup)
        temp = possibleMove[i + 3] # for swapping positions
        possibleMove[i + 3] = possibleMove[i]
        possibleMove[i] = temp
        tup = tuple(possibleMove)
    else:
        print("No Move\n")
    printTuple(tup)

def copyPuzzle(arr_1, arr_2):
    arr_2 = np.empty_like(arr_1)
    arr_2[:] = arr_1
    return arr_2

def copyTuple(tup_1, tup_2):
    tup_2 = deepcopy(tup_1)    

def printingArray(arr_):
    printArr =  arr_.reshape(3,3)
    print(printArr)

def printTuple(tup):
    print(tup[0], tup[1], tup[2])
    print(tup[3], tup[4], tup[5])
    print(tup[6], tup[7], tup[8],"\n") 

def goalReached(arr_):
    goal = True
    firstValue = arr_[0]
    for x in arr_:
        if firstValue > x:
            goal = False
            break
    return goal        
    

def depthFirstSearch(arr_):
    print("Dept First Search")
    openStack = []
    closed = []
    
class Node:
    childrenList = []

class Assignment_2:
    initialState = toBigTuple(initialState_)
    printTuple(initialState)
    option = input()
    while option != '0':
        if option == 'd':
            opt = int(input())    
            movingRight(initialState, opt)
        if option == 'a':
            opt = int(input())
            movingLeft(initialState, opt)
        if option == 'w':
            opt = int(input())
            movingUp(initialState, opt)
        if option == 'z':
            opt = int(input())
            movingDown(initialState, opt)    
        option = input()



    