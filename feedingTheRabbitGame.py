import sys
import ast

a = input("Please enter feeding map as a list:\n")
board = ast.literal_eval(a)
c = input("Please enter direction of movements as a list:\n")
mov = ast.literal_eval(c)


ob = "" #"output board - board çıktısı"
g = "" #"desired output form of board input - board girdisinin istenilen çıktı hali"
h = "" #"straight string of board input - board girdisinin düz string hali"
ce = 0 #"counter of elements - eleman sayacı" 
cr = 0 #"counter of rows - satır sayacı"

for i in range(0,len(board)):
    b = (board[i])
    c = len(b)
    cr+=1
    for j in range (c):
        ce+=1
        h+=(b[j])
        g+=(b[j]+" ")
    g+=("\n")

row = cr #"number of lines on the board - boarddaki satır sayısı"
column = ce//cr #"number of columns on the board - boarddaki sütun sayısı"

rb = h.index("*") #"the number of the rabbit's place in the list - tavşanın listedeki yerinin sayısı"

ror = rb//column #"row of rabbit - tavşanın satırı"
cor = rb%column #"column of rabbit - tavşanın sütunu"

por = [ror, cor]

point = 0

def oob(): #operation output board
    global ob
    for i in range(0,len(board)):
        b = (board[i])
        c = len(b)
        for j in range (c):
            ob+=(b[j]+" ")
        ob+=("\n")

    print("Your board is:")
    print(g[0:len(g)-1])
    print("\nYour output should be like this:")
    print(ob[0:len(ob)-1])
    print("Your score:",point)
    
def obj():
    if board[m][n] == "W":
        wall()
    if board[m][n] == "C" :
        carrot()
    if board[m][n] == "A" :
        apple()
    if board[m][n] == "M" :
        meat()
    if board[m][n] == "P" :
        poison()
    if board[m][n] == "X" :
        empty()
        
def wall():
    global k
    global l
    m = k
    n = l
    
def carrot():
    global k
    global l
    global por
    por = [m, n]
    board[k][l] = 'X'
    k = por[0]
    l = por[1]
    board[k][l] = '*'
    global point
    point+=10
    
def apple():
    global k
    global l
    global por
    por = [m, n]
    board[k][l] = 'X'
    k = por[0]
    l = por[1]
    board[k][l] = '*'
    global point
    point+=5
    
def meat():
    global k
    global l
    global por
    por = [m, n]
    board[k][l] = 'X'
    k = por[0]
    l = por[1]
    board[k][l] = '*'
    global point
    point-=5

def poison():
    global k
    global l
    global por
    por = [m, n]
    board[k][l] = 'X'
    k = por[0]
    l = por[1]
    board[k][l] = '*'
    print("Your score:", point)
    oob()
    sys.exit()
    
def empty():
    global k
    global l
    global por
    por = [m, n]
    board[k][l] = 'X'
    k = por[0]
    l = por[1]
    board[k][l] = '*'


def up():
    global k
    global l
    global m
    global n
    k = por[0]
    l = por[1]
    if k > 0:
        m = k-1
    else :
        m = k
    n = l
    obj()
        
def down():
    global k
    global l
    global m
    global n
    k = por[0]
    l = por[1]
    if k < row-1:
        m = k+1
    else :
        m = k
    n = l
    obj()
    
def right():
    global k
    global l
    global m
    global n
    k = por[0]
    l = por[1]
    m = k
    if l < column-1 :
        n = l+1
    else :
        n = l
    obj()
    
def left():
    global k
    global l
    global m
    global n
    k = por[0]
    l = por[1]
    m = k
    if l > 0:
        n = l-1
    else :
        n = l
    obj()
       
for i in range(0,len(mov)):
    com = mov[i]
    if com == "U":
        up()
    if com == "D":
        down()
    if com == "R":
        right()
    if com == "L":
        left()

oob()