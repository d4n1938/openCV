import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.cvtColor(cv2.imread("fish.jpg"),cv2.COLOR_BGR2GRAY)
# cv2.imshow("original",img)

block_size = 15
c = 25

blur_img = cv2.GaussianBlur(img,(block_size,block_size),0)
# cv2.imshow("blur",blur_img)

diff_img = blur_img - img 

result_img = np.where(blur_img - c > img ,0 ,255)

cv2.imshow("result",result_img.astype(np.uint8))

cv2.waitKey(0)
