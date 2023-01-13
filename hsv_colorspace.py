import cv2 
import numpy as np
import matplotlib.pyplot as plt

#グラフを大きめに表示する
fig, ax = plt.subplots(figsize=(10,5))

img_hsv = np.zeros((180,256,3),np.uint8)

for y, h in enumerate(range(0,180)):
  for x, s in enumerate(range(0,256)):
    img_hsv[y,x,:] = (h,s,255)
    
img_rgb = cv2.cvtColor(img_hsv,cv2.COLOR_HSV2RGB)

ax.set_title("HSV Color")


plt.imshow(img_rgb)
plt.show()
