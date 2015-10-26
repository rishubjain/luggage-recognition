import time
import math

f=open('luggage.ppm').read().split()
g=list(map(int,(f[4:])))
col=int(f[1])
row=int(f[2])

w=open('kmeans.ppm', 'w')

ar=[]
w.write('P3\n')
w.write(str(col) + ' ')
w.write(str(row) + '\n')
w.write(f[3] + '\n')

k=10
kmeans = []
for j in range(k):
    kmeans.append([j*255/(k-1), j*255/(k-1), j*255/(k-1)])

startt = time.time()

grid = [[]]

for i in range(30):
    numchange = 0
    sumk = [[0 for x in range(3)] for x in range(k)] 
    numk = [0 for x in range(k)]
    for q in range(3):
        print('kmeans: ' + str(kmeans[q][0]) + ' ' + str(kmeans[q][1]) + ' ' + str(kmeans[q][2]))
    for y in range(row):
        grid.append([])
        for x in range(col):
            rgb = [g[(y*col+x)*3],g[(y*col+x)*3+1],g[(y*col+x)*3+2]]
            mindist = 200000
            mink = -1
            for j in range(k):
                dist = math.pow((rgb[0]-kmeans[j][0]),2) + math.pow((rgb[1]-kmeans[j][1]),2) + math.pow((rgb[2]-kmeans[j][2]),2)
                if dist<mindist:
                    mindist = dist
                    mink = j
            numk[mink]+=1
            sumk[mink][0] += rgb[0]
            sumk[mink][1] += rgb[1]
            sumk[mink][2] += rgb[2]
            if i!=0:
                if mink!=grid[y][x]:
                    numchange+=1
            grid[y].append(mink)
    print(numk[0])
    print(numk[1])
    for j in range(k):
        kmeans[j] = [sumk[j][0]/numk[j], sumk[j][1]/numk[j], sumk[j][2]/numk[j]]
    print('i: ' + str(i) + ' numchange: ' + str(numchange))
            
for y in range(row):
    for x in range(col):
        w.write(str(kmeans[grid[y][x]][0]) + ' ')
        w.write(str(kmeans[grid[y][x]][1]) + ' ')
        w.write(str(kmeans[grid[y][x]][2]) + '\n')


fint = time.time()

print('rows, col: ' + str(row) + ' ' + str(col))
print('time: ' + str(fint-startt))
