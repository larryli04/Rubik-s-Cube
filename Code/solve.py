import cube
from sty import bg, ef, rs

test_scramble = ""

white = '\x1b[107m  \x1b[48;5;0m'
orange = '\x1b[48;5;214m  \x1b[48;5;0m'
green = '\x1b[42m  \x1b[48;5;0m'
red = '\x1b[41m  \x1b[48;5;0m'
blue = '\x1b[44m  \x1b[48;5;0m'
yellow = '\x1b[48;5;226m  \x1b[48;5;0m'

adj1 = ["0 0 1", "0 1 2","0 1 0","0 2 1","0 6 1","0 7 2","0 7 0","0 8 1", "1 1 2", "0 4 2", "2 1 2", "0 11 1", "1 0 1","2 0 1","0 3 1","0 5 1","1 2 1","2 1 1","0 9 1", "2 1 0", "1 1 0", "0 4 0"]
adj2 = ["0 11 1", "1 0 1","2 0 1","0 3 1","0 5 1","1 2 1","2 1 1","0 9 1", "2 1 0", "1 1 0", "0 4 0", "0 0 1", "0 1 2","0 1 0","0 2 1","0 6 1","0 7 2","0 7 0","0 8 1", "1 1 2", "0 4 2", "2 1 2"]

moves = ["U", "U'", "D", "D'", "L", "L'", "R", "R'", "F", "F'", "B", "B'"]
def adj(x, y, z):
    index = adj1.index(str(x)+" "+str(y)+" "+str(z))
    return adj2[index]

class State:
    def __init__(self, data, depth, parent, moves):
        self.children = []
        self.parent = parent
        self.data = data
        self.moves = moves
        self.depth = depth
        self.score = 0

    
    def PrintTree(self, dep):
        print("    "*dep, end="")
        print(self.data, self.depth)

        for child in self.children:
            child.PrintTree(dep+1)

    def gen(self, dep):
        # print(dep)
        if(dep > 0):
            for move in moves:
                self.children.append(State(cube.scramble(self.data, move), self.depth+1, self, self.moves+" "+move))
            
            #print(self.data)
            # print(self.children)
            for child in self.children:
                
                if(True):
                    child.gen(dep-1)
                else:
                    pass

    
    
    #idea of protected squares

        
def white_cross(cube): #only need 4 moves per edge
    c = cube
    dest = ["1 2 1", "1 1 2", "1 0 1", "1 1 0"] #red, blue, orange, green
    for value in adj1:
        l = value.split(" ")
        x=int(l[0])
        y=int(l[1])
        z=int(l[2])
        if(cube[x][y][z] == white):
            adj_color = adj(x, y, z)
            #then find destination
    if(cube[1][1][2] == white):
        print("yes")
    return c

c = State(cube.scramble(cube.create_cube(), test_scramble), 0, 0, "")
cube.print_cube(c.data)
c.gen(4)

print(adj(0,4,2))