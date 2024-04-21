import tensorflow.compat.v1 as tf
from imutils.video import VideoStream


import argparse
from . import facenet
import imutils
import os
import sys
import math
import pickle
from . align import detect_face
import numpy as np
import cv2
from PyQt6 import QtGui
from PyQt6.QtGui import QImage
import collections
from sklearn.svm import SVC


class FaceRegconition():

    def __init__(self):

        self.MINSIZE = 20
        self.THRESHOLD = [0.6, 0.7, 0.7]
        self.FACTOR = 0.709
        self.IMAGE_SIZE = 182
        self.INPUT_IMAGE_SIZE = 160
        self.CLASSIFIER_PATH = 'Models/facemodel.pkl'
        self.FACENET_MODEL_PATH = 'Models/20180402-114759.pb'

        self.frame = None
        self.camera = False
        self.source_cam = 0

    def run(self):
        # Load The Custom Classifier
        with open(self.CLASSIFIER_PATH, 'rb') as file:
            model, class_names = pickle.load(file)
        print("Custom Classifier, Successfully loaded")

        src_cam = self.source_cam

        with tf.Graph().as_default():

            # Cai dat GPU neu co
            gpu_options = tf.compat.v1.GPUOptions(per_process_gpu_memory_fraction=0.6)
            sess = tf.compat.v1.Session(config=tf.compat.v1.ConfigProto(gpu_options=gpu_options, log_device_placement=False))

            with sess.as_default():

                # Load the model
                print('Loading feature extraction model')
                facenet.load_model(self.FACENET_MODEL_PATH)

                # Get input and output tensors
                images_placeholder = tf.get_default_graph().get_tensor_by_name("input:0")
                embeddings = tf.get_default_graph().get_tensor_by_name("embeddings:0")
                phase_train_placeholder = tf.get_default_graph().get_tensor_by_name("phase_train:0")
                embedding_size = embeddings.get_shape()[1]

                pnet, rnet, onet = detect_face.create_mtcnn(sess, "src/align")

                people_detected = set()
                person_detected = collections.Counter()

                cap  = VideoStream(src=src_cam).start()
                self.camera = True
                while (self.camera):
                    frame = cap.read()
                    frame = imutils.resize(frame, width=600)
                    frame = cv2.flip(frame, 1)

                    bounding_boxes, _ = detect_face.detect_face(frame, self.MINSIZE, pnet, rnet, onet, self.THRESHOLD, self.FACTOR)

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
                                print(bb[i][3]-bb[i][1])
                                print(frame.shape[0])
                                print((bb[i][3]-bb[i][1])/frame.shape[0])
                                if (bb[i][3]-bb[i][1])/frame.shape[0]>0.25:
                                    cropped = frame[bb[i][1]:bb[i][3], bb[i][0]:bb[i][2], :]
                                    scaled = cv2.resize(cropped, (self.INPUT_IMAGE_SIZE, self.INPUT_IMAGE_SIZE),
                                                        interpolation=cv2.INTER_CUBIC)
                                    scaled = facenet.prewhiten(scaled)
                                    scaled_reshape = scaled.reshape(-1, self.INPUT_IMAGE_SIZE, self.INPUT_IMAGE_SIZE, 3)
                                    feed_dict = {images_placeholder: scaled_reshape, phase_train_placeholder: False}
                                    emb_array = sess.run(embeddings, feed_dict=feed_dict)

                                    predictions = model.predict_proba(emb_array)
                                    best_class_indices = np.argmax(predictions, axis=1)
                                    best_class_probabilities = predictions[
                                        np.arange(len(best_class_indices)), best_class_indices]
                                    best_name = class_names[best_class_indices[0]]
                                    print("Name: {}, Probability: {}".format(best_name, best_class_probabilities))



                                    if best_class_probabilities > 0.6:
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
                                    else:
                                        name = "Unknown"
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

                    cv2.imshow('Face Recognition', frame)
                    # self.setPhoto(frame)
                    self.frame = frame
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break

                cap.release()
                cv2.destroyAllWindows()
    
    def stop(self):
        self.camera = False

    def setPhoto(self, image):
        image = imutils.resize(image,width=640)
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = QImage(frame, frame.shape[1],frame.shape[0],frame.strides[0],QImage.Format.Format_RGB888) 
        self.label.setPixmap(QtGui.QPixmap.fromImage(image)) 
        


