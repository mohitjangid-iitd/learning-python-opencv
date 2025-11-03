import cv2
import numpy as np

rec = cv2.VideoCapture(r'C:/Users/Admin/Desktop/6221917301201965293.mp4')  # Start video capture

frame_counter = 0  # Counter to keep track of frames

while True:
    ret, frame = rec.read()
    
    width = int(rec.get(3))  # Get the width of the video
    height = int(rec.get(4))  # Get the height of the video
    
    if not ret:
        break
    
    img = frame.copy()  # Make a copy of the frame to use separately
    
    img = cv2.line(img, (0, 0), (width, height), (0, 255, 255), 5)
    img = cv2.rectangle(img, (25, 25), (width - 25, height - 25), (255, 255, 0), 10)
    img = cv2.circle(img, (width // 2, height // 2), 25, (255, 0, 255), -1)  # -1 thickness to fill it entirely
    
    font = cv2.FONT_ITALIC
    
    img = cv2.putText(img, 'cam 0', (35, height - 35), font, 2, (255, 255, 255), 5)  # 2-> font size, 5-> font thickness
    
    # Display the frame with shapes and text
    cv2.imshow('REC1', img)
    
    key = cv2.waitKey(1)
    
    if key == ord('c'):  # Press 'c' to break the loop
        break
    elif key == ord('p'):  # Press 'p' to pause the frame
        while True:
            key2 = cv2.waitKey(0)
            if key2 == ord('p'):  # Press 'p' again to continue
                break
            elif key2 == ord('s'):  # Press 's' to save the paused frame
                frame_name = f"paused_frame_{frame_counter}.jpg"
                cv2.imwrite(frame_name, img)  # Save the frame as a JPEG file
                print(f"Frame saved as {frame_name}")
                frame_counter += 1

rec.release()  # Release the video capture
cv2.destroyAllWindows()  # Close all windows
