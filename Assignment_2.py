import copy

class Tree(object):
    '''Tree that will contain a state in its data'''
    def __init__(self):
        self.data = None
        self.parent = None
        self.children = list()
        self.depth = None


def depthFirst(Tree):
    '''Not Complete'''
    current_node = Tree
    while True:
        child_state = generateChild(current_node.data)
        current_state = child_state
        if not current_state:
            if current_state.isFinal():
                print("final")
                break
            else:
                temp_node = Tree()
                temp_node.depth = current_node.depth +1
                temp_node.parent = current_node
                temp_node.data = generateChild(current_state)
                current_node.children.append(temp_node)

                current_node = temp_node



        else:
            print("no")

def generateChild(state):
    '''takes a state as a parameter, tries all possible actions, and returns a child state or None when there are no more child states '''
    #next_state = open_list.pop(0)

    #iterating through all the possible moveUp actions
    for i in list(range(0,rows)):
        for j in list(range(0, column)):
            out = state.moveUp(i, j)

            if not out: continue

            if out in open_list:
                continue
            else:
                return out

    #iterating through all the possible moveDown actions
    for i in list(range(0,rows)):
        for j in list(range(0, column)):
            out = state.moveDown(i, j)

            if not out: continue

            if out in open_list:
                continue
            else:
                return out
    #iterating through all the possible moveRight actions
    for i in list(range(0,rows)):
        for j in list(range(0, column)):
            out = state.moveRight(i, j)

            if not out: continue

            if out in open_list:
                continue
            else:
                return out
    #iterating through all the possible moveLeft actions
    for i in list(range(0,rows)):
        for j in list(range(0, column)):
            out = state.moveLeft(i, j)

            if not out: continue

            if out in open_list:
                continue
            else:
                return out
    return None

class State(object):
    '''State that represents the puzzle. It contains the tuple/array (array for now) and a list of changes applied to it'''

    def __init__(self, Data, log ):
        self.Data = Data
        self.log = log

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
            print("No Move\n")

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
            print("No Move\n")

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
            print("No Move\n")

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
        if self.Data == goal:
            return True
        else:
            return False
column =3
rows = 3
goal = [[1,2,3],[4,5,6],[7,8,9]]
open_list = list()
closed_list = None

if __name__ == '__main__':

    init = [[9, 8, 5], [4, 5, 3], [7, 2, 1]]

    #starting intial state
    s = State(init,list())

    #creating tree root
    root = Tree()

    #loading the initial state into the root of the tree
    root.data = s

    #adding the inital state to the open list
    open_list.append(s)

    #test stuff
    open_list.append(s.moveUp(1,0))
    generateChild(s)

