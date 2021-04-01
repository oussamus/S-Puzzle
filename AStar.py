import copy
import time as time
childrenProcess = []
class Node:
    def __init__(self, data, level, fval):
        self.data = data
        self.level = level
        self.fval = fval
        self.parent = None


    def generate_possible_children(self):

        # list_children = self.find_children()
        global goal
        children = []
        values_to_move = []
        puz = copy.deepcopy(self.data)
        for i in range(rows):
            for j in range(columns):
                if (puz[i][j] != goal[i][j]):
                    values_to_move.append(puz[i][j])
                    self.possible_moves(children, puz, i, j)
        return children
        

    def possible_moves(self, children, puz, col, row):
        # Checks all the possible moves for each number misplaced in the puzzle
        # These functions create the node according to the moves, if the node doesn't excists in the open list,
        # it will be added to it.
        self.moveRight(children, puz, col, row)
        self.moveLeft(children, puz, col, row)
        self.moveUp(children, puz, col, row)
        self.moveDown(children, puz, col, row)
        #for i in range(len(children)):
        #    print(children[i].data, children[i].parent)
        #x = input()

    def moveRight( self, children, puz, col, row):
        if (row <= (rows - 2)):
            addingNode = False
            puz_ = copy.deepcopy(puz)
            temp = puz_[col][row]
            puz_[col][row] = puz_[col][row + 1]
            puz_[col][row + 1] = temp
            if(len(childrenProcess) == 0):
                child_node = Node(puz_, self.level + 1, 0)
                child_node.parent = self
                children.append(child_node)
                #print("First Right added")
                return
            else:
                for j in range(len(childrenProcess)):
                    if( puz_ != childrenProcess[j].data):
                        addingNode = True
                        break
                if(addingNode):
                    child_node = Node(puz_, self.level + 1, 0)
                    child_node.parent = self
                    children.append(child_node)
                #    print(" chikkkkkk ",child_node.parent.data)
                

    def moveLeft( self, children, puz, col, row):
        if (row > 0):
            addingNode = False
            puz_ = copy.deepcopy(puz)
            temp = puz_[col][row]
            puz_[col][row] = puz_[col][row - 1]
            puz_[col][row - 1] = temp 
            for j in range(len(childrenProcess)):
                if( puz_ != childrenProcess[j].data):
                    addingNode = True
                    break
            if(addingNode):
                child_node = Node(puz_, self.level + 1, 0)
                child_node.parent = self
                children.append(child_node)
                

        
        

    def moveUp( self, children, puz, col, row):
        if (col > 0):
            addingNode = False
            puz_ = copy.deepcopy(puz)
            temp = puz_[col][row]
            puz_[col][row] = puz_[col - 1][row]
            puz_[col - 1][row] = temp 
            #print("Up ",puz_)
            for j in range(len(childrenProcess)):
                if( puz_ != childrenProcess[j].data):
                    addingNode = True
                    break
            if(addingNode):
                child_node = Node(puz_, self.level + 1, 0)
                child_node.parent = self
                children.append(child_node)
                #self.parent = self

        

    def moveDown( self, children, puz, col, row):
        if (col <= (columns - 2)):
            addingNode = False
            puz_ = copy.deepcopy(puz)
            temp = puz_[col][row]
            puz_[col][row] = puz_[col + 1][row]
            puz_[col + 1][row] = temp 
            #print("Down ",puz_)
            for j in range(len(childrenProcess)):
                if( puz_ != childrenProcess[j].data):
                    addingNode = True
                    break
            if(addingNode):
                child_node = Node(puz_, self.level + 1, 0)
                child_node.parent = self
                children.append(child_node)
                #self.parent = self



def find(puzzle, rows, cols, target):
    for i in range(rows):
        for j in range(cols):
            if puzzle[i][j] == target:
                return (i,j)
    return None

