import numpy as np
import random as r
import numpy

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
        else:
            return M - (jarak)
    else :
        jarak = abs(posK[0] - posK[i])
        if posK[i] <= posK[0]:
            return jarak
        else:
            return M - (jarak)
        
def updateV(i):
    velK[i] = min(velK[i]+1,vmax)
    velK[i] = min(velK[i], getJarak(i)-1)
    c = np.random.uniform(0,1)
    #print(c)
    if(c > p):
        #print(c)
        velK[i] = max(0, velK[i]-1)
        
def updatePosisi(posK):
    jum = 0
    for i in range(N):
        b4 = posK[i]-1
        updateV(i)
        posK[i] += velK[i]
        if(posK[i] >= M):
            posK[i] = posK[i] - M
        if (( (80-(M/2)) <= posK[i] <= (90-(M/2)) )):
            jum += 1
        if (b4 < posAK[i] == posK[i]):
            timeLewat[i].append(lewat[i])
            #print('hubla',i)
            lewat[i] = 0
        else :
            lewat[i] += 1   
    return jum
            
posK = list(r.sample(range(M), N)) #posisi kendaraan
posK.sort()
posAK = posK[:]
velK = [vmax]*N
t = 0
kep = []
timeLewat = []
lewat = [0]*N

for i in range(N):
    timeLewat.append([])
    
while(t <= tmax):
    print(velK)
    k = updatePosisi(posK)
    kep.append(k)
    t += dt
print('awal = ',posAK)
#print('kepadatan di 80-90 = ',kep)
#print('rata rata kepadatan dikepadatan di 80-90 =',sum(kep)/len(kep))
#print('lewat = ',lewat)
#print('time lewat : ',timeLewat)
#for i in range(len(timeLewat)):
    #print('waktu rata-rata mobil ',i,' kembali =',sum(timeLewat[i])/len(timeLewat[i]))
