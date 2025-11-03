import cv2
import numpy as np

rec = cv2.VideoCapture(0) #start rec. via camera 0

while True:
    ret, frame = rec.read()
    
    width = int(rec.get(3)) #from 17 infos of capture we are reading no. 3 as width 
    height = int(rec.get(4)) #and no. 4 as height
    
    image = np.zeros(frame.shape, np.uint8) #creating an empty numpy array of the shape of frame
    
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5) #squasing the size of frame
    
    image[ :height//2, :width//2] = smaller_frame  #Top left
    image[height//2:, :width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_180)   #bottom left
    image[ :height//2, width//2:] = smaller_frame  #Top right
    image[height//2:, width//2:] = smaller_frame   #bottom right
    
    cv2.imshow( 'frame', image)
    
    # cv2.imshow('REC',frame)
    if cv2.waitKey(1)== ord('c'): #breaks the loop while press c
        break

rec.release() #camera rec. off
cv2.destroyAllWindows() #close all windows