class Puzzle:
    def __init__(self, size):
        self.n = size
        self.open = []
        self.closed = []



    def f(self, start, goal): # f() = g() + h()
        returnVal = self.h(start.data, goal)
        #print("level ", start.level,"returnVal ", returnVal )
        returnVal += start.level
        return returnVal

    def f2(self, start, goal):
        returnVal = self.h2(start.data) 
        returnVal += start.level
        return returnVal

    def h(self, start, goal): # The basic heuristic funtion 
        temp = 0
        for i in range(0,self.n):
            for j in range(0,self.n):
                #print(i,j," ",start[i][j], " ",goal[i][j])
                if start[i][j] != goal[i][j]:
                    temp += 1
        #print("temp ", temp)
        return temp
    def h2(self, start):
        global rows, columns, goal
        distance  = 0
        for i in range(self.n):
            for j in range(self.n):
                if start[i][j] != goal[i][j]:
                    (real_row,real_col) = find(goal, rows, columns, start[i][j])
                    distance += abs(real_col - j) + abs(real_row - i)
        return distance



    def A1(self):
        self.open.clear()
        self.closed.clear()
        global init
        global goal
        stoptime = time.time() + 60
        start = Node(init, 0, 0)
        start.fval = self.f(start, goal)
        self.open.append(start)
        while True:
            cur = self.open[0]
            # Printing the current puzzle nicely
            print("\n")
            for row in cur.data:
                print("{: >3} {: >3} {: >3}".format(*row))
            # The loop breaks when the heuristic function returns 0. The goal is found
            if time.time() > stoptime:
                break
            if self.h(cur.data, goal) == 0:
                return cur
                break

            for i in cur.generate_possible_children():
                i.fval = self.f(i,goal)
                if i.fval == 0: 
                    return i
                # To check later on (in possible_moves function ) if we have duplicate nodes
                childrenProcess.append(i) 
                self.open.append(i)
            self.closed.append(cur)
            self.open.remove(self.open[0])
            # We sort the open list according the f value 
            self.open.sort(key = lambda x:x.fval)
            #for i in range(len(self.open)):
             #   print(self.open[i].data)
            #x = input()

    def A2(self):
        self.open.clear()
        self.closed.clear()
        global init
        global goal
        stoptime = time.time() + 60
        start = Node(init, 0, 0)
        start.fval = self.f2(start, goal)
        self.open.append(start)
        while True:
            cur = self.open[0]
            # Printing the current puzzle nicely
            print("\n")
            for row in cur.data:
                print("{: >3} {: >3} {: >3}".format(*row))
            # The loop breaks when the heuristic function returns 0. The goal is found
            if time.time() > stoptime:
                break
            if self.h2(cur.data) == 0:
                return cur
                break

            for i in cur.generate_possible_children():
                i.fval = self.f2(i,goal)
                if i.fval == 0: 
                    return i
                # To check later on (in possible_moves function ) if we have duplicate nodes
                childrenProcess.append(i) 
                self.open.append(i)
            self.closed.append(cur)
            self.open.remove(self.open[0])
            # We sort the open list according the f value 
            self.open.sort(key = lambda x:x.fval)
            #for i in range(len(self.open)):
             #   print(self.open[i].data)
            #x = input()


def printNode(node):
    out = ""
    for i in range(rows):
        out += "\n" + str(node.data[i])
    return out

def getSolutionPath(node):
    ls1 = list()
    parent = node.parent
    ls1.append(node)
    out = ""

    while parent:
        ls1.append(parent)
        parent = parent.parent

    for n in reversed(ls1):
        out += "\n" + printNode(n)

    return out



#init = [[1,2,3,4],[5,6,7,8],[14,10,11,12],[13,9,15,16]]
#goal = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
init = [[2,3,5], [1,8,6],[9,7,4]]
goal = [[1,2,3],[4,5,6],[7,8,9]]
columns = len(init)
rows = len(init[0])

starTime = time.time()
puz = Puzzle(columns)
ret = puz.A2()
endTime = time.time() + 60
print(endTime - starTime)
print(getSolutionPath(ret))
