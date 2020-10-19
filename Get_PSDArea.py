import cv2
import numpy as np
import pandas as pd
from PIL import Image

def PSDArea(df_size):
  Width=np.array(df_size['Width'])
  Size=28
  Nx, Ny = df_size.shape
  
  Area_todas = []
  for qual_img in range(Nx):
    L = Width[qual_img]
    data=np.array(df_size.drop('Width',axis=1).iloc[qual_img]).reshape(Size,Size)
    img = Image.fromarray(data.astype('uint8'), mode='L')
    img=np.float32(img)
    
    mean_value = np.mean(img)
    img_new = img.copy()
    
    img28=cv2.resize(img,(Size,Size), interpolation = cv2.INTER_AREA)
    Foto=np.array(img28).reshape(28,28)
    

    for i in range(28):
      for j in range(28):
        if img[i,j] < mean_value:
          img_new[i,j] = 255
        else:
          img_new[i,j] = 0
          
    #for qual_img in range(Nx):
    Area = np.sum(img_new) / (255.0 * 28 * 28)* L*L
    Area_todas.append(Area)
    
  return Area_todas

