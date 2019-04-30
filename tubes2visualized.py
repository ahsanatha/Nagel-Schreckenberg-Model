import numpy as np
import random as r
import turtle as tu

M = 1000       #panjang lintasan
p = 0.3         #probabilitas
v0 = 0          #kecepatan awal
N = 10         #banyak kendaraan
tmax = 500     #waktu maksimum
vmax = M/N     #kecepatan maksimum
dt = 1          #step waktu
colors = ['red','yellow','blue','grey','green','aqua','purple',
          'navy','maroon','violet']

def getJarak(i):
    if(i != N-1):
        jarak = abs(turtles[i+1].xcor() - turtles[i].xcor())
        if turtles[i].xcor() <= turtles[i+1].xcor(): #kalau mobil ke i dibelakang mobil i+1
            return jarak
        else:
            return M - (jarak) #mobil i+1 dibelakang mobil i
    else :
        jarak = abs(turtles[0].xcor() - turtles[i].xcor())
        if turtles[i].xcor() <= turtles[0].xcor(): #mobil terakhir dibelakang mobil ke 0
            return jarak
        else:
            return M - (jarak) #mobil ke 0 dibelakang mobil terakhir
        
def move(i):
    velK[i] = min(velK[i]+1,vmax)
    velK[i] = min(velK[i], getJarak(i)-1)
    #c = np.random.choice(range(2),1,[1-p,p])
    c = np.random.uniform(0,2)
    if(c > p):
        velK[i] = max(0, velK[i]-1)
    turtles[i].forward(velK[i])

def updatePosisi():
    jum = 0#2
    for i in range(N):
        b4 = turtles[i].xcor()#3
        move(i)
        posK[i] = turtles[i].xcor()
        if (turtles[i].xcor() > M/2):
            turtles[i].hideturtle()
            turtles[i].goto(turtles[i].xcor()-M,0)
            turtles[i].showturtle()
        if (( (800-(M/2)) <= turtles[i].xcor() <= (900-(M/2)) )):#2
            jum += 1
        if(b4 <= posAK[i] <= posK[i]):#3
            lewat[i] += 1
    return jum
            
screen = tu.Screen()
screen.setup(M,M/2)
screen.bgcolor('light grey')
screen.delay(0)
turtles = []
for i in range(N):
    turtles.append(tu.Turtle())
    
posK = list(r.sample(range(-int(M/2),int(M/2)), N)) #posisi kendaraan
posK.sort()
posAK = posK[:]
#print(posK)
velK = [v0]*N
t = 0
kep = []
lewat = [0]*N

for i in range(N):
    turtles[i].penup()
    turtles[i].setposition(posK[i], 0)
    turtles[i].color(colors[i])
    turtles[i].speed('slow')
    turtles[i].turtlesize(2,2,0)
    #turtles[i].shape('arrow')

while(t <= tmax):
    print(velK)
    k = updatePosisi()
    kep.append(k)
    #print(k)
    t += dt

print('done')
print('kepadatan di 800-900',kep)
print('rata rata kepadatan di 800-900',sum(kep)/len(kep))
print('lewat = ',lewat)
