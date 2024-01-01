import cv2
import os
from picamera2 import Picamera2

FACE_DETECTOR = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam = Picamera2()

cam.preview_configuration.main.size = (640, 360)
cam.preview_configuration.main.format = "RGB888"
cam.preview_configuration.controls.FrameRate = 30
cam.preview_configuration.align()
cam.configure("preview")
cam.start()

ID = input('\n Enter unique numeric ID and press RETURN ')
print("\n Look at the camera and press Q when you want to snap a picture (take around 15)")

count = 0

while True:
    frame = cam.capture_array()
    frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = FACE_DETECTOR.detectMultiScale( 
            frameGray,      
            scaleFactor=1.1,
            minNeighbors=5, 
            minSize=(30, 30)
    )
    
    for (xpos, ypos, width, height) in faces:
        cv2.rectangle(frame, (xpos, ypos), (xpos + width, ypos + height), (0, 0, 255), 3)
        cv2.imshow('FaceCapture', frame)

    key = cv2.waitKey(100) & 0xff
    if key == 113:  # q key
        count += 1 
        if not os.path.exists("dataset"):
            os.makedirs("dataset")
        file_path = os.path.join("dataset", f"User.{ID}.{count}.jpg")
        cv2.imwrite(file_path, frameGray[ypos:ypos + height, xpos:xpos + width])
        print(f"Image saved: {file_path}")

    elif key == 13:  # RETURN key
        print("\n Exiting Photo Capture")
        cam.stop()
        cv2.destroyAllWindows()
        exit()
