# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login1.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Signup(object):
    def setupUi(self, Signup):
        Signup.setObjectName("Signup")
        Signup.resize(400, 532)
        Signup.setAutoFillBackground(False)
        Signup.setStyleSheet("\n"
"background-color: rgb(0, 0, 0);")
        self.lineEdit = QtWidgets.QLineEdit(Signup)
        self.lineEdit.setGeometry(QtCore.QRect(140, 160, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("color: rgb(0, 85, 0);\n"
"background-color: rgb(0, 0, 0);")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Signup)
        self.label.setGeometry(QtCore.QRect(40, 160, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("\n"
"color: rgb(0, 85, 0);")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Signup)
        self.label_3.setGeometry(QtCore.QRect(40, 210, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 85, 0);")
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(Signup)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 210, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("color: rgb(0, 85, 0);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Signup)
        self.pushButton.setGeometry(QtCore.QRect(80, 290, 75, 23))
        self.pushButton.setStyleSheet("QPushButton\n"
"{\n"
"    color: rgb(255, 255, 255);\n"
"background-color : rgb(0, 0, 127);\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"background-color : rgb(0, 0, 255);\n"
"color:white;\n"
"}\n"
"QPushButton::pressed\n"
"{\n"
"background-color :rgb(0, 0, 127)  ;\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Signup)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 290, 75, 23))
        self.pushButton_2.setStyleSheet("QPushButton\n"
"{\n"
"    color: rgb(255, 255, 255);\n"
"background-color : rgb(0, 0, 127);\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"background-color : rgb(0, 0, 255);\n"
"color:white;\n"
"}\n"
"QPushButton::pressed\n"
"{\n"
"background-color :rgb(0, 0, 127)  ;\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(Signup)
        self.label_4.setGeometry(QtCore.QRect(30, 250, 301, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: red")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Signup)
        QtCore.QMetaObject.connectSlotsByName(Signup)

    def retranslateUi(self, Signup):
        _translate = QtCore.QCoreApplication.translate
        Signup.setWindowTitle(_translate("Signup", "Form"))
        self.label.setText(_translate("Signup", "Identification"))
        self.label_3.setText(_translate("Signup", "Password"))
        self.pushButton.setText(_translate("Signup", "Go"))
        self.pushButton_2.setText(_translate("Signup", "Message"))
