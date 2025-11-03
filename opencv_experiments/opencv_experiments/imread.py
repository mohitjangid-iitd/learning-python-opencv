import cv2
from scipy import ndimage

img = cv2.imread(r"C:/Users/Admin/Desktop/nit f.jpg")

img_1 = cv2.resize(img, (600, 600))
img_2 = cv2.resize(img, (0,0), fx=.75,fy=.75)
img_3 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
img_4 = cv2.rotate(img, cv2.ROTATE_180)
img_5 = ndimage.rotate(img, 90)

cv2.imshow("image", img)
cv2.imshow("image 1", img_1)
cv2.imshow("image 2", img_2)
cv2.imshow("image 3", img_3)
cv2.imshow("image 4", img_4)
cv2.imshow("image 5", img_5)

k=cv2.waitKey(0)

if k == ord('d'):
    cv2.destroyAllWindows()