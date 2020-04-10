import math
import random
import turtle
from turtle_run import * #引入我們自訂的 config.py

# 設定畫布大小為 500 x 500
win_length = 500
win_height = 500

#設定有八隻烏龜
turtles = 8

#創建新畫布
turtle.screensize(win_length, win_height)

#宣告config class
config = Config()

# 宣告比賽烏龜的型別，有位置、顏色、形狀、名稱等等的參數
class racer(object):
    def __init__(self, color, pos, name):
        self.pos = pos
        self.color = color
        self.turt = turtle.Turtle()
        self.turt.shape('turtle')
        self.turt.color(color)
        self.turt.penup()
        self.turt.setpos(pos)
        self.turt.setheading(90)
        self.name = name
        
    #定義賽龜的運動行為，透過 pos + r 來前進
    def move(self):
        r = random.randrange(1, 30)
        self.pos = (self.pos[0], self.pos[1] + r)
        self.turt.pendown()
        self.turt.forward(r)
        
    #讓賽龜們回到初始位置
    def reset(self):
        self.turt.penup()
        self.turt.setpos(self.pos)


def startGame():
    tList = []
    turtle.clearscreen() #清空畫布
    turtle.hideturtle() 
    data = config.load() #讀取設定的資料

    #將賽龜資料處理並加入 tList[] 中
    start = -(win_length/2) + 20
    for t in range(turtles):
        newPosX = start + t*(win_length)//turtles
        tList.append(racer(data[t]["color"],(newPosX, -230), data[t]["name"]))
        tList[t].turt.showturtle()

    #開始比賽
    run = True
    while run:
        for t in tList:
            t.move()

        maxColor = []
        maxDis = 0
        for t in tList:
            if t.pos[1] > 230 and t.pos[1] > maxDis:
                maxDis = t.pos[1]
                maxColor = []
                maxColor.append(t.name)
            elif t.pos[1] > 230 and t.pos[1] == maxDis:
                maxDis = t.pos[1]
                maxColor.append(t.name)

        #比賽結束後將第一名的以 console 方式輸出
        ShowWinText = ""
        if len(maxColor) > 0:
            run = False
            print('The winner is: ')
            for win in maxColor:
                print(win) 
                ShowWinText= win

    #再宣告一隻烏龜用來顯示結果
    pen = turtle.Turtle()
    pen.penup()
    pen.goto(0,-270)
    
    #到畫布下方寫下第一名的烏龜名稱
    pen.write(ShowWinText,False,"center",('Arial', 16, 'normal'))
    pen.showturtle()

startGame()

while True:
    print('-----------------------------------')
    start = input('Would you like to play again')
    startGame()