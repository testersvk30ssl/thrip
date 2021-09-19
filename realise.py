from tkinter import Tk, Canvas
import time,datetime
from math import *
from random import *

t = datetime.datetime.now()

p = [0,0,0]             #Начальные точки
width = 700             #Ширина квадрата-полотна
cunt =1000              #кол-во точек в круге
evry = 3                #Чертить каждую {evry} точку на круге
speed = (3,2,1)         #Скорость движения различных точек (точка/такт)
delay = 0.02            #Задержка между тактами в секундах
arrowcolor = 'red'      #Цвет линий
circlecolor = 'black'   #Цвет круга
onintreecolor = 'blue'  #Цвет линий, когда центр в триугольнике

def circle(radius):
    dot = list()
    for i in range(0,cunt):
        x=cos(i/cunt*2*pi)*radius
        y=sin(i/cunt*2*pi)*radius
        dot.append((round(rad+x),round(rad+y)))
    return dot

def randot(p):
    rand = list()
    l = len(dots)
    for f in range(len(p)):
        rand=speed[f]
        tmp = p[f]
        p[f] = add(l,tmp,rand)[0]
        
    return (p)

def add(lenght,value,key):
    if(key+value>lenght):
        return ((key+value)%lenght,(key+value)//lenght)
    elif(key+value<0):
        return (key-value+lenght,0)
    else: return (key+value,0)

def intri(p,o)->bool:
    a = (p[0][0] - o[0]) * (p[1][1] - p[0][1]) - (p[1][0] - p[0][0]) * (p[0][1] - o[1])
    b = (p[1][0] - o[0]) * (p[2][1] - p[1][1]) - (p[2][0] - p[1][0]) * (p[1][1] - o[1])
    c = (p[2][0] - o[0]) * (p[0][1] - p[2][1]) - (p[0][0] - p[2][0]) * (p[2][1] - o[1])
    d=((a>=0)==(b>=0)==(c>=0))
    return d

def point(xy,color=circlecolor,width=1,tag=1,ofset=0):
    d = width/2
    return c.create_oval(
            xy[0]-d, xy[1]-d, xy[0]+d, xy[1]+d, outline=color,
            fill=color, width=1)

def line(xy,x1y1,color=circlecolor,width=7,tag=1,ofset=0):
    return c.create_line(ofset+xy[0],ofset+xy[1],ofset+x1y1[0],ofset+x1y1[1],fill=color,width=width,tag=tag)
def tri(p):
    pin.clear()
    lin.clear()
    for i in range(len(p)):
        d = dots[p[i]-1]
        dp.append((d[0],d[1]))
        d1 = i
        d2 = add(len(dp),i,-1)[0]
        lin.append(line(dp[d1],dp[d2],color,ofset=0,tag=1))
    lin.append(line(dp[0],dp[2],color,ofset=0,tag=1))
    dp.clear()





rad =int(width/2)
dots = list()
tmp = circle(rad)
l=len(tmp)
oth = l/4
i = -oth
while(i<0):
    a = add(l,0,round(i))
    dots.append(tmp[a[0]])
    i+=1
while(i<l-oth):
    dots.append(tmp[add(l,0,round(i))[0]])
    i+=1
t = round(len(dots)/3)
pin = list()
lin=list()
dp = list()
root = Tk()
c = Canvas(root, width=width, height=width)
c.pack()
for d in range(len(dots)):
    if(d%evry==0):
        point((dots[d][0],dots[d][1]),width=5)
point((rad,rad),width=10)
f=0
s = 0
for t in range(0):
    p = randot(p)
    ds = (dots[p[0]-1],dots[p[1]-1],dots[p[2]-1])
    if(intri(ds,(rad,rad))):
        s+=1
    f+=1

while(True):
    p = randot(p)
    ds = (dots[p[0]-1],dots[p[1]-1],dots[p[2]-1])
    
    if(intri(ds,(rad,rad))):
        color = onintreecolor
    else: color = arrowcolor
    tri(p)
    c.update()
    time.sleep(delay)
    c.delete(lin[3])
    c.delete(lin[1])
    c.delete(lin[2])
    


