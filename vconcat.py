import cv2
import numpy as np

img1 = cv2.imread("dog.jpg",cv2.IMREAD_COLOR)
flipImg = cv2.flip(img1,0)

vconcatImg = cv2.vconcat([img1,flipImg])

cv2.imshow('vconcatImg',vconcatImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
