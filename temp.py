import time
import cv2, imutils
from PyQt6.QtGui import QImage
from ui.ui_attendence import *
import numpy as np

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

class AttendenceWidget(Ui_Attendence):

    def __init__(self, page):
        self.setupUi(page)
        
        self.camera = False
        self.vid = cv2.VideoCapture(0)

        self.btnOpenCam.clicked.connect(lambda: self.openCamera())
        self.btnCloseCam.clicked.connect(lambda: self.closeCamera())



    def openCamera(self):
        print("Dang mo camera")
        self.camera = True
        self.loadImage()

    def loadImage(self):
        
        cnt=0
        
        while(self.vid.isOpened() and self.camera):
            QtWidgets.QApplication.processEvents()	
            ret, self.image = self.vid.read()
            if ret:
                self.image  = imutils.resize(self.image ,height = 480 )
                gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY) 
                faces = faceCascade.detectMultiScale(
                    gray,
                    scaleFactor=1.15,  
                    minNeighbors=7, 
                    minSize=(80, 80), 
                    flags=cv2.CASCADE_SCALE_IMAGE)
                for (x, y, w, h) in faces:
                    cv2.rectangle(self.image, (x, y), (x + w, y + h), (10, 228,220), 5) 
                cnt+=1
                self.setPhoto(self.image)
            else:
                break
            
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                break


    def setPhoto(self,image):
        self.tmp = image
        image = imutils.resize(image,width=640)
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = QImage(frame, frame.shape[1],frame.shape[0],frame.strides[0],QImage.Format.Format_RGB888) 
        self.lbCamera.setPixmap(QtGui.QPixmap.fromImage(image))       

    def closeCamera(self):
        image = np.ones((640, 640, 3), dtype = np.uint8)
        image = 255*image
        self.setPhoto(image)
        self.camera = False
