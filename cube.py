from sty import bg, ef, rs
import time
import sys
import const

cube_face = [[1,2,2],[1,2,3],[4,2,3]]
moves = {
    "R": 2,
    "L": 0,
    "F": 1,
    "B": 3,
    "U": 4,
    "D": 5
}

color = {
    0:bg(214),
    1:bg.green,
    2:bg.red,
    3:bg.blue,
    4:bg.white,
    5:bg(226)
}

def create_cube(): # creates a standard rubiks cube as an array
    cube = [[] for x in range(0,3)]
    colors = [bg(214), bg.green, bg.red, bg.blue, bg.white, bg(226)]
    #colors = [1, 2, 3, 4, 5, 6]
    for x in range(0,4):
        piece = x
        
        for y in range(0, 3):
            cube[0].append([piece, piece, piece])
    for x in range(0,2):
        piece = x+4
        
        for y in range(0, 3):
            cube[x+1].append([piece, piece, piece])

    return cube

def create_test_cube(): # creates a numbered cube used to debug
    cube = [[] for x in range(0,3)]
    for y in range(0, 12):
        n=3*y
        cube[0].append([str(n) + (" "*(len(str(n)) == 1)), str(n+1) + (" "*(len(str(n+1)) == 1)), str(n+2) + (" "*(len(str(n+1)) == 1))])
        
    for y in range(0,3):
        n=3*y
        cube[1].append([str(n)+" ",str(n+1)+" ",str(n+2)+" "])

    for y in range(0,3):
        n=3*y
        cube[2].append([str(n)+" ",str(n+1)+" ",str(n+2)+" "])
    return cube

def print_face(face): # deprecated prints a face given the array
    print(face[0])
    print(face[1])
    print(face[2])

def print_cube(cube): # prints the cube as a flattened 2d shape

    for y in range(0, 3):
        print("            ", end='')
        for x in range(0,3):
            print(color[cube[1][x][2-y]] + "  " + bg(0), " ", end='')
        print("")
        print("")

    for y in range(0, 3):
        for x in range(0, 12):
            print(color[cube[0][x][2-y]] + "  " + bg(0)," ", end='')
        print("")
        print("")

    for y in range(0, 3):
        print("            ", end='')
        for x in range(0,3):
            print(color[cube[2][x][2-y]] + "  " + bg(0), " ", end='')
        print("")
        print("")

def print_dt(cube): #debug prints the cube as it appears as an array
    for x in range(0,3):
        for y in range(0,18):
            print(cube[y][x], " ", end='')
        print("")
    
def f_turn(cube, side): # defines how to change cube face
    c = cube
    
    #3n+1,2,3
    if((side>=0) and (side<=3)):
        c[0][(3*side)+0][0], c[0][(3*side)+0][2], c[0][(3*side)+2][2], c[0][(3*side)+2][0] = c[0][(3*side)+2][0], c[0][(3*side)+0][0], c[0][(3*side)+0][2], c[0][(3*side)+2][2]
        c[0][(3*side)+0][1], c[0][(3*side)+1][2], c[0][(3*side)+2][1], c[0][(3*side)+1][0] = c[0][(3*side)+1][0], c[0][(3*side)+0][1], c[0][(3*side)+1][2], c[0][(3*side)+2][1]
    elif(side == 4):
        c[1][0][0], c[1][0][2], c[1][2][2], c[1][2][0] = c[1][2][0], c[1][0][0], c[1][0][2], c[1][2][2]
        c[1][0][1], c[1][1][2], c[1][2][1], c[1][1][0] = c[1][1][0], c[1][0][1], c[1][1][2], c[1][2][1]
    else:
        c[2][0][0], c[2][0][2], c[2][2][2], c[2][2][0] = c[2][2][0], c[2][0][0], c[2][0][2], c[2][2][2]
        c[2][0][1], c[2][1][2], c[2][2][1], c[2][1][0] = c[2][1][0], c[2][0][1], c[2][1][2], c[2][2][1]
    return c

