def PSDArea(df_size):
  Size=28
  qual_img=40
  L = Width[qual_img]
  data=np.array(df_size.drop('Width',axis=1).iloc[qual_img]).reshape(Size,Size)
  img = Image.fromarray(data.astype('uint8'), mode='L')
  img=np.float32(img)
  img28=cv2.resize(img,(Size,Size), interpolation = cv2.INTER_AREA)
  Foto=np.array(img28).reshape(28,28)
  plt.imshow(Foto, cmap = "gray")
  
  for i in range(28):
    for j in range(28):
      if img[i,j] < mean_value:
        img_new[i,j] = 255
      else:
        img_new[i,j] = 0

  img28=cv2.resize(img_new,(Size,Size), interpolation = cv2.INTER_AREA)
  Foto=np.array(img28).reshape(28,28)
  plt.imshow(Foto, cmap = "gray")
  return df_areas

