import cv2
import numpy as np
from Functions import crop , bgr2bw

rec = cv2.VideoCapture(r'C:/Users/Admin/Desktop/6.mp4')  # Open the video file

while True:
    ret, frame = rec.read()  # Read a frame from the video

    if not ret:  # Break the loop if the video ends
        break

    # Convert the cropped region to black and white
    bw_img = bgr2bw(frame, 245)

    # Apply edge detection using the Canny edge detector
    edges = cv2.Canny(bw_img, 240, 250)

    # Find contours based on the detected edges
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw the contours on the original cropped frame
    cv2.drawContours(frame, contours, -1, (0, 255, 0), 2)

    # Display the result
    cv2.imshow('Detected Contours', frame)

    if cv2.waitKey(100) == ord('c'):  # Break the loop when 'c' is pressed
        break

# Release the video capture object and close all windows
rec.release()
cv2.destroyAllWindows()
