import copy
class Node:
    def __init__(self,data,level,fval):
        """ Initialize the node with the data, level of the node and the calculated fvalue """
        self.data = data
        self.level = level
        self.fval = fval

    def generate_child(self):
        """ Generate child nodes from the given node by moving the blank space
            either in the four directions {up,down,left,right} """
        x,y = self.find(self.data,'9')
        self.generate_possible_children()    
        val_list = [[x,y-1],[x,y+1],[x-1,y],[x+1,y]]
        children = []
        for i in val_list:
            child = self.shuffle(self.data,x,y,i[0],i[1])
            if child is not None:
                child_node = Node(child,self.level+1,0)
                children.append(child_node)
        return children

    def generate_possible_children(self):
        #list_children = self.find_children()
        
        children = []
        values_to_move = []
        goal = [['1', '2', '3'], ['4', '5', '6'], [ '7', '8','9']]
        puz = copy.deepcopy(self.data)
        for i in range(3):
            for j in range(3):
                if(puz[i][j] != goal[i][j]):
                    values_to_move.append(puz[i][j])
                    self.possible_moves(children, puz, i, j)
        
        for i in range(len(children)):
            print("children ", children[i].data)
        x = input()
        

    def possible_moves(self, children, puz, col, row):
        self.moveRight(children, puz, col, row)
        self.moveLeft(children, puz, col, row)
        self.moveUp(children, puz, col, row)
        self.moveDown(children, puz, col, row)
        

        

    def moveRight( self, children, puz, col, row):
        if (row <= 1):
            puz_ = copy.deepcopy(puz)
            temp = puz_[col][row]
            puz_[col][row] = puz_[col][row + 1]
            puz_[col][row + 1] = temp 
            print("Right ",puz_)
            child_node = Node(puz_, self.level + 1, 0)
            children.append(child_node)


        

    def moveLeft( self, children, puz, col, row):
        if (row > 0):
            puz_ = copy.deepcopy(puz)
            temp = puz_[col][row]
            puz_[col][row] = puz_[col][row - 1]
            puz_[col][row - 1] = temp 
            print("Left ",puz_)
            child_node = Node(puz_, self.level+1, 0)
            children.append(child_node)
        
        

    def moveUp( self, children, puz, col, row):
        if (col > 0):
            puz_ = copy.deepcopy(puz)
            temp = puz_[col][row]
            puz_[col][row] = puz_[col - 1][row]
            puz_[col - 1][row] = temp 
            print("Up ",puz_)
            child_node = Node(puz_, self.level + 1, 0)
            children.append(child_node)
        

    def moveDown( self, children, puz, col, row):
        if (col <= 1):
            puz_ = copy.deepcopy(puz)
            temp = puz_[col][row]
            puz_[col][row] = puz_[col + 1][row]
            puz_[col + 1][row] = temp 
            print("Down ",puz_)
            child_node = Node(puz_, self.level+1, 0)
            children.append(child_node)
        

    def shuffle(self,puz,x1,y1,x2,y2):
        """ Move the blank space in the given direction and if the position value are out
            of limits the return None """
        if x2 >= 0 and x2 < 3 and y2 >= 0 and y2 < 3:
            temp_puz = []
            temp_puz = self.copy(puz)
            temp = temp_puz[x2][y2]
            temp_puz[x2][y2] = temp_puz[x1][y1]
            temp_puz[x1][y1] = temp
            return temp_puz
        else:
            return None
            

    def copy(self,root):
        """ Copy function to create a similar matrix of the given node"""
        temp = []
        for i in root:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp    
            
    def find(self,puz,x):
        for i in range(0,len(self.data)):
            for j in range(0,len(self.data)):
                if puz[i][j] == x:
                    return i,j
                   

class Puzzle:
    def __init__(self,size):
        """ Initialize the puzzle size by the specified size,open and closed lists to empty """
        self.n = size
        self.open = []
        self.closed = []



    def f(self, start, goal):
        """ Heuristic Function to calculate hueristic value f(x) = h(x) + g(x) """
        
        returnVal = self.h(start.data, goal)
        #print("level ", start.level,"returnVal ", returnVal )
        returnVal += start.level
        return returnVal

    def h(self,start,goal):
        """ Calculates the different between the given puzzles """
        temp = 0
        for i in range(0,self.n):
            for j in range(0,self.n):
                #print(i,j," ",start[i][j], " ",goal[i][j])
                if start[i][j] != goal[i][j]:
                    temp += 1
        #print("temp ", temp)
        return temp
        

    def process(self):
        start = [['1', '2', '3'], ['4', '5', '6'], [ '9', '8', '7']]
        goal = [['1', '2', '3'], ['4', '5', '6'], [ '7', '8','9']]
        start = Node(start,0,0)
        start.fval = self.f(start,goal)
        """ Put the start node in the open list"""
        self.open.append(start)
        while True:
            cur = self.open[0]
            print("")
            for i in cur.data:
                for j in i:
                    print(j,end=" ")
                print("")
            """ If the difference between current and goal node is 0 we have reached the goal node"""
            if(self.h(cur.data,goal) == 0):
                break
            for i in cur.generate_child():
                i.fval = self.f(i,goal)
                self.open.append(i)
            self.closed.append(cur)
            self.open.remove(self.open[0])

            """ sort the open list based on f value """
            self.open.sort(key = lambda x:x.fval)
            temp = self.open[0]
            self.open.clear()
            self.open.append(temp)
            #print("len(self.open) ",len(self.open)  )
            #for i in range(len(self.open)):
             #   print("self.open[",i,"].fval ",self.open[i].fval)
              #  print(self.open[i].data)
            #x = input()


puz = Puzzle(3)
puz.process()
