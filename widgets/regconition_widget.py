import time
import cv2, imutils
from PyQt6.QtGui import QImage
from PyQt6.QtWidgets import QMainWindow, QApplication
from bus.class_bus import ClassBUS
from ui.ui_attendence import *
from ui.ui_facereg import *
from ui.ui_sesson_selection import *
from bus.attend_bus import *
from bus.student_bus import *
from bus.sesson_bus import *
from bus.subject_bus import *
from bus.teacher_bus import *
import numpy as np
import threading
import os
import datetime


import tensorflow.compat.v1 as tf # type: ignore
from imutils.video import VideoStream
import argparse
import face.src.facenet as facenet
import imutils
import os
import sys
import math
import pickle
import face.src.align.detect_face as detect_face
import numpy as np
import cv2
from PyQt6 import QtGui
from PyQt6.QtGui import QImage
import collections
from sklearn.svm import SVC

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

times_dict = {
    1: datetime.datetime.strptime("2000-01-01 07:00:00", "%Y-%m-%d %H:%M:%S"),
    2: datetime.datetime.strptime("2000-01-01 07:50:00", "%Y-%m-%d %H:%M:%S"),
    3: datetime.datetime.strptime("2000-01-01 09:00:00", "%Y-%m-%d %H:%M:%S"),
    4: datetime.datetime.strptime("2000-01-01 09:50:00", "%Y-%m-%d %H:%M:%S"),
    5: datetime.datetime.strptime("2000-01-01 10:40:00", "%Y-%m-%d %H:%M:%S"),
    6: datetime.datetime.strptime("2000-01-01 13:00:00", "%Y-%m-%d %H:%M:%S"),
    7: datetime.datetime.strptime("2000-01-01 13:50:00", "%Y-%m-%d %H:%M:%S"),
    8: datetime.datetime.strptime("2000-01-01 15:00:00", "%Y-%m-%d %H:%M:%S"),
    9: datetime.datetime.strptime("2000-01-01 15:50:00", "%Y-%m-%d %H:%M:%S"),
    10: datetime.datetime.strptime("2000-01-01 16:40:00", "%Y-%m-%d %H:%M:%S"),
}