def a_turn(cube, side): # fix the adjacent squares
    c = cube
    read = []
    if(side == 0): 
        for x in range(0,3):
            c[0][-9][2-x], c[2][0][(2-x)], c[0][-1][0+x], c[1][0][(2-x)]  = c[1][0][(2-x)], c[0][-9][2-x], c[2][0][(2-x)], c[0][-1][0+x]
    elif(side == 2):
        for x in range(0, 3):
            c[0][-3][2-x], c[2][2][((2-x) * -1) + 2], c[0][5][0+x], c[1][2][(2-x) * (-1) + 2]  = c[1][2][(2-x) * (-1) + 2], c[0][-3][2-x], c[2][2][(2-x) * (-1) + 2], c[0][5][0+x]
    elif(side == 1):
        for x in range(0,3):
            c[0][(side*3)-9][(2-x) * (((side==3)*-2)+1) + (side-1)], c[2][(2-x) * ((((side-1)==2)*-2)+1) + (side-1)][(-1*side)+3], c[0][(side*3)-1][0+x], c[1][0+x][side-1] = c[1][0+x][side-1], c[0][(side*3)-9][(2-x) * ((((side-1)==2)*-2)+1) + (side-1)], c[2][(2-x) * ((((side-1)==2)*-2)+1) + (side-1)][(-1*side)+3], c[0][(side*3)-1][0+x]
    elif(side == 3):
        
        for x in range(0,3):
            c[0][0][2-x], c[2][x][0], c[0][8][x], c[1][2-x][2] = c[1][2-x][2], c[0][0][2-x], c[2][x][0], c[0][8][x]
    # not completely sure how this works but it does

    elif(side == 4):
        for x in range(0,12):
            read.append(c[0][x][2])
        
        for x in range(-3, 9):
            c[0][x-3][2] = read[x]
    else:
        for x in range(0,12):
            read.append(c[0][x][0])
        
        for x in range(-3, 9): 
            c[0][x+3][0] = read[x]
        
    return c

def F(cube, side): # rotate face clockwise
    c = cube
    c = f_turn(c, side)
    c = a_turn(c, side)
    return cube

def scramble(c, m):
    cube = c
    if(m==""):
        return create_cube()
    x = m
    l = x.split(" ")
    #print(l)
    #print_cube(cube)
    
    for move in l:
   
        if("2" in move):
            
            face = move[0]
            cube = F(cube, moves[face])
            cube = F(cube, moves[face])
        elif("'" in move):
            
            face = move[0]
            
            cube = F(cube, moves[face])
            cube = F(cube, moves[face])
            cube = F(cube, moves[face])
        else:
            face = move[0]
            cube = F(cube, moves[face])
        #print_cube(cube)
    return cube
def unpack(cube):
    out = []
    ans = ""
    for y in range(3):
        for x in range(3):
            out.append(cube[1][x][2-y])
    for y in range(3):
        for x in range(3):
            out.append(cube[0][x+6][2-y])
    for y in range(3):
        for x in range(3):
            out.append(cube[0][x+3][2-y])
    for y in range(3):
        for x in range(3):
            out.append(cube[2][x][2-y])
    for y in range(3):
        for x in range(3):
            out.append(cube[0][x][2-y])
    for y in range(3):
        for x in range(3):
            out.append(cube[0][x+9][2-y])
    print(out)
    for num in out:
        ans+=const.num_to_face[num]
    return ans
if __name__ == "__main__":
    args = str(sys.argv[1])
    opt_scramble = str(sys.argv[2])
    if(args == "--test-all"):
        cube = scramble(create_cube(), opt_scramble)
        print_cube(cube)
    elif(args == "--bench"):
        start_time = time.time()
        for x in range(0, 10000):
            cube = scramble(create_cube(), "R2 U' L' R2 D2 B F2 U F' R' F D' U F2 U F2 L U2 R' F")
        print("--- %s seconds ---" % (time.time() - start_time))
    elif(args == "--test_turns"):
        cube = create_cube()
        while(True):
            print_cube(cube)
            x = input()
            cube = scramble(cube, x)
    elif(args == "--gen_scramble"): # urfdlb
        cube = scramble(create_cube(), opt_scramble)
        print(unpack(cube))
        print_cube(cube)
    else:
        cube = create_test_cube()
        print(cube)
        print(unpack(cube))


# print_cube(cube)
# cube = F(cube, 5)
# print_cube(cube)

#print_dt(cube)