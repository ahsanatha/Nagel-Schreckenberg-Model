import numpy as np
import random as r

M = 100 #panjang lintasan
p = 0.3 #probabilitas
v0 = 0 #kecepatan awal
N = 10 #banyak kendaraan
tmax = 100 #waktu maksimum
vmax = 5 #kecepatan maksimum
dt = 1 #step waktu

def getJarak(i):
    if(i < N-1):
        jarak = abs(posK[i+1] - posK[i])
        #print(i,' ',jarak)
        if posK[i] <= posK[i+1]:
            return jarak
        elif posK[i] > posK[i+1]:
            return M - (jarak)
    else :
        jarak = abs(posK[0] - posK[i])
        if posK[0] <= posK[i]:
            return jarak
        elif posK[0] > posK[i]:
            return M - (jarak)
        
def updateV(i):
    velK[i] = min(velK[i]+1,vmax)
    velK[i] = min(velK[i], getJarak(i)-1)
    c = np.random.choice(range(2),1,[p,1-p])
    if(c[0] == 1):
        velK[i] = max(0, velK[i]-1)
        
def updatePosisi(posK):
    for i in range(N):
        updateV(i)
        posK[i] = posK[i] + velK[i]
        if(posK[i] >= M):
            posK[i] = posK[i] - M
            
posK = list(r.sample(range(M), N)) #posisi kendaraan
velK = [vmax]*N
t = 0
while(t <= tmax):
    print(posK)
    updatePosisi(posK)
    t += dt

