import numpy as np
import random as r
import turtle as tu

M = 1000        #panjang lintasan
p = 0.3         #probabilitas
v0 = 0          #kecepatan awal
N = 10          #banyak kendaraan
tmax = 1000     #waktu maksimum
vmax = M/N      #kecepatan maksimum
dt = 1          #step waktu
colors = ['red','yellow','blue','grey','green','brown','purple',
          'navy','maroon','violet']

def getJarak(i):
    if(i < N-1):
        jarak = abs(turtles[i+1].xcor() - turtles[i].xcor())
        if turtles[i].xcor() <= turtles[i+1].xcor():
            return jarak
        else:
            return M - (jarak)
    else :
        jarak = abs(turtles[0].xcor() - turtles[i].xcor())
        if turtles[0].xcor() <= turtles[i].xcor():
            return jarak
        else:
            return M - (jarak)
        
def move(i):
    velK[i] = min(velK[i]+1,vmax)
    velK[i] = min(velK[i], getJarak(i)-4)
    c = np.random.choice(range(2),1,[1-p,p])
    if(c[0] == 1):
        velK[i] = max(0, velK[i]-1)
    turtles[i].forward(velK[i])

def updatePosisi():
    for i in range(N):
        move(i)
        posK[i] = turtles[i].pos()[0]
        if (turtles[i].xcor() > M/2):
            turtles[i].hideturtle()
            turtles[i].goto(turtles[i].position()[0]-M,0)
            turtles[i].showturtle()
            
screen = tu.Screen()
screen.setup(M,M/2)
screen.bgcolor('light grey')
screen.delay(0)
turtles = []
for i in range(N):
    turtles.append(tu.Turtle())
    
posK = list(r.sample(range(-int(M/2),int(M/2)), N)) #posisi kendaraan
posK.sort()
print(posK)
velK = [v0]*N
t = 0

for i in range(N):
    turtles[i].penup()
    turtles[i].setposition(posK[i], 0)
    turtles[i].color(colors[i])
    turtles[i].speed(1)
    turtles[i].turtlesize(2,2,0)

while(t <= tmax):
    print(velK)
    updatePosisi()
    t += dt
print('done')
