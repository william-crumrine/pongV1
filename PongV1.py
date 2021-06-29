#termProject.py
from graphics import *
from time import sleep
from messageBox import *

win = GraphWin("Two Player Pong",1000,600)
#def players():
#player 1 (blue) 
player1A = Rectangle(Point(100,285),Point(110,205))
player1A.draw(win)
player1A.setFill('blue')
player1B = Rectangle(Point(600,285),Point(610,205))
player1B.draw(win)
player1B.setFill('blue')
#player 2 (red)
player2A = Rectangle(Point(900,285),Point(890,205))
player2A.draw(win)
player2A.setFill('red')
player2B = Rectangle(Point(400,285),Point(390,205))
player2B.draw(win)
player2B.setFill('red')
scoreP1 = 0
scoreP2 = 0
win.done = False #continue the game until this is set to 1 in keyProcess


def keyProcess(event):
    print(repr(event.char), str(event.char), event.keycode, event.keysym, "is pressed.")
    if event.keysym=="w" and player2A.getP1().getY()>175:
        player2A.move(0,-5)
        player2B.move(0,-5)
    elif event.keysym=="s" and player2A.getP2().getY()<515:
        player2A.move(0,5)
        player2B.move(0,5)
    elif event.keysym=="Up" and player1A.getP1().getY()>175:
        player1A.move(0,-5)
        player1B.move(0,-5)
    elif event.keysym=="Down" and player1A.getP2().getY()<515:
        player1A.move(0,5)
        player1B.move(0,5)
    elif event.keysym=="Escape":
        resetGame()
##        ball.move(500-ball.getCenter().getX(), 345-ball.getCenter().getY())
    elif event.keysym=="q":
        win.gameOn = False
##    else:
##        player1A.move(0,0)
##        player1B.move(0,0)
##        player2A.move(0,0)
##        player2B.move(0,0)
        
#playing feild
win.master.bind('<Key>', keyProcess)
win.setBackground('green')
p1 = Point(0,95)
p2 = Point(1000,90)
scoreBox = Rectangle(p1,p2)
scoreBox.draw(win)
scoreBox.setFill('white')
bLine = Rectangle(Point(0,600),Point(1000,595))
bLine.draw(win)
bLine.setFill('white')
ulGoal = Rectangle(Point(0,95),Point(50,220))
ulGoal.draw(win)
ulGoal.setFill('white')
urGoal = Rectangle(Point(1000,95),Point(950,220))
urGoal.draw(win)
urGoal.setFill('white')
blGoal = Rectangle(Point(0,595),Point(50,470))
blGoal.draw(win)
blGoal.setFill('white')
brGoal = Rectangle(Point(1000,595),Point(950,470))
brGoal.draw(win)
brGoal.setFill('white')
middleLine = Rectangle(Point(495,95),Point(505,595))
middleLine.draw(win)
middleLine.setFill('white')

#ball
ball = Circle(Point(500,345),15)
ball.setFill('black')

def resetGame():
    player1A.move(100-player1A.getP1().getX(), 285-player1A.getP1().getY())
    player1B.move(600-player1B.getP1().getX(), 285-player1B.getP1().getY())
    player2A.move(400-player2A.getP1().getX(), 285-player2A.getP1().getY())
    player2B.move(900-player2B.getP1().getX(), 285-player2B.getP1().getY())
    ball.move(500-ball.getCenter().getX(), 345-ball.getCenter().getY())
    

#def ballMoving():

dx = 1
dy = -1

scoreBoard = Text(Point(500,45), "Player1: 0, Player2: 0")
scoreBoard.draw(win)

