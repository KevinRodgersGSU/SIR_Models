import math
import matplotlib.pyplot as plt
N = 750000
y = 1
x = N
z = 0
taxis=[ ]
xaxis=[ ]
yaxis=[ ]
zaxis=[ ]
beta=0.000001
gamma=0.25
t = 0
while t<=100:
  taxis.append(t)
  xaxis.append(x)
  yaxis.append(y)
  zaxis.append(z)
  kx1 = - beta*x*y
  ky1 = beta*x*y - gamma*y
  x += kx1
  y += ky1
  z = N - x - y + 1
  t += 1
plt.title("SIR MODEL")
plt.plot(taxis,xaxis, color=(0,0,1), linewidth=1.0, label='S')
plt.plot(taxis,yaxis, color=(1,0,0), linewidth=1.0, label='I')
plt.plot(taxis,zaxis, color=(0,1,0), linewidth=1.0, label='R')
plt.xlim(0,100)
plt.ylim(0,N)
plt.legend()

plt.xlabel("TIME STEPS")
plt.ylabel("POPULATION")
plt.grid(True)
plt.show()
