import numpy as np
import matplotlib.pyplot as plt
import math
import random

points = np.linspace(0,4*math.pi, 100)
sinOne = np.sin(points)
sinTwo = np.sin(5*points+math.pi/2)*0.2
noise = np.zeros((100))
for i in range(len(noise)):
  noise[i]+=(random.random()-0.5)/3

print(noise)

def fft(points, wave):
  coefList = list()
  phaseList = list()
  print("Performing fft")
  for f in range(len(points)):
    # me^ik = m( cos(k)+isin(k) )
    # k = 2 pi f t
    fc = 0
    fci = 0
    for t in range(len(points)):
      fc+=wave[t]*math.cos(2*math.pi*f*points[t]/points[-1])/len(points)
      fci+=wave[t]*math.sin(2*math.pi*f*points[t]/points[-1])/len(points)
    coefList.append(fc)
    phaseList.append(fci)
  coefList = np.array(coefList)
  phaseList = np.array(phaseList)
  for i in range(len(coefList)):
    coefList[i] = math.pow(math.pow(coefList[i],2)+math.pow(phaseList[i],2),0.5)
  plt.plot(coefList)
  plt.plot(wave)
  plt.show()


fft(points, sinOne+sinTwo+noise)


