import os
import shutil
from ui.ui_student_image import *
from PyQt6.QtWidgets import QWidget
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout,QListWidgetItem,QMessageBox
from PyQt6.QtCore import QTimer
import cv2
from PyQt6.QtGui import QImage, QPixmap,QIcon
from tkinter import messagebox
import shutil
import imutils
from utils.image_info import *
from datetime import datetime

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

class TrainingWidget(QWidget):
    def __init__(self,masv):
        super().__init__()
        self.ui = Ui_StudentImage()
        self.ui.setupUi(self)

        self.masv = masv
        self.ui.btn_dong.clicked.connect(self.close_window)
        self.ui.btn_mocam.clicked.connect(self.open_camera)
        self.ui.btn_chupanh.clicked.connect(lambda: self.capture_photo())
        self.ui.listhinhanh.itemClicked.connect(self.display_image_in_label)
        self.ui.btn_xacnhan.clicked.connect(lambda:self.savePhotos())
        self.ui.btn_xoa.clicked.connect(lambda:self.deletePhoto())
        
        self.camera = False
        self.path_processed = 'face/Dataset/FaceData/processed/'
        self.path_processed = self.path_processed + str(self.masv)

        self.path_raw = 'face/Dataset/FaceData/raw/'
        self.path_raw = self.path_raw + str(self.masv)
       

        self.imageList = []
        
        self.loadImageList()
        self.display_images_in_listwidget()
        try:
            self.setPhoto(self.imageList[0].image)
        except:
            pass
        
    def deletePhoto(self):
        current_item = self.ui.listhinhanh.currentRow()
        self.imageList.pop(current_item)
        self.display_images_in_listwidget()
        self.ui.lb_numimg.setText(f"Số ảnh: {len(self.imageList)}")
        try:
            self.setPhoto(self.imageList[0].image)
        except:
            pass

    def loadImageList(self):
        self.imageList = []
        try:
            for filename in os.listdir(self.path_processed):
                img = cv2.imread(os.path.join(self.path_processed,filename))
                if img is not None:
                    imif = ImageInfo(filename, img)
                    self.imageList.append(imif)
            self.ui.lb_numimg.setText(f"Số ảnh: {len(self.imageList)}")
        except Exception as e:
            print(e)

    def open_camera(self):
        self.vid = cv2.VideoCapture(0)
        self.camera = True
        while(self.vid.isOpened() and self.camera):
            QtWidgets.QApplication.processEvents()	
            ret, self.frame = self.vid.read()
            if self.frame is not None:
                self.frame  = imutils.resize(self.frame ,height = 480)
                
                gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY) 
                self.faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.15,  
                minNeighbors=7, 
                minSize=(80, 80), 
                flags=cv2.CASCADE_SCALE_IMAGE)
                self.tmp = self.frame
                # for (x, y, w, h) in self.faces:
                #     face_gray = self.frame[y:y+h, x:x+w]
                #     cv2.rectangle(self.frame, (x, y), (x + w, y + h), (10, 228,220), 1) 
                
                self.setCam(self.frame)
                key = cv2.waitKey(1) & 0xFF
                if key == ord("q"):
                    break
    
    def setCam(self, image):
        self.tmp = image
        image = imutils.resize(image,width=640)
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = QImage(frame, frame.shape[1],frame.shape[0],frame.strides[0],QImage.Format.Format_RGB888) 
        self.ui.lb_cam.setPixmap(QtGui.QPixmap.fromImage(image))   

    def setPhoto(self, image):
        self.tmp = image
        image = imutils.resize(image,width=250)
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = QImage(frame, frame.shape[1],frame.shape[0],frame.strides[0],QImage.Format.Format_RGB888) 
        self.ui.lb_hinhanh.setPixmap(QtGui.QPixmap.fromImage(image)) 

    def capture_photo(self):
        if self.camera is True:
            filename = str('{}.jpg'.format(str(datetime.now())[:-7].replace(":","-").replace(" ","-")))
            imif = ImageInfo(filename, self.frame)
            self.imageList.append(imif)
            self.display_images_in_listwidget()
            self.ui.lb_numimg.setText(f"Số ảnh: {len(self.imageList)}")
        else:
            dlg = QtWidgets.QMessageBox()
            dlg.setWindowTitle("Thông báo!")
            dlg.setStyleSheet("QLabel{min-width: 150px;}")
            dlg.setText("Chưa mở camera")
            dlg.exec()

    def display_images_in_listwidget(self):
        self.ui.listhinhanh.clear()
        for imif in self.imageList:
            item = QListWidgetItem(imif.fileName)  
            self.ui.listhinhanh.addItem(item)

    def display_image_in_label(self):
        current_item = self.ui.listhinhanh.currentRow()
        self.setPhoto(self.imageList[current_item].image)

    def close_window(self):
        self.camera = False
        self.vid.release()

    def savePhotos(self):
        dlg = QtWidgets.QMessageBox()
        dlg.setWindowTitle("Thông báo!")
        dlg.setStyleSheet("QLabel{min-width: 250px;min-height: 100px;}")

        try:
            if os.path.exists(self.path_raw):
                shutil.rmtree(self.path_raw)
                print(f'Delete directory {self.path_raw} successfully')
            try:
                os.makedirs(self.path_raw)
                print(f'Create directory {self.path_raw} successfully')

                for imif in self.imageList:
                    path = os.path.join(self.path_raw, imif.fileName)
                    cv2.imwrite(path, imif.image) 
                dlg.setText("Lưu ảnh thành công")
                dlg.exec()   

                dlg.setText("Cần training lại khi có dữ liệu mới")
                dlg.exec()     

            except Exception as e:
                print(f'Failed to create directory: {e}')
                dlg.setText("Lưu ảnh thất bại")
                dlg.exec()
        except Exception as e:
            print(f'Failed to delete directory: {e}')
            dlg.setText("Lưu ảnh thất bại")
            dlg.exec()

