import pyautogui as pg
import autopy as ap

sizeX = pg.size().width
sizeY = pg.size().height

x1 = 100
y1 = 50

pg.FAILSAFE = False

def click():
    curPosX = pg.position().x
    curPosY = pg.position().y
    pg.leftClick(curPosX,curPosY)

def mouseMovement(direction):
    x = pg.position().x
    y = pg.position().y

    if(direction == "incX"):
        x = x + 10
    elif(direction == "incY"):
        y = y + 10
    elif(direction == "decX"):
        x = x - 10
    elif(direction == "decY"):
        y = y - 10

    print(x,y)
    ap.mouse.smooth_move(x, y)
    

# mouseMovement(10,0)