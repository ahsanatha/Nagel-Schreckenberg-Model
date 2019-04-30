import numpy as np
import random as r
import turtle as tu

M = 1000       #panjang lintasan
p = 0.1        #probabilitas
v0 = 0          #kecepatan awal
N = 10         #banyak kendaraan
tmax = 1000     #waktu maksimum
vmax = M/N     #kecepatan maksimum
dt = 1          #step waktu
colors = ['red','yellow','blue','grey','green','aqua','purple',
          'navy','maroon','violet']

def getDepan(i):
    for j in range(N):
        if (posK[i][1] == posK[j][1]) and (posK[i][0] < posK[j][0]):
            return j
        if j == (N-1):
            return 0

def getJarak(i,idepan):
    if(i != N-1):
        jarak = abs(turtles[idepan].xcor() - turtles[i].xcor())
        if turtles[i].xcor() <= turtles[idepan].xcor(): #kalau mobil ke i dibelakang mobil i+1
            return jarak
        else:
            return M - (jarak) #mobil i+1 dibelakang mobil i
    else :
        jarak = abs(turtles[idepan].xcor() - turtles[i].xcor())
        if turtles[i].xcor() <= turtles[idepan].xcor(): #mobil terakhir dibelakang mobil ke 0
            return jarak
        else:
            return M - (jarak) #mobil ke 0 dibelakang mobil terakhir
def move(i,idepan):
    velK[i] = min(velK[i]+1,vmax)
    velK[i] = min(velK[i], getJarak(i,idepan)-1)
    c = np.random.uniform(0,1)
    print(c)
    if(c >= p):
        velK[i] = max(0, velK[i]-1)
    turtles[i].forward(velK[i])

def updatePosisi():
    for i in range(N):
        dep = getDepan(i)
        #print(dep)
        move(i,dep)
        posK[i][0] = turtles[i].xcor()
        if (turtles[i].xcor() > M/2):
            turtles[i].hideturtle()
            turtles[i].goto(turtles[i].xcor()-M,posK[i][1])
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
for i in range(N):
    posK[i] = [posK[i],(np.random.randint(0,2)*30)]
posAK = posK[:]
print(posK)
velK = [v0]*N
t = 0
kep = []
lewat = [0]*N

for i in range(N):
    turtles[i].penup()
    turtles[i].setposition(posK[i][0],posK[i][1])
    turtles[i].color(colors[i])
    turtles[i].speed(0)
    turtles[i].turtlesize(2,2,0)

while(t <= tmax):
    print(velK)
    updatePosisi()
    #kep.append(k)
    #print(k)
    t += dt

#print('done')
#print('kepadatan di 800-900',kep)
#print('rata rata kepadatan di 800-900',sum(kep)/len(kep))
#print('lewat = ',lewat)