while win.done==False:
    win.gameOn = True #the game starts
    resetGame()
    ball.draw(win)
    while win.gameOn == True:
        ball.move(dx,dy)
        center = ball.getCenter()
        centerRP1A = player1A.getCenter()
        centerRP1Ay = centerRP1A.getY()
        centerRP1B = player1B.getCenter()
        centerRP1By = centerRP1B.getY()
        centerRP2A = player2A.getCenter()
        centerRP2Ay = centerRP2A.getY()
        centerRP2B = player2B.getCenter()
        centerRP2By = centerRP2B.getY()
        if center.getY() +15 > 595:
            dy = -dy
        if center.getY() - 15 < 95:
            dy = -dy
        #ulgoal
        if center.getX() - 15 < 50 and center.getY() < 220: 
            dx = - dx
        if center.getX() < 50 and center.getY() - 15 == 220:
            dy = - dy
        #blgoal
        if center.getX() - 15 < 50 and center.getY() > 470: 
            dx = - dx
        if center.getX() < 50 and center.getY() +15 == 470:
            dy = - dy
        #urgoal
        if center.getX() + 15 > 950 and center.getY() < 220: 
            dx = - dx
        if center.getX() > 950 and center.getY() -15 == 220:
            dy = - dy
        #brgoal
        if center.getX() + 15 > 950 and center.getY() > 470: 
            dx = - dx
        if center.getX() > 950 and center.getY() +15 == 470:
            dy = - dy
        if center.getX() > 1000:
            print("Goal! Player 1 scored.")
            win.gameOn = False
            scoreP1 = scoreP1 + 1
            ball.undraw()
        if center.getX() < 0:
            print("Goal! Player 2 scored.")
            win.gameOn = False
            scoreP2 = scoreP2 + 1
            ball.undraw()
        #player1A
        if center.getX() + 15 == 100 and center.getY() < centerRP1Ay + 40 and center.getY() > centerRP1Ay - 40:
            dx = -dx
        if center.getX() - 15 == 110 and center.getY() < centerRP1Ay + 40 and center.getY() > centerRP1Ay - 40:
            dx = -dx
        if center.getX() > 100 and center.getX() < 110 and center.getY() + 15 == centerRP1Ay -40:
            dy = - dy
        if center.getX() > 100 and center.getX() < 110 and center.getY() -15 == centerRP1Ay +40:
            dy = - dy
        #player1B
        if center.getX() + 15 == 600 and center.getY() < centerRP1By + 40 and center.getY() > centerRP1By - 40:
            dx = -dx
        if center.getX() - 15 == 610 and center.getY() < centerRP1By + 40 and center.getY() > centerRP1By - 40:
            dx = -dx
        if center.getX() > 600 and center.getX() < 610 and center.getY() +15 == centerRP1By - 40:
            dy = - dy
        if center.getX() > 600 and center.getX() < 610 and center.getY() - 15 == centerRP1By + 40:
            dy = - dy
        #player2A
        if center.getX() + 15 == 890 and center.getY() < centerRP2Ay + 40 and center.getY() > centerRP2Ay - 40:
            dx = -dx
        if center.getX() - 15 == 900 and center.getY() < centerRP2Ay + 40 and center.getY() > centerRP2Ay - 40:
            dx = -dx
        if center.getX() > 890 and center.getX() < 900 and center.getY() + 15 == centerRP2Ay - 40:
            dy = - dy
        if center.getX() > 890 and center.getX() < 900 and center.getY() - 15 == centerRP2Ay + 40:
            dy = - dy
        #player2B
        if center.getX() + 15 == 390 and center.getY() < centerRP2By + 40 and center.getY() > centerRP2By - 40:
            dx = -dx
        if center.getX() - 15 == 400 and center.getY() < centerRP2By + 40 and center.getY() > centerRP2By - 40:
            dx = -dx
        if center.getX() > 390 and center.getX() < 400 and center.getY() + 15 == centerRP2By - 40:
            dy = - dy
        if center.getX() > 390 and center.getX() < 400 and center.getY() - 15 == centerRP2By + 40:
            dy = - dy
        sleep(0.02)
    scoreBoard.setText("Player 1: " + str(scoreP1) + ", Player 2: " + str(scoreP2))
    if scoreP1 == 10:
        win.close()
        win1 = GraphWin("WINNER!", 250, 250)
        winner1 = Text (Point(125,125), "Player 1 wins!")
        winner1.draw(win1)
    if scoreP2 == 10:
        win.close()
        win2 = GraphWin("WINNER!", 250, 250)
        winner2 = Text(Point(125,125), "Player 2 wins!")
        winner2.draw(win2)
    resp = messageBox2("Click yes to continue")
    if resp != "yes":
        break
    else:
        resetGame()
        

win.close()

    

