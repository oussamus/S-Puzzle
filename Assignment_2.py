import copy
from collections import deque
open_list = deque()
closed_list = list()

class Tree(object):
    '''Tree that will contain a state in its data'''
    def __init__(self):
        self.data = None
        self.parent = None
        self.children = list()
        self.depth = None


def depthFirst():
    '''Not Complete'''
    current_node = Tree
    global open_list
    # generate the child state
    #child_state = generateChild(current_node.data)

    counter =0
    while len(open_list) > 0:

        if counter == 4:
            counter =0
            print(current_state.log)
        counter += 1
        current_state = open_list.pop()
        closed_list.append(current_state)
        
        #print(len(open_list))
        #if current state is not null (i.e if a child exists
        if current_state:

            #check if it is the final state
            if current_state.isFinal():
                print(current_state)
                break
            #if not, creat anew tree node, fit the child state into it, set all the variables for the node, and set current node to that node
            else:

                children = generateAllChildren(current_state)
                open_list.extend(children)
                #open_list = children + open_list
                '''
                temp_node = Tree()
                #setting parameters
                temp_node.depth = current_node.depth +1
                temp_node.parent = current_node
                #inserting the state in the open queue
                open_list.append(current_state)
                #fitting the child state
                temp_node.data = generateChild(open_list.pop())

                #adding the child node to the children of the current node
                current_node.children.append(temp_node)

                #setting the current node = to the child node
                current_node = temp_node
                '''
        #if there are no child states in the current state
        else:
            '''
            #add the current state into the closed list
            closed_list.append(current_state)
            current_node = current_node.parent
            print("no")
            '''
def difference(child_list, open_list, closed_list):
    returning_list = list()
    for state in child_list:
        if state in open_list or state in closed_list:
            continue
        else:
            returning_list.append(state)
    return returning_list



def generateAllChildren(state):
    returning = list()

    # iterating through all the possible moveUp actions
    for i in list(range(0, rows)):
        for j in list(range(0, column)):
            out = state.moveUp(i, j)

            if not out: continue


            returning.append(out)

    # iterating through all the possible moveDown actions
    for i in list(range(0, rows)):
        for j in list(range(0, column)):
            out = state.moveDown(i, j)

            if not out: continue

            returning.append(out)
    # iterating through all the possible moveRight actions
    for i in list(range(0, rows)):
        for j in list(range(0, column)):
            out = state.moveRight(i, j)

            if not out: continue


            returning.append(out)
    # iterating through all the possible moveLeft actions
    for i in list(range(0, rows)):
        for j in list(range(0, column)):
            out = state.moveLeft(i, j)

            if not out: continue

            returning.append(out)

    filtered_list = difference(returning,open_list,closed_list)
    return filtered_list

def generateChild(state):
    '''takes a state as a parameter, tries all possible actions, and returns a child state or None when there are no more child states '''
    #next_state = open_list.pop(0)

    #iterating through all the possible moveUp actions
    for i in list(range(0,rows)):
        for j in list(range(0, column)):
            out = state.moveUp(i, j)

            if not out: continue

            if out in open_list or out in closed_list:
                continue
            else:
                return out

    #iterating through all the possible moveDown actions
    for i in list(range(0,rows)):
        for j in list(range(0, column)):
            out = state.moveDown(i, j)

            if not out: continue

            if out in open_list or out in closed_list:
                continue
            else:
                return out
    #iterating through all the possible moveRight actions
    for i in list(range(0,rows)):
        for j in list(range(0, column)):
            out = state.moveRight(i, j)

            if not out: continue

            if out in open_list or out in closed_list:
                continue
            else:
                return out
    #iterating through all the possible moveLeft actions
    for i in list(range(0,rows)):
        for j in list(range(0, column)):
            out = state.moveLeft(i, j)

            if not out: continue

            if out in open_list or out in closed_list:
                continue
            else:
                return out
    return None

class State(object):
    '''State that represents the puzzle. It contains the tuple/array (array for now) and a list of changes applied to it'''

    def __init__(self, Data, log ):
        self.Data = Data
        self.log = log
        self.parent = None
        self.children = list()
        self.depth = None

    def addLog(self, log):
        self.log.append(log)
    def printData(self):
        for row in self.Data:
            print(row)

    def moveLeft(self,row, col):
        if (col % column) > 0:
            new_state = State(copy.deepcopy(self.Data),copy.deepcopy(self.log) ) #making a deep copy of the state
            possibleMove = new_state.Data
            temp = possibleMove[row][col -1]  # for swapping positions
            possibleMove[row][col - 1] = possibleMove[row][col]
            possibleMove[row][col] = temp
            new_state.log.append((row, col, "left"))    #adding the chages to the log of the state (the slides said we should do so, we don't use them yet)
            return new_state    #returns the new child state

        else:
            return None

    def moveRight(self, row, col):
        if (col % column) < (column - 1):
            new_state = State(copy.deepcopy(self.Data), copy.deepcopy(self.log))
            possibleMove = new_state.Data
            temp = possibleMove[row][col + 1]  # for swapping positions
            possibleMove[row][col + 1] = possibleMove[row][col]
            possibleMove[row][col] = temp
            new_state.log.append((row, col, "right"))
            return new_state
        else:
            return None

    def moveDown(self, row, col):
        if row < rows -1:
            new_state = State(copy.deepcopy(self.Data), copy.deepcopy(self.log))
            possibleMove = new_state.Data
            temp = possibleMove[row +1][col]  # for swapping positions
            possibleMove[row +1][col] = possibleMove[row][col]
            possibleMove[row][col] = temp
            new_state.log.append((row, col, "down"))
            return new_state
        else:
            return None

    def moveUp(self, row, col):
        if row > 0 and row <= rows :
            new_state = State(copy.deepcopy(self.Data), copy.deepcopy(self.log))
            possibleMove = new_state.Data
            temp = possibleMove[row -1][col]  # for swapping positions
            possibleMove[row -1][col] = possibleMove[row][col]
            possibleMove[row][col] = temp
            new_state.log.append((row, col, "up"))
            return new_state
        else:
            return None

    def __eq__(self, state2):
        '''overwriting the equals method'''
        if self.Data == state2.Data:
            return True
        else:
            return False

    def isFinal(self):
        global goal
        if self.Data == goal:
            return True
        else:
            return False
column =3
rows = 3
goal = [[1,2,3],[4,5,6],[7,8,9]]


if __name__ == '__main__':

    init = [[1, 2, 3], [4, 5, 6], [8, 7, 9]]

    open_list = deque()
    closed_list = list()

    #starting intial state
    s = State(init,list())
    s.depth = 1

    #creating tree root
    #root = Tree()

    #loading the initial state into the root of the tree
    #root.data = s

    #adding the inital state to the open list
    open_list.append(s)
    depthFirst()

