import cv2 
import numpy as np
import matplotlib.pyplot as plt

img_bgr = cv2.imread("fish.jpg")
img_hsv = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2HSV)

h, s, v = cv2.split(img_hsv)

plt.figure(figsize=(10,7))

mask = s

mask[((h > 80) & (h < 140)& (s > 70))] = 255
mask_3ch = cv2.cvtColor(mask,cv2.COLOR_GRAY2BGR)

result_img = cv2.bitwise_and(img_bgr,mask_3ch)

cv2.imshow("result_img",result_img)

plt.subplot(2,3,1)
plt.title("Original (RGB)")
plt.imshow(cv2.cvtColor(img_bgr,cv2.COLOR_BGR2RGB))


plt.subplot(2,3,2)
plt.title("Hue (H)")
plt.imshow(cv2.cvtColor(h,cv2.COLOR_BGR2RGB))


plt.subplot(2,3,3)
plt.title("Saturation (S)")
plt.imshow(cv2.cvtColor(s,cv2.COLOR_BGR2RGB))


plt.subplot(2,3,4)
plt.title("Volume (V)")
plt.imshow(cv2.cvtColor(v,cv2.COLOR_BGR2RGB))


plt.subplot(2,3,5)
plt.title("Volume (V)")
plt.imshow(cv2.cvtColor(img_bgr,cv2.COLOR_BGR2RGB))


plt.subplot(2,3,6)
plt.title("Volume (V)")
plt.imshow(cv2.cvtColor(img_bgr,cv2.COLOR_BGR2RGB))

plt.show()
