import cv2

img = cv2.imread("dog.jpg",cv2.IMREAD_COLOR)

b_plane, g_plane, r_plane = cv2.split(img)

merge_bg = cv2.merge((b_plane,g_plane,r_plane))

cv2.imshow("img",img)
cv2.imshow("b_plane",b_plane)
cv2.imshow("g_plane",g_plane)
cv2.imshow("r_plane",r_plane)
cv2.imshow("merge_bg",merge_bg)

cv2.waitKey(0)
cv2.destroyAllWindows()


