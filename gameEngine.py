import random

def makeGrid(size):
    lisF=[]
    lisT=[]
    for i in range(0,size,1):
        lisT=[]
        for j in range(0,size,1):
            lisT.append(" ")
        lisF.append(lisT)
    return lisF
            
def disp(grid,size,score):
    print("Score: ",score,"\n")
    for i in range(0,size,1):
        for j in range(0,size,1):
            if(j!=size-1):
                print(grid[i][j],end=" | ")
            else:
                print(grid[i][j],end=" ")
        print("\n")

def getBlanks(grid,size):
    lis=[]
    for i in range(0,size,1):
        for j in range(0,size,1):
            if(grid[i][j]==" "):
                lis.append(i*size+j)
    return lis
        
def generate2(grid,size):
    lis_blocks=getBlanks(grid,size)
    flag=1
    status=1
    while(flag):
        if(len(lis_blocks)!= 0):
            block=random.choice(lis_blocks)
            grid[int(block/size)][int(block%size)]=2
            flag=0
        else:
            status=0
        return grid,status

def initGame(size):
    grid = makeGrid(size)
    lis_blocks=list(range(0,size*size,1))
    for i in range(0,2,1):
        block=random.choice(lis_blocks)
        grid[int(block/size)][int(block%size)]=2
    return grid

def up(grid,size,score):
    for j in range(0,size,1):
        flag=0
        n=0
        n1=0
        i=0
        ind_i=0
        while(i<size):
            if (grid[i][j]!=" " and flag == 0):
                n=grid[i][j]
                ind_i=i
                i=i+1
                flag=1
            elif(grid[i][j]!=" " and flag == 1):
                n1=grid[i][j]
                if(n==n1):
                    grid[ind_i][j]=n+n1
                    grid[i][j]=" "
                    score+=n+n1
                    ind_i=i
                    i=i+1
                    flag=0
                else:
                    flag=0
            else:
                i=i+1
    count=0
    while(count!=2):
        for k in range(0,size,1):
            loc = -1
            flag = 0
            l=0
            while(l<size):
                if(grid[l][k]==" " and flag==0):
                    loc=l
                    l=l+1
                    flag=1
                elif(flag==1 and grid[l][k]!=" "):
                    grid[loc][k]=grid[l][k]
                    grid[l][k]=" "
                    flag=0
                else:
                    l=l+1
        count+=1
    return grid,score

def down(grid,size,score):
    for j in range(size-1,-1,-1):
        flag=0
        n=0
        n1=0
        i=size-1
        ind_i=size-1
        while(i>=0):
            if (grid[i][j]!=" " and flag == 0):
                n=grid[i][j]
                ind_i=i
                i=i-1
                flag=1
            elif(grid[i][j]!=" " and flag == 1):
                n1=grid[i][j]
                if(n==n1):
                    grid[ind_i][j]=n+n1
                    grid[i][j]=" "
                    score+=n+n1
                    ind_i=i
                    i=i-1
                    flag=0
                else:
                    flag=0
            else:
                i=i-1
    count=0
    while(count!=2):
        for k in range(size-1,-1,-1):
            loc = -1
            flag = 0
            l=size-1
            while(l>=0):
                if(grid[l][k]==" " and flag==0):
                    loc=l
                    l=l-1
                    flag=1
                elif(flag==1 and grid[l][k]!=" "):
                    grid[loc][k]=grid[l][k]
                    grid[l][k]=" "
                    flag=0
                else:
                    l=l-1
        count+=1
    return grid,score

def right(grid,size,score):
    for i in range(size-1,-1,-1):
        flag=0
        n=0
        n1=0
        j=size-1
        ind_j=size-1
        while(j>=0):
            if (grid[i][j]!=" " and flag == 0):
                n=grid[i][j]
                ind_j=j
                j=j-1
                flag=1
            elif(grid[i][j]!=" " and flag == 1):
                n1=grid[i][j]
                if(n==n1):
                    grid[i][ind_j]=n+n1
                    grid[i][j]=" "
                    score+=n+n1
                    ind_j=j
                    j=j-1
                    flag=0
                else:
                    flag=0
            else:
                j=j-1
    count=0
    while(count!=2):
        for l in range(size-1,-1,-1):
            loc = -1
            flag = 0
            k=size-1
            while (k>=0):
                if(grid[l][k]==" " and flag==0):
                    loc=k
                    k=k-1
                    flag=1
                elif(flag==1 and grid[l][k]!=" "):
                    grid[l][loc]=grid[l][k]
                    grid[l][k]=" "
                    flag=0
                else:
                    k=k-1
        count+=1
    return grid,score

def left(grid,size,score):
    for i in range(0,size,1):
        flag=0
        n=0
        n1=0
        j=0
        ind_j=0
        while(j<size):
            if (grid[i][j]!=" " and flag == 0):
                n=grid[i][j]
                ind_j=j
                j=j+1
                flag=1
            elif(grid[i][j]!=" " and flag == 1):
                n1=grid[i][j]
                if(n==n1):
                    grid[i][ind_j]=n+n1
                    grid[i][j]=" "
                    score+=n+n1
                    ind_j=j
                    j=j+1
                    flag=0
                else:
                    flag=0
            else:
                j=j+1

    count=0
    while(count!=2):        
        for l in range(0,size,1):
            loc = -1
            flag = 0
            k=0
            while(k<size):
                if(grid[l][k]==" " and flag==0):
                    loc=k
                    k=k+1
                    flag=1
                elif(flag==1 and grid[l][k]!=" "):
                    grid[l][loc]=grid[l][k]
                    grid[l][k]=" "
                    flag=0
                else:
                    k=k+1
        count+=1
    return grid,score

def hasWon(grid,status):
    for rows in grid:
        if 2048 in rows:
            return 200
    return status    

def gameController():
    size=int(input("Enter grid size"))
    flag=1
    score=0
    status=1
    grid = initGame(size)
    gameGrids=[list(map(list,grid))]
    while(flag):
        print(gameGrids)
        disp(grid,size,score)
        
        choice = input(" Press k to escape. u to undo")

        if(choice=='k'):
            flag=0
            
        elif(choice=='w'):
            grid,score = up(grid,size,score)
            grid,status = generate2(grid,size)
            status=hasWon(grid,status)
            
            
        elif(choice=='s'):
            grid,score = down(grid,size,score)
            grid,status = generate2(grid,size)
            status=hasWon(grid,status)
            
        elif(choice=='d'):
            grid,score = right(grid,size,score)
            grid,status = generate2(grid,size)
            status=hasWon(grid,status)
            
        elif(choice=='a'):
            grid,score = left(grid,size,score)
            grid,status = generate2(grid,size)
            status=hasWon(grid,status)

        elif(choice=='u'):
            if (len(gameGrids)>1):
                gameGrids.pop()
                grid=gameGrids.pop()
            else:
                print("cannot Undo further")

        else:
            continue
        gameGrids.append(list(map(list,grid)))
            