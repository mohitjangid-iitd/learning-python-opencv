import cv2
import random

# BGR
img1 = cv2.imread(r"C:/Users/Admin/Desktop/SS Test.png",1) #import img as it is
img2 = cv2.imread(r"C:/Users/Admin/Desktop/SS Test.png",0) #import img as b&w

print(img1[90][121]) #90th raw and 121th colamb
print(type(img1))    #image is a numpy array
print(img1.shape,'\n',img2.shape) #(H,W,C)

# cv2.imshow("image1", img1)
# cv2.imshow("image2", img2)

for i in range(50):
    for j in range(img1.shape[1]):
        img1[i][j] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
# random.randrange(255)
cv2.imshow("image1", img1)
img2[30:90,90:200]=img2[90:150,200:310] #replacing entries [30-90:90-120] by [90-150,200-310]
cv2.imshow("image2", img2)

if cv2.waitKey(0) == ord('d'):
    cv2.destroyAllWindows()