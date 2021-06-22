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



#figure out which group the cube is in
#apply function to move to next group?
def phase1(cube):
    edgeState = [False] * 32
    
    #if all edges good:
    # pass
    