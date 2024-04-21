import os
import shutil
from ui.ui_capimge import *
from PyQt6.QtWidgets import QWidget
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout,QListWidgetItem,QMessageBox
from PyQt6.QtCore import QTimer
import cv2
from PyQt6.QtGui import QImage, QPixmap,QIcon
from tkinter import messagebox
import shutil



class TrainingWidget(QWidget):
    def __init__(self,masv,):
        super().__init__()
        self.ui = Ui_Capimge()
        self.ui.setupUi(self)
        self.ui.btn_dong.clicked.connect(self.close_window)
        self.ui.btn_mocam.clicked.connect(self.open_camera)
        self.ui.btn_chupanh.clicked.connect(lambda: self.capture_photo(masv))
        self.ui.listhinhanh.itemClicked.connect(self.display_image_in_label)
        # self.ui.btn_xacnhan.clicked.connect(lambda:self.xacnhan(masv))

        self.listanh=[]
        self.dataset_path = "dataset"
        self.masv_folder=""
        # Tạo thư mục dataset nếu nó không tồn tại
        if not os.path.exists(self.dataset_path):
            os.makedirs(self.dataset_path)
        self.datasettam_path = "dataset_tam"
        # Tạo thư mục dataset nếu nó không tồn tại
        if not os.path.exists(self.datasettam_path):
            os.makedirs(self.datasettam_path)
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    
    #Hàm để khi ấn nút chụp thì chụp 10 anh----------------------------------#
    def capture_photo(self,masv):
        # Đảm bảo rằng camera đã được mở
        
        if not self.cap.isOpened():
            print("Vui lòng mở camera trước khi chụp ảnh")
            return
        
        ret, frame = self.cap.read()

        if ret:

            
            
            # for file_name in os.listdir(self.masv_folder):
            #     file_path = os.path.join(self.masv_folder, file_name)

            #     if os.path.isfile(file_path):
            #         os.remove(file_path)

            # Phát hiện khuôn mặt trong khung hình
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
            

            # Lưu ảnh với các khuôn mặt phát hiện được
            for (x, y, w, h) in faces:
                # Vẽ hình chữ nhật xung quanh khuôn mặt
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                
                # Cắt và lưu ảnh khuôn mặt
                face_gray = gray[y:y+h, x:x+w]
                # face_path = os.path.join(self.masv_folder, f"face_{len(os.listdir(self.masv_folder)) + 1}.jpg")
                # cv2.imwrite(face_path, face_gray)
                # image_paths.append(face_path)
                self.listanh.append(face_gray)
                    
            
            self.display_images_in_listwidget()
            
        else:
            messagebox.showinfo("", "chụp ảnh thất bại")

    def display_images_in_listwidget(self):
        
        for anh in range(0,len(self.listanh)):
            
            item = QListWidgetItem(str(anh))  # Sử dụng tên tệp làm văn bản cho mục
            self.ui.listhinhanh.addItem(item)
    
    def display_image_in_label(self):
    # Lấy mục hiện tại được chọn trong QListWidget
        current_item = self.ui.listhinhanh.currentItem()
        if current_item is not None:
            
            # Lấy đường dẫn của ảnh từ mục được chọn
            # image_path = os.path.join(self.masv_folder, current_item.text())
            
            # Hiển thị ảnh trong QLabel
            # pixmap = QPixmap(image_path)

            # self.ui.lb_hinhanh.setPixmap(pixmap)

            self.ui.lb_hinhanh.setScaledContents(True)

    def close_window(self):
        try:
            shutil.rmtree(self.masv_folder)
            print(f"Đã xóa thư mục {self.masv_folder} và tất cả các tệp con thành công.")
        except OSError as e:
            print(f"Lỗi: {e.filename} - {e.strerror}.")
        self.close()

    def open_camera(self):
          # 10ms
        if hasattr(self, 'cap') and self.cap.isOpened():
            self.cap.release()
            self.ui.lb_cam.clear()
        else:
            self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) 
            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)

            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)

            self.cap.set(cv2.CAP_PROP_FOURCC, 0x32595559)

            self.cap.set(cv2.CAP_PROP_FPS, 25)
            # Chỉ số của webcam
            if not self.cap.isOpened():
                print("Không thể mở webcam")
                return
            self.timer = QTimer(self)
            self.timer.timeout.connect(self.update_frame)
            self.timer.start(10)

    def update_frame(self):
     ret, frame = self.cap.read()
     if ret:
        # Chuyển đổi frame từ OpenCV sang QImage
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = frame.shape
        bytesPerLine = ch * w
        img = QImage(frame.data, w, h, bytesPerLine, QImage.Format.Format_RGB888)

        # Đặt kích thước widget theo tỉ lệ với kích thước hình ảnh gốc
        self.ui.lb_cam.setFixedSize(w, h)

        pixmap = QPixmap.fromImage(img)
        # Điều chỉnh kích thước hình ảnh để phù hợp với kích thước widget
        pixmap = pixmap.scaled(self.ui.lb_cam.size(), QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        # Hiển thị hình ảnh trong widget
        self.ui.lb_cam.setPixmap(pixmap)
            
    # def xacnhan(self, masv):
    #     # Xác nhận người dùng có muốn thực hiện hành động hay không
    #     response = messagebox.askokcancel("Xác nhận", "Bạn có chắc muốn xác nhận không?")
    #     self.masv_folder= os.path.join(self.dataset_path, masv)
    #     if response:
    #         # Xóa tất cả các file ảnh trong self.masv_folder
    #         for file_name in os.listdir(self.masv_folder):
    #             file_path = os.path.join(self.masv_folder, file_name)
    #             if os.path.isfile(file_path):
    #                 os.remove(file_path)
            
    #         # Di chuyển tất cả các tệp từ self.datasettam_path/masv sang self.dataset_path/masv
    #         source_folder = os.path.join(self.datasettam_path, masv)
    #         destination_folder = os.path.join(self.dataset_path, masv)
    #         if os.path.exists(source_folder) and os.path.exists(destination_folder):
    #             for file_name in os.listdir(source_folder):
    #                 source = os.path.join(source_folder, file_name)
    #                 destination = os.path.join(destination_folder, file_name)
    #                 shutil.move(source, destination)
    #     else:
    #         print("Hủy thao tác.")
    
    def __del__(self):
        if self.cap.isOpened():
            self.cap.release()
            self.ui.lb_cam.clear()
