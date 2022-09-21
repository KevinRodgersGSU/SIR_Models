import math
import matplotlib.pyplot as plt

YS = 400000
OS = 400000
N = YS + OS
S = N
OI = 5
YI = 5
II = YI + OI
YL = 0
YLP = .25
OL = 0
OLP = .5
L = OL + YL
I = II
R = 0
taxis=[ ]
xaxis=[ ]
yaxis=[ ]
zaxis=[ ]
baxis=[ ]
YBeta= 0.0000015
YGamma=0.4
OBeta = 0.000001
OGamma = 0.125
t = 0
while t<=100:
  taxis.append(t)
  xaxis.append(S)
  baxis.append(L)
  yaxis.append(I)
  zaxis.append(R)
  NYL = (YS*OI*OBeta) + (YS*YI*YBeta) - (YLP*YL)
  NOL = (OS*OI*OBeta) + (OS*YI*YBeta) - (OLP*OL)
  NYI = (YLP*YL)  - (YGamma*YI)
  NOI = (OLP*OL) - (OGamma*OI)
  YL += NYL
  OL += NOL
  YI += NYI
  OI += NOI
  YS -= (YS*OI*OBeta) + (YS*YI*YBeta)
  OS -= (OS*OI*OBeta) + (OS*YI*YBeta)
  S = YS + OS
  I = YI + OI
  L = YL + OL
  R = N - S - I - L + II
  t += 1
plt.title("SEIR MODEL")
plt.plot(taxis,xaxis, color=(0,0,1), linewidth=1.0, label='S')
plt.plot(taxis,baxis, color=(1,0,1), linewidth=1.0, label='E')
plt.plot(taxis,yaxis, color=(1,0,0), linewidth=1.0, label='I')
plt.plot(taxis,zaxis, color=(0,1,0), linewidth=1.0, label='R')
plt.xlim(0,100)
plt.ylim(0,N)
plt.legend()
plt.xlabel("TIME STEPS")
plt.ylabel("POPULATION")
plt.grid(True)
plt.show()
