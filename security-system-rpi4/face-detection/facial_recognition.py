import cv2
import os
import numpy as np
from picamera2 import Picamera2
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)  # relay
GPIO.setup(11, GPIO.IN)  # PIR sensor

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')

cam = Picamera2()
cam.preview_configuration.main.size = (640, 360)
cam.preview_configuration.main.format = "RGB888"
cam.preview_configuration.controls.FrameRate = 30
cam.preview_configuration.align()
cam.configure("preview")
cam.start()

print("Starting Program")
while True:
    pir_status = GPIO.input(11)

    if pir_status == GPIO.HIGH:
        frame = cam.capture_array()
        frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(
            frameGray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(150, 150)
        )
        for (xpos, ypos, width, height) in faces:
            id, confidence = recognizer.predict(frameGray[ypos:ypos + height, xpos:xpos + width])
            if confidence < 77:
                GPIO.output(18, GPIO.HIGH)
                sleep(10)
                GPIO.output(18, GPIO.LOW)
            else:
                id = "unknown"
                confidence = f"{100 - confidence:.0f}%"
                cv2.imwrite(f"../webui/static/photos/{id}_{confidence}.jpg", frame[ypos:ypos + height, xpos:xpos + width])


    key = cv2.waitKey(100) & 0xff
    if key == 27:  # ESCAPE key
        break
    elif key == 113:  # q key
        break

print("\nExiting Program")
cam.stop()
cv2.destroyAllWindows()


