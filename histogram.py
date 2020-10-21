import numpy as np

def PSD(diam):
  Size = [1.19,1.00,0.84,0.71,0.59,0.50,0.42,0.35,0.21]
  Malha = [16,18,20,25,30,35,40,45,70]

  Class = np.zeros(9,dtype=int)

  for item in Diam:
    if item > Size[0]:
      Class[0] = Class[0]+1 # bigger 16
    elif item > Size[1]:
      Class[1] = Class[1]+1 # between 16 and  18
    elif item > Size[2]:
      Class[2] = Class[2]+1 # between 18 and  20
    elif item > Size[3]:
      Class[3] = Class[3]+1 # between 20 and  25
    elif item > Size[4]:
      Class[4] = Class[4]+1 # between 25 and  30
    elif item > Size[5]:
      Class[5] = Class[5]+1 # between 30 and  35    
    elif item > Size[6]:
      Class[6] = Class[6]+1 # between 35 and  40
    elif item > Size[7]:
      Class[7] = Class[7]+1 # between 40 and  45
    elif item > Size[8]:
      Class[8] = Class[8]+1 # between 45 and  70
    else:
      Class[9] = Class[9]+1 # bigger  70  
  
  Class = Class[::-1]
  
  return Class