class RegconitionWidget(Ui_Attendence):

    def __init__(self, page):
        self.setupUi(page)
        
        self.maBH = None

        self.btnOpenCam.clicked.connect(lambda: self.openCamera())
        self.btnCloseCam.clicked.connect(lambda: self.closeCamera())
        self.btnDelete.clicked.connect(self.delete)
        self.btnBuoihoc.clicked.connect(self.openSessonSelectedWindow)

        self.ui = Ui_Face()
        self.ui_ses = Ui_SessonSelection()
        


        

    def loadTable(self):
        self.listStudents = {}
        self.list = AttendBUS.getList(self.maBH)
        if self.list is not None:
            self.tbDiemdanh.setRowCount(self.list.__len__())
            tablerow = 0
            for row in self.list:
                self.tbDiemdanh.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                self.tbDiemdanh.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                tensv = StudentBUS.getHoTen(str(row[1]))[0][0]
                self.tbDiemdanh.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(tensv))
                self.tbDiemdanh.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[2])))
                self.tbDiemdanh.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row[3])))
                self.tbDiemdanh.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(row[4])))
                
                obj = Attendence(row[0], row[1], row[2], row[3])
                self.listStudents[row[1]]=obj
                tablerow += 1

    def loadInfo(self):
        self.buoihoc = lessonBUS.get(self.maBH)[0]

        self.txt_mabh.setText(str(self.buoihoc[0]))

        tenmh = subjectBUS.getTenMH(str(self.buoihoc[1]))[0][0]
        self.txt_mh.setText(tenmh)
        self.txt_tuan.setText(str(self.buoihoc[2]))
        self.txt_tietbd.setText(str(self.buoihoc[3]))
        self.txt_tietkt.setText(str(self.buoihoc[4]))
        self.txt_ngay.setText(str(self.buoihoc[5]))

        magv = subjectBUS.getMaGV(str(self.buoihoc[1]))[0][0]
        self.txt_gv.setText(str(TeacherBUS.getHoTen(str(magv))[0][0]))

        tenlop = ClassBUS.getTenLop(str(self.buoihoc[0]))
        self.txt_lop.setText(tenlop)

    def openSessonSelectedWindow(self, s):
        self.sesson_window = QMainWindow()
        self.ui_ses.setupUi(self.sesson_window)
        self.ui_ses.btn_accept.clicked.connect(self.chooseSesson)
        self.loadSessonList()
        self.sesson_window.show()

    def loadSessonList(self):
        list = lessonBUS.get_all()
        if list is not None:
            self.ui_ses.table_bh.setRowCount(list.__len__())
            tablerow=0
            for row in list:
                self.ui_ses.table_bh.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                monHoc = subjectBUS.getTenMH(str(row[1]))[0][0]
                self.ui_ses.table_bh.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(monHoc))
                self.ui_ses.table_bh.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                maGV = subjectBUS.getMaGV(str(row[1]))[0][0]
                tenGV = TeacherBUS.getHoTen(str(maGV))[0][0]
                self.ui_ses.table_bh.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(tenGV))          
                self.ui_ses.table_bh.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row[3])))
                self.ui_ses.table_bh.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(row[4])))
                self.ui_ses.table_bh.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(str(row[5])))
                
                tenlop = ClassBUS.getTenLop(str(row[1]))
                self.ui_ses.table_bh.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(tenlop))      

                tablerow += 1

    def chooseSesson(self, s):
        try:
            cr = self.ui_ses.table_bh.currentRow()
            self.maBH = self.ui_ses.table_bh.item(cr, 0).text()
            self.sesson_window.hide()
            self.loadInfo()
            self.loadTable()
        except Exception as e:
            print(e)

    def checkList(self, masv):
            check = AttendBUS.check(masv, self.maBH)
            # print(f"{masv}  {self.maBH}")
            if len(check) < 1:
                self.bh = lessonBUS.get(self.maBH)
                current_dateTime = datetime.datetime.now()
                current_time = current_dateTime.time()
                start_time = times_dict[int(self.bh[0][3])].time()
                difference_seconds = (datetime.datetime.combine(datetime.date.today(), current_time) - datetime.datetime.combine(datetime.date.today(), start_time)).total_seconds()
                hours = difference_seconds // 3600
                minutes = (difference_seconds % 3600) // 60
                
                diff_seconds_sesson = (datetime.datetime.combine(datetime.date.today(), times_dict[int(self.bh[0][4])].time()) - datetime.datetime.combine(datetime.date.today(), start_time)).total_seconds()

                chitiet = ""
                if difference_seconds < diff_seconds_sesson:
                    gioVao = current_dateTime.strftime("%H:%M:%S")
                    if difference_seconds > 1000:
                        if hours >= 1:
                            chitiet = "Đến trễ " + str(int(hours)) + " tiếng " + str(int(minutes)) +" phút"
                        else:
                            chitiet = "Đến trễ "+ str(int(minutes)) +" phút"
                        if AttendBUS.add(self.maBH, masv, gioVao, 1, chitiet) == True:
                            
                                student = StudentBUS.get(masv)[0]
                                self.lbAleart.setText(f"{student[1]} MSSV {masv} vừa điểm danh")
                                self.loadTable()
                    else:
                        chitiet = "Vào đúng giờ"
                        if AttendBUS.add(self.maBH, masv, gioVao, 1, chitiet) == True:
                        
                            student = StudentBUS.get(masv)[0]
                            self.lbAleart.setText(f"{student[1]} MSSV {masv} vừa điểm danh")
                            self.loadTable()
                    
        

    def delete(self, s):
        try:
            cr = self.tbDiemdanh.currentRow()
            mabh = self.tbDiemdanh.item(cr, 0).text()
            masv = self.tbDiemdanh.item(cr, 1).text()
            if (AttendBUS.delete2(mabh, masv)):
                self.loadTable()
        except Exception as e:
            print(e)

    def newWindow(self):
        self.newwindow = QMainWindow()
        self.ui.setupUi(self.newwindow)
        self.newwindow.show()

    def openCamera(self):
        if self.maBH is not None:
            self.frame = None
            self.source_cam = 0
            self.camera = True
            self.newWindow()
            self.faceReg()
            # self.loadImage()

    def faceReg(self):
        MINSIZE = 20
        THRESHOLD = [0.6, 0.7, 0.7]
        FACTOR = 0.709
        IMAGE_SIZE = 182
        INPUT_IMAGE_SIZE = 160
        CLASSIFIER_PATH = 'face/Models/facemodel.pkl'
        FACENET_MODEL_PATH = 'face/Models/20180402-114759.pb'

        self.lbAleart.setText("Loading Face model")
        # Load The Custom Classifier
        with open(CLASSIFIER_PATH, 'rb') as file:
            model, class_names = pickle.load(file)
        print("Custom Classifier, Successfully loaded")

        src_cam = 0
        QtWidgets.QApplication.processEvents()
        with tf.Graph().as_default():

            # Cai dat GPU neu co
            gpu_options = tf.compat.v1.GPUOptions(per_process_gpu_memory_fraction=0.6)
            sess = tf.compat.v1.Session(config=tf.compat.v1.ConfigProto(gpu_options=gpu_options, log_device_placement=False))

            with sess.as_default():

                # Load the model
                print('Loading feature extraction model')
                self.lbAleart.setText("Loading feature extraction model")
                facenet.load_model(FACENET_MODEL_PATH)

                # Get input and output tensors
                images_placeholder = tf.get_default_graph().get_tensor_by_name("input:0")
                embeddings = tf.get_default_graph().get_tensor_by_name("embeddings:0")
                phase_train_placeholder = tf.get_default_graph().get_tensor_by_name("phase_train:0")
                embedding_size = embeddings.get_shape()[1]

                pnet, rnet, onet = detect_face.create_mtcnn(sess, "face/src/align")

                people_detected = set()
                person_detected = collections.Counter()

                self.cap  = VideoStream(src=src_cam).start()
                self.lbAleart.setText("Opening Camera")
                while (self.camera):
                    frame = self.cap.read()
                    frame = imutils.resize(frame, width=600)
                    frame = cv2.flip(frame, 1)

                    bounding_boxes, _ = detect_face.detect_face(frame, MINSIZE, pnet, rnet, onet, THRESHOLD, FACTOR)

                    faces_found = bounding_boxes.shape[0]
                    try:
                        if faces_found > 1:
                            cv2.putText(frame, "Only one face", (0, 100), cv2.FONT_HERSHEY_COMPLEX_SMALL,
                                        1, (255, 255, 255), thickness=1, lineType=2)
                        elif faces_found > 0:
                            det = bounding_boxes[:, 0:4]
                            bb = np.zeros((faces_found, 4), dtype=np.int32)
                            for i in range(faces_found):
                                bb[i][0] = det[i][0]
                                bb[i][1] = det[i][1]
                                bb[i][2] = det[i][2]
                                bb[i][3] = det[i][3]
                                # print(bb[i][3]-bb[i][1])
                                # print(frame.shape[0])
                                # print((bb[i][3]-bb[i][1])/frame.shape[0])
                                if (bb[i][3]-bb[i][1])/frame.shape[0]>0.25:
                                    cropped = frame[bb[i][1]:bb[i][3], bb[i][0]:bb[i][2], :]
                                    scaled = cv2.resize(cropped, (INPUT_IMAGE_SIZE, INPUT_IMAGE_SIZE),
                                                        interpolation=cv2.INTER_CUBIC)
                                    scaled = facenet.prewhiten(scaled)
                                    scaled_reshape = scaled.reshape(-1, INPUT_IMAGE_SIZE, INPUT_IMAGE_SIZE, 3)
                                    feed_dict = {images_placeholder: scaled_reshape, phase_train_placeholder: False}
                                    emb_array = sess.run(embeddings, feed_dict=feed_dict)

                                    predictions = model.predict_proba(emb_array)
                                    best_class_indices = np.argmax(predictions, axis=1)
                                    best_class_probabilities = predictions[
                                        np.arange(len(best_class_indices)), best_class_indices]
                                    best_name = class_names[best_class_indices[0]]
                                    # print("Name: {}, Probability: {}".format(best_name, best_class_probabilities))



                                    if best_class_probabilities > 0.7:
                                        cv2.rectangle(frame, (bb[i][0], bb[i][1]), (bb[i][2], bb[i][3]), (0, 255, 0), 2)
                                        text_x = bb[i][0]
                                        text_y = bb[i][3] + 20

                                        name = class_names[best_class_indices[0]]
                                        cv2.putText(frame, name, (text_x, text_y), cv2.FONT_HERSHEY_COMPLEX_SMALL,
                                                    1, (255, 255, 255), thickness=1, lineType=2)
                                        cv2.putText(frame, str(round(best_class_probabilities[0], 3)), (text_x, text_y + 17),
                                                    cv2.FONT_HERSHEY_COMPLEX_SMALL,
                                                    1, (255, 255, 255), thickness=1, lineType=2)
                                        person_detected[best_name] += 1

                                        self.checkList(name)
                                    else:
                                        name = ""
                                        cv2.rectangle(frame, (bb[i][0], bb[i][1]), (bb[i][2], bb[i][3]), (0, 255, 0), 2)
                                        text_x = bb[i][0]
                                        text_y = bb[i][3] + 20

                                        cv2.putText(frame, name, (text_x, text_y), cv2.FONT_HERSHEY_COMPLEX_SMALL,
                                                    1, (255, 255, 255), thickness=1, lineType=2)
                                        cv2.putText(frame, str(round(best_class_probabilities[0], 3)), (text_x, text_y + 17),
                                                    cv2.FONT_HERSHEY_COMPLEX_SMALL,
                                                    1, (255, 255, 255), thickness=1, lineType=2)
                                        

                    except:
                        pass

                    # cv2.imshow('Face Recognition', frame)
                    self.setPhoto(frame)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                cv2.destroyAllWindows()

    def setPhoto(self,image):
        self.tmp = image
        image = imutils.resize(image,width=450)
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = QImage(frame, frame.shape[1],frame.shape[0],frame.strides[0],QImage.Format.Format_RGB888) 
        self.ui.lbCamera.setPixmap(QtGui.QPixmap.fromImage(image))       

    def closeCamera(self):
        self.camera = False
        self.cap.stop()
        image = np.ones((640, 640, 3), dtype = np.uint8)
        image = 255*image
        self.setPhoto(image)
        self.newwindow.hide()
