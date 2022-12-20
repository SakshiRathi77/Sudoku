import random

def MakeSudoku(level):
    if level==1:
        range_g=9 
        el=15
    elif level==2:
        range_g=6
        el=10
    elif level==3:
        range_g=3
        el=5
        print("reached")
    Grid=[[0 for i in range(range_g)] for j in range (range_g)]

    Gridi=[[0 for i in range(range_g)] for j in range (range_g)]
    Gridt=[[False for i in range(range_g)] for j in range (range_g)]
    
    for i in range(range_g):
        for j in range(range_g):
            Grid[i][j]=0
            Gridt[i][j]=False


    for i in   range(el):
        row=random.randrange(range_g)
        col=random.randrange(range_g)
        num= random.randrange(1,range_g+1)
        while(not Checkvalid(range_g,Grid,row ,col,num)  or Grid[row][col]!=0):
            row=random.randrange(range_g)
            col=random.randrange(range_g)
            num= random.randrange(1,range_g)
            # print(1)
                
        Grid[row][col]=num
        Gridi[row][col]=num
        Gridt[row][col]=True   
        # print(Grid)
    printgrid(Grid,range_g)
    return Gridi,Grid,Gridt,range_g


def Solve_MakeSudoku(level):
    if level==1:
        range_g=9 
        el=15
    elif level==2:
        range_g=6
        el=10
    elif level==3:
        range_g=3
        el=5
        print("reached")
    Grid=[[0 for i in range(range_g)] for j in range (range_g)]
    print(Grid)
    Gridi=[[0 for i in range(range_g)] for j in range (range_g)]
    Gridt=[[False for i in range(range_g)] for j in range (range_g)]
    
    for i in range(range_g):
        for j in range(range_g):
            Grid[i][j]=0
            Gridt[i][j]=False
    print(Grid)

    for i in   range(el):
        row=i
        col=random.randrange(range_g)
        num= random.randrange(1,range_g+1)
        while(not Checkvalid(range_g,Grid,row ,col,num)  or Grid[row][col]!=0):
            row=i
            col=random.randrange(range_g)
            num= random.randrange(1,range_g)
            # print(1)
                
        Grid[row][col]=num
        Gridi[row][col]=num
        Gridt[row][col]=True   
        # print(Grid)
    printgrid(Grid,range_g)
    return Gridi,Grid,Gridt,range_g



def printgrid(Grid,range_g):
    # global Grid
    table1="|--------"*(range_g//3)

    for x in range (len(Grid)):
        if x%3==0:
            print(table1)
        for y in range(range_g):
            if y%3==0:
                print("| ", end=" ")
            print(Grid[x][y], end=" ") 
            if y==range_g-1:
                print(" |",end=" ")
        if x==range_g-1:
            print()
            print(table1)
        print()
    
def Checkvalid(range_g,Grid,row,col,num):
    # global Grid
    valid=True
    for x in range(range_g):
        if Grid[x][col]==num:
            valid=False
        for y in range(range_g):
            if Grid[row][y]==num:
                valid=False
    rowsection=row//3
    colsection=col//3
    for  x in range(3):
        if Grid[rowsection+x][y]==num:
            valid=False
        for y in range(3):
            if Grid[x][colsection+y]==num:
                valid=False   

    return valid     

def userinput(Grid,Gridt,undo_list):
    
    row=int(input("enter the row you want to add element :"))
    row=row-1
    col=int(input("enter the column you want to add element :"))
    col=col-1
    num=int(input("enter the value you want to add element :"))
    if(row>len(Grid) or col>len(Grid) or num>len(Grid)):
        print("please enter valid value !!")
    else:
        if (Gridt[row][col]):
            print("Sorry,it is fixed.\n try again!!")
        else:
            Grid[row][col]=num
            l=[row,col]
            undo_list.append(l)
    return Grid
def undo_move(Grid,undo_list):
    if len(undo_list)==0:
        print("Grid do not contain any element you entered!!!")
    else:
        a=undo_list.pop()
        Grid[a[0]][a[1]]=0
        print("Move is undo!")
    return Grid,undo_list


def check_result(range_g,Grid,row,col,num):
    valid=True
    for x in range(range_g):
        if Grid[x][col]==num and x!=row:
            valid=False
        for y in range(range_g):
            if Grid[row][y]==num and y!=col:
                valid=False
    rowsection=row//3
    colsection=col//3
    y=0
    for  x in range(3):
        for y in range(3):
            if Grid[rowsection+x][y]==num and y!=col and rowsection+x!=row:
                valid=False
            if Grid[x][colsection+y]==num and x!=row and y!=colsection+y:
                valid=False   

    return valid   

def result(range_g,Grid):
    for i in range (range_g):
        for j in range(range_g):
            
            num=Grid[i][j]
            if (check_result(range_g,Grid,i,j,num)==False or Grid[i][j]==0 ):
                print("You have entered wrong value at",i
                ,"th row ",j,"th column,try again!")
                return False
    return True
            
undo_list=[]

a=input("Enter your name to start the game\n")
if(a):
    print("Hey "+a+"\n!!!!!!!!welcome to Sudoku!!!!!!!!")
    a=int(input("enter the level of difficulty\n1.difficult\n2.Medium\n3.Easy\n"))
    intial_grid,Grid,Gridt,range_g=MakeSudoku(a)

    
    while(True):
        ch=int(input("Enter your choice :\n1.play\n2.Undo\n3.Default\n4.Submit\n5.Quit\n"))
        if ch==1:
            Grid=userinput(Grid,Gridt,undo_list)
            printgrid(Grid,range_g)
        elif ch==2:
            Grid,undo_list=undo_move(Grid,undo_list)
            printgrid(Grid,range_g)
        elif ch==3:
            print(intial_grid,range_g)
            Grid=intial_grid[:]
            printgrid(Grid,range_g)
        elif ch==4:
            if(result(range_g,Grid)):
                print("wow!!You are genius\n <<<<<<<<<<<YOU WON>>>>>>>>>")
            
        elif ch==5:
            exit()
        else:
            print("please enter the valid choice !!!")
else:
    print("GAME END >>><<<<NO INPUTS GIVEN!!!")

    
