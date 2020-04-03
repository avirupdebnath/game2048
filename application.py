import gameEngine
import copy
from flask import Flask,request,render_template,flash,redirect,url_for,session
from datetime import timedelta
app = Flask(__name__)
app.debug = False 
app.secret_key="random_string"
app.permanent_session_lifetime=timedelta(days=1)

@app.route("/", methods = ['GET','POST'] ) 
def gameControllerPost():
    if 'grid' not in session:
        session.clear()
        session['size']=4
        session['grid']=gameEngine.initGame(session['size'])
        session['score']=0
        session['allscores']=[0,0]
        session['gameGrids']= [list(map(list,session['grid']))]
        session['gameGrids'].append(list(map(list,session['grid'])))
        session['status']=1
        score=session['score']
        grid=session['grid']
        return render_template('game.html',score=score,grid1=grid[0][0],grid2=grid[0][1],grid3=grid[0][2],grid4=grid[0][3],grid5=grid[1][0],grid6=grid[1][1],grid7=grid[1][2],grid8=grid[1][3],grid9=grid[2][0],grid10=grid[2][1],grid11=grid[2][2],grid12=grid[2][3],grid13=grid[3][0],grid14=grid[3][1],grid15=grid[3][2],grid16=grid[3][3])
    
    elif request.method== 'GET':
        size=session['size'] 
        grid =session['grid']
        score =session['score']
        gameGrids=session['gameGrids']
        allscores=session['allscores']
        status=session['status']
        return render_template('game.html',score=score,grid1=grid[0][0],grid2=grid[0][1],grid3=grid[0][2],grid4=grid[0][3],grid5=grid[1][0],grid6=grid[1][1],grid7=grid[1][2],grid8=grid[1][3],grid9=grid[2][0],grid10=grid[2][1],grid11=grid[2][2],grid12=grid[2][3],grid13=grid[3][0],grid14=grid[3][1],grid15=grid[3][2],grid16=grid[3][3])
    
    elif request.method== 'POST':
        size=session['size'] 
        grid =session['grid']
        score =session['score']
        gameGrids=session['gameGrids']
        allscores=session['allscores']
        status=session['status']
        
        choice=str(request.form['control'])
        if(choice=='UP'):
            grid,score = gameEngine.up(grid,size,score)
            grid,status = gameEngine.generate2(grid,size)
            status=gameEngine.hasWon(grid,status)
                
                
        elif(choice=='DOWN'):
            grid,score = gameEngine.down(grid,size,score)
            grid,status = gameEngine.generate2(grid,size)
            status=gameEngine.hasWon(grid,status)
                
                
        elif(choice=='RIGHT'):
            grid,score = gameEngine.right(grid,size,score)
            grid,status = gameEngine.generate2(grid,size)
            status=gameEngine.hasWon(grid,status)
                
                
        elif(choice=='LEFT'):
            grid,score = gameEngine.left(grid,size,score)
            grid,status = gameEngine.generate2(grid,size)
            status=gameEngine.hasWon(grid,status)
            
        elif(choice=='UNDO'):
            if (len(gameGrids)>1):
                gameGrids.pop()
                allscores.pop()
                grid=gameGrids.pop()
                score=allscores.pop()
        
        elif(choice=='RESET'):
            session.clear()
            return redirect("/")
           
        else:
            pass
        allscores.append(score)
        gameGrids.append(list(map(list,grid)))  

        session['grid']=grid
        session['score']=score
        session['allscores']=allscores
        session['gameGrids']= gameGrids
        session['status']=status

        if (status==200):
            session.clear()
            return render_template('gamewin.html',score=score)

        elif (status == 1):
            return render_template('game.html',score=score,grid1=grid[0][0],grid2=grid[0][1],grid3=grid[0][2],grid4=grid[0][3],grid5=grid[1][0],grid6=grid[1][1],grid7=grid[1][2],grid8=grid[1][3],grid9=grid[2][0],grid10=grid[2][1],grid11=grid[2][2],grid12=grid[2][3],grid13=grid[3][0],grid14=grid[3][1],grid15=grid[3][2],grid16=grid[3][3])
        
        else:
            session.clear()
            return render_template('gameover.html',score=score)

if __name__ == "__main__":
    app.run()