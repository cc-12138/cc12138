import pygame as pg
import time
import sys
import os
import math
from pygame.locals import *

#棋子类
class stornpoint:
    def __init__(self,x,y,state):
        self.x=x            #表示x轴坐标
        self.y=y            #表示y轴坐标
        self.state=state    #表示该点状态，0表示没有棋子，1表示为白棋，2表示为黑棋

#初始化棋盘
def initchesssquare(x,y):
    initChessList = []
    for i in range(15):
        row_list = []       #该行坐标
        for j in range(15):
            pointX = i*40+x
            pointY = j*40+y
            sp = stornpoint(pointX,pointY,0)
            row_list.append(sp)
        initChesslist.append(row_list)
    return initChessList

#判断函数
def judgeresult(x,y,state):
    count = 0
    #纵向检查
    for i in range(x-4,x+1):
        if i<0 or i>14:
            continue
        for k in range(5):
            if i+k>14:
                break
            if initChesslist[i+k][y].state == state:
                count += 1
            else:
                count = 0
        if count == 5:        
            return True
    #横向检查
    for j in range(y-4,y+1):
        if j<0 or j>14:
            continue
        for k in range(5):
            if j+k>14:
                break
            if initChesslist[x][j+k].state == state:
                count += 1
            else:
                count = 0
        if count == 5:
            return True
    #从左上到右下检查
    for i,j in zip(range(x-4,x+1),range(y-4,y+1)):
        if i<0 or j<0 or i>14 or j>14:
            continue
        for k in range(5):
            if i+k>14 or j+k>14:
                break
            if initChesslist[i+k][j+k].state == state:
                count += 1
            else:
                count = 0
        if count == 5:
            return True
    #从左下到右上检查
    for i,j in zip(range(x-4,x+1),range(y+4,y-1,-1)):
        if i<0 or j<0 or i>14 or j>14:
            continue
        for k in range(5):
            if i+k>14 or j-k<0:
                break
            if initChesslist[i+k][j-k].state == state:
                count += 1
            else:
                count = 0
        if count == 5:
            return True

#初始化界面大小
width = 628
height = 617
size = (width, height)
pg.init()
screen = pg.display.set_mode(size)

#加载图片
begin = pg.image.load("./picture/begin.png").convert()
chesssquare = pg.image.load("./picture/chesssquare.png").convert()
white = pg.image.load("./picture/whitestorn.png").convert()
black = pg.image.load("./picture/blackstorn.png").convert()
whitewin = pg.image.load("./picture/whitewin.png").convert()
blackwin = pg.image.load("./picture/blackwin.png").convert()

#初始化工作
pg.display.set_caption("五子棋")

screen.blit(begin,(0,0))
pg.display.update()
i=1
while i == 1:
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            i=0
            break
screen.blit(chesssquare,(0,0))
pg.display.update()

initChesslist = []
initx,inity = 28,17
initChesslist.append(initchesssquare(initx,inity))

#游戏界面，实现交互功能
epoch = 1 #表示下棋的对象，1为白棋，2为黑棋
result = False #表示结果
while True:
    #事件处理
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            x,y = pg.mouse.get_pos()
            for temp in initChesslist:
                for point in temp:
                    if x>=point.x-10 and x<=point.x+10 and y>=point.y-10 and y<=point.y+10:
                        if epoch == 1 and point.state == 0:
                            point.state = epoch
                            result = judgeresult(int((point.x-initx)/40) , int((point.y-inity)/40) , point.state)
                            epoch = 2
                            screen.blit(white,(point.x-5,point.y-5))
                        elif epoch == 2 and point.state == 0:
                            point.state = epoch
                            result = judgeresult(int((point.x-initx)/40) , int((point.y-inity)/40) , point.state)
                            epoch = 1
                            screen.blit(black,(point.x-5,point.y-5))
                    pg.display.update()
    #游戏结果判断
    if result == True:
        if epoch == 2:
            screen.blit(whitewin,(0,0))
        elif epoch == 1:
            screen.blit(blackwin,(0,0))
        pg.display.update()
        time.sleep(4)

        #显示胜利后清空界面开始新一轮循环
        screen.blit(begin,(0,0))
        pg.display.update()
        while result:
            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    result = False
                    break
        screen.blit(chesssquare,(0,0))
        pg.display.update()
        initChesslist = []
        initx,inity = 28,17
        initChesslist.append(initchesssquare(initx,inity))