from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt6.QtGui import QAction
import sys
import os

from ui import *
from student_widget import *
from teacher_widget import *
from subject_widget import *

class MenuForm(Ui_MainMenu):

    def initialize(self):

        self.initializePage()

        self.btnHome.clicked.connect(lambda: self.buttonClick(self.btnHome))
        self.btnAttendence.clicked.connect(lambda: self.buttonClick(self.btnAttendence))
        self.btnStudent.clicked.connect(lambda: self.buttonClick(self.btnStudent))
        self.btnTeacher.clicked.connect(lambda: self.buttonClick(self.btnTeacher))
        self.btnClass.clicked.connect(lambda: self.buttonClick(self.btnClass))
        self.btnSesson.clicked.connect(lambda: self.buttonClick(self.btnSesson))
        self.btnStat.clicked.connect(lambda: self.buttonClick(self.btnStat))
        self.btnAccount.clicked.connect(lambda: self.buttonClick(self.btnAccount))

    def initializePage(self):
        
        self.pageHome = QtWidgets.QWidget()
        self.pageAttendance = QtWidgets.QWidget()
        self.pageStudent = QtWidgets.QWidget()
        self.pageTeacher = QtWidgets.QWidget()
        self.pageClass = QtWidgets.QWidget()
        self.pageSession = QtWidgets.QWidget()
        self.pageStats = QtWidgets.QWidget()
        self.pageAccount = QtWidgets.QWidget()

        self.stackedWidget.addWidget(self.pageHome)
        self.stackedWidget.addWidget(self.pageAttendance)
        self.stackedWidget.addWidget(self.pageStudent)
        self.stackedWidget.addWidget(self.pageTeacher)
        self.stackedWidget.addWidget(self.pageClass)
        self.stackedWidget.addWidget(self.pageSession)
        self.stackedWidget.addWidget(self.pageStats)
        self.stackedWidget.addWidget(self.pageAccount)

        self.stackedWidget.setCurrentWidget(self.pageHome)
        UIFunctions.resetStyle(self, self.btnHome)
        self.btnHome.setStyleSheet(UIFunctions.selectMenu())

        home_page = HomeWidget(self.pageHome)

        student_page = StudentWidget(self.pageStudent)

        teacher_page = TeacherWidget(self.pageTeacher)

        subject_page = SubjectWidget(self.pageClass)

        account_page = AccountWidget(self.pageAccount)

        attendence_page = AttendenceWidget(self.pageAttendance)

        lesson_page = LessonWidget(self.pageSession)

    def buttonClick(self, btn):

        btnName = btn.objectName()

        if btnName == "btnHome":
            self.stackedWidget.setCurrentWidget(self.pageHome)
            UIFunctions.resetStyle(self, btn)
            self.btnHome.setStyleSheet(UIFunctions.selectMenu())

        if btnName == "btnAttendence":
            self.stackedWidget.setCurrentWidget(self.pageAttendance)
            UIFunctions.resetStyle(self, btn)
            self.btnAttendence.setStyleSheet(UIFunctions.selectMenu())

        if btnName == "btnStudent":
            self.stackedWidget.setCurrentWidget(self.pageStudent)
            UIFunctions.resetStyle(self, btn)
            self.btnStudent.setStyleSheet(UIFunctions.selectMenu())

        if btnName == "btnTeacher":
            self.stackedWidget.setCurrentWidget(self.pageTeacher)
            UIFunctions.resetStyle(self, btn)
            self.btnTeacher.setStyleSheet(UIFunctions.selectMenu())

        if btnName == "btnClass":
            self.stackedWidget.setCurrentWidget(self.pageClass)
            UIFunctions.resetStyle(self, btn)
            self.btnClass.setStyleSheet(UIFunctions.selectMenu())

        if btnName == "btnSesson":
            self.stackedWidget.setCurrentWidget(self.pageSession)
            UIFunctions.resetStyle(self, btn)
            self.btnSesson.setStyleSheet(UIFunctions.selectMenu())

        if btnName == "btnStat":
            self.stackedWidget.setCurrentWidget(self.pageStats)
            UIFunctions.resetStyle(self, btn)
            self.btnStat.setStyleSheet(UIFunctions.selectMenu())

        if btnName == "btnAccount":
            self.stackedWidget.setCurrentWidget(self.pageAccount)
            UIFunctions.resetStyle(self, btn)
            self.btnAccount.setStyleSheet(UIFunctions.selectMenu())


        
    
