import cv2

img = cv2.imread("dog.jpg",cv2.IMREAD_ANYCOLOR)

img_roi = img[135:320,150:290]

cv2.imshow("img",img)
cv2.imshow("img_roi",img_roi)
cv2.waitKey(0)
cv2.destroyAllWindows()

