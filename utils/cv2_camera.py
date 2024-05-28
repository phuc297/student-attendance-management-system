import cv2
from PyQt6.QtCore import QThread

class CameraThread(QThread):

    def __init__(self):
        super().__init__()
        self.camera = cv2.VideoCapture(0)
        self.running = False

    def run(self):
        self.running = True
        while self.running:
            ret, frame = self.camera.read()
            if ret:
                self.change_pixmap_signal.emit(frame)
            else:
                break
        self.camera.release()

    def stop(self):
        self.running = False
        self.wait()