import gameEngine
from flask import Flask,request,render_template,flash,redirect,url_for
app = Flask(__name__)
app.debug = False 
app.secret_key="random string"
size=0
grid=[]
flag=0
score=0
allscores=[]
gameGrids=[]

@app.route("/")
def gameController(): 
    global size 
    global grid 
    global flag
    global score
    global gameGrids
    global allscores
    size = 4
    grid = gameEngine.initGame(size)
    allscores.append(score)
    allscores.append(score)
    flag=0
    score=0 
    allscores=[]
    gameGrids=[]
    gameGrids= [list(map(list,grid))]
    gameGrids.append(list(map(list,grid)))
    return render_template('game.html',score=score,grid1=grid[0][0],grid2=grid[0][1],grid3=grid[0][2],grid4=grid[0][3],grid5=grid[1][0],grid6=grid[1][1],grid7=grid[1][2],grid8=grid[1][3],grid9=grid[2][0],grid10=grid[2][1],grid11=grid[2][2],grid12=grid[2][3],grid13=grid[3][0],grid14=grid[3][1],grid15=grid[3][2],grid16=grid[3][3])

@app.route("/", methods = ['POST','GET'] ) 
def gameControllerPost():
    global grid
    global size
    global flag
    global score
    global gameGrids
    global allscores
    status=1
    choice=str(request.form['control'])
    if(choice=='UP'):
        grid,score = gameEngine.up(grid,size,score)
        grid,status = gameEngine.generate2(grid,size)
            
            
    elif(choice=='DOWN'):
        grid,score = gameEngine.down(grid,size,score)
        grid,status = gameEngine.generate2(grid,size)
            
            
    elif(choice=='RIGHT'):
        grid,score = gameEngine.right(grid,size,score)
        grid,status = gameEngine.generate2(grid,size)
            
            
    elif(choice=='LEFT'):
        grid,score = gameEngine.left(grid,size,score)
        grid,status = gameEngine.generate2(grid,size)
           
    elif(choice=='UNDO'):
        if (len(gameGrids)>1):
            gameGrids.pop()
            allscores.pop()
            grid=gameGrids.pop()
            score=allscores.pop()
    elif(choice=='RESET'):
        size = 4
        grid = gameEngine.initGame(size)
        score=0
        allscores=[]
        gameGrids=[]
        allscores.append(score)
        allscores.append(score)
        flag=0 
        gameGrids= [list(map(list,grid))]
        gameGrids.append(list(map(list,grid)))
        return render_template('game.html',score=score,grid1=grid[0][0],grid2=grid[0][1],grid3=grid[0][2],grid4=grid[0][3],grid5=grid[1][0],grid6=grid[1][1],grid7=grid[1][2],grid8=grid[1][3],grid9=grid[2][0],grid10=grid[2][1],grid11=grid[2][2],grid12=grid[2][3],grid13=grid[3][0],grid14=grid[3][1],grid15=grid[3][2],grid16=grid[3][3])
    allscores.append(score)
    gameGrids.append(list(map(list,grid)))  
    if (status == 1):
        return render_template('game.html',score=score,grid1=grid[0][0],grid2=grid[0][1],grid3=grid[0][2],grid4=grid[0][3],grid5=grid[1][0],grid6=grid[1][1],grid7=grid[1][2],grid8=grid[1][3],grid9=grid[2][0],grid10=grid[2][1],grid11=grid[2][2],grid12=grid[2][3],grid13=grid[3][0],grid14=grid[3][1],grid15=grid[3][2],grid16=grid[3][3])
    else:
        return render_template('gameover.html',score=score)
if __name__ == "__main__":
    app.run(threaded=False)
