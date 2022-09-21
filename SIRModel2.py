import math
import matplotlib.pyplot as plt

YS = 400000
OS = 400000
N = YS + OS
S = N
OI = 1
YI = 1
II = OI + YI
I = II
R = 0
taxis=[ ]
xaxis=[ ]
yaxis=[ ]
baxis=[ ]
caxis=[ ]
zaxis=[ ]
YBeta= 0.0000015
YGamma=0.8
OBeta = 0.000001
OGamma = 0.125
t = 0
while t<=100:
  taxis.append(t)
  xaxis.append(S)
  baxis.append(YI)
  caxis.append(OI)
  yaxis.append(I)
  zaxis.append(R)
  NYI = (YS*OI*OBeta) + (YS*YI*YBeta) - (YGamma*YI)
  NOI = (OS*OI*OBeta) + (OS*YI*YBeta)- (OGamma*OI)
  YI += NYI
  OI += NOI
  YS -= YS*OI*OBeta + YS*YI*YBeta
  OS -= OS*OI*OBeta + OS*YI*YBeta
  S = YS + OS
  I = YI + OI
  R = N - S - I + II
  t += 1
plt.title("SIR MODEL")
plt.plot(taxis,xaxis, color=(0,0,1), linewidth=1.0, label='S')
plt.plot(taxis,yaxis, color=(1,0,0), linewidth=1.0, label='I')
plt.plot(taxis,baxis, color=(1,1,0), linewidth=1.0, label='YI')
plt.plot(taxis,caxis, color=(1,0,1), linewidth=1.0, label='OI')
plt.plot(taxis,zaxis, color=(0,1,0), linewidth=1.0, label='R')
plt.xlim(0,100)
plt.ylim(0,N)
plt.legend()

plt.xlabel("TIME STEPS")
plt.ylabel("POPULATION")
plt.grid(True)
plt.show()
