import cv2
import os
import numpy as np

RECOGNIZER = cv2.face.LBPHFaceRecognizer_create()
FACE_DETECTOR = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
PATH = 'dataset'

def getFacesAndID(PATH):
    faces = []
    IDs = []

    for fileName in os.listdir(PATH):
        ID = int(fileName.split(".")[1])
        imagePath = os.path.join(PATH, fileName)
        image = cv2.imread(imagePath, cv2.IMREAD_GRAYSCALE)

        detectedFaces = FACE_DETECTOR.detectMultiScale(image)
        for (xpos, ypos, width, height) in detectedFaces:
            faces.append(image[ypos:ypos+height, xpos:xpos+width])
            IDs.append(ID)

    return faces, IDs

print("\nTraining Face Recognizer")
faces, IDs = getFacesAndID(PATH)

RECOGNIZER.train(faces, np.array(IDs))
RECOGNIZER.write('trainer/trainer.yml')

numTrained = len(set(IDs))
print("\n{} faces trained to recognizer. Exiting Program".format(numTrained))

