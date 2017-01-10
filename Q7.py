#Assignment: The Millikan Experiment: Gareth Sykes

try:
    import matplotlib.pyplot as plt
except ImportError:
    print("error importing matplotlib(required module), please install matplotlib through pip to run this code")
try:
    import numpy as np
except ImportError:
    print("Error importing Numpy(required module), please install numpy through pip to run this code")


#a)


#Read in values from Millikan experiment

f = open('millikan.txt')

values = f.readlines()

f.close()

#initialize counter (n) and arrays for x & y values

n = 0
x = []
y = []

#populate the arrays x & y with the points from the millikan file

for i in values:
    temp = i.split() #A temporary array to hold a point (x,y)
    x.append(temp[0])
    y.append(temp[1])


plt.plot(x,y, 'ro')
#plt.show()

#b)

#initialize sums and counter (n)

xSum = 0.0
xSumSqr = 0.0
ySum = 0.0
xySum = 0.0
n = 0

#Caclulate Sums

for i in x:
    xSum += float(i)

for i in y:
    ySum += float(i)

for i in x:
    xSumSqr += (float(i))**2

for i in x:
    xySum += (float(x[n])*float(y[n]))
    n += 1

#Calculate E values
    
Ex = (1.0/6) * xSum
Ey = (1.0/6) * ySum
Exx = (1.0/6) * xSumSqr
Exy = (1.0/6) * xySum


#calculate Slope and intercept

m = (Exy - (Ex*Ey))/(Exx - (Ex)**2)

c = ((Exx*Ey) - (Ex*Exy))/(Exx - (Ex)**2)

print "Slope: ", m, " Intercept: ", c

#c)

#initialize x & y + counter (n)

xNew = x
yNew = np.zeros([6])
n = 0

for i in x:
    yNew[n] = m*float(i) + c
    n += 1

plt.plot(x,yNew, 'b')
plt.title('The Millikan Experiment')
plt.xlabel('Frequency of light (Hz)')
plt.ylabel('Volts (V)')
plt.savefig('figure.png')

#d)

# V = (h/e)v - phi --> m = h/e & h = m*e AND int = -Phi

e = 1.602e-19 #units are Coluombs

h = m * e #Calculated plank constant

print "Calculated h: ", h, " Actual h: 6.62607004e-34"
