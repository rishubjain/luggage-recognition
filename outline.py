import time

f=open('luggage.ppm').read().split()
g=list(map(int,(f[4:])))
col=int(f[1])
row=int(f[2])

w=open('luggageo.ppm', 'w')

ar=[]
w.write('P3\n')
w.write(str(col) + ' ')
w.write(str(row) + '\n')
w.write(f[3] + '\n')

startt = time.time()

for x in range(col*row):
	gr = int(.30*g[x*3] + .59*g[x*3+1] + .11*g[x*3+2])
	#print(gr, gr, gr)
	ar.append(gr)
	
minx=1000000
miny=1000000
maxx=0
maxy=0

midt = time.time()

for y in range(row):
	for x in range(col):
		if x==col-1 or x==0 or y==row-1 or y==0:
			gr = ar[y*col + x]
			w.write(str(gr) + ' ')
			w.write(str(gr) + ' ')
			w.write(str(gr) + '\n')
		else:
			m =[-1, 0, 1, -2, 0, 2, -1, 0, 1]
			my=[1, 2, 1, 0, 0, 0, -1, -2, -1]
			
			gx = m[0]*ar[(y-1)*col +(x-1)] + m[2]*ar[(y-1)*col +(x+1)] + m[6]*ar[(y+1)*col +(x-1)] + m[8]*ar[(y+1)*col +(x+1)] + m[3]*ar[(y)*col +(x-1)] + m[1]*ar[(y-1)*col +(x)] + m[5]*ar[(y)*col +(x+1)] + m[7]*ar[(y+1)*col +(x)] + m[4]*ar[(y)*col +(x)]
			
			gy = my[0]*ar[(y-1)*col +(x-1)] + my[2]*ar[(y-1)*col +(x+1)] + my[6]*ar[(y+1)*col +(x-1)] + my[8]*ar[(y+1)*col +(x+1)] + my[3]*ar[(y)*col +(x-1)] + my[1]*ar[(y-1)*col +(x)] + my[5]*ar[(y)*col +(x+1)] + my[7]*ar[(y+1)*col +(x)] + my[4]*ar[(y)*col +(x)]

			gr = abs(gx) + abs(gy)
			if gr<125 and not (x==77 or x==324 or y==15 or y==379):
				w.write('255 255 255\n')
			else:
				if x<minx:
				   minx = x
				if y<miny:
				   miny = y
				if y>maxy:
				   maxy = y
				if x>maxx:
				   maxx = x
				w.write('0 0 0\n')
			#	w.write(str(gr) + ' ')
			#	w.write(str(gr) + ' ')
			#	w.write(str(gr) + '\n')
#print(minx)
#print(miny)
#print(maxx)
#print(maxy)
fint = time.time()
minx=77
maxx=324
miny=15
maxy=379
print('R: ' + str(g[3 * ((col * (miny + maxy)/2) + (minx + maxx)/2)]))
print('G: ' + str(g[3 * ((col * (miny + maxy)/2) + (minx + maxx)/2) + 1]))
print('B: ' + str(g[3 * ((col * (miny + maxy)/2) + (minx + maxx)/2) + 2]))
print('\nwidth: ' + str(maxx-minx))
print('hight: ' + str(maxy-miny))
print('rows, col: ' + str(row) + ' ' + str(col))
print('time1: ' + str(midt-startt))
print('time2: ' + str(fint-midt))
