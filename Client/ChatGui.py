# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ChatGui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(827, 527)
        Form.setMinimumSize(QtCore.QSize(827, 527))
        Form.setMaximumSize(QtCore.QSize(827, 527))
        Form.setStyleSheet("background-color:rgb(54, 54, 54)")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(420, 10, 401, 511))
        self.textEdit.setStyleSheet("color:rgb(0, 170, 0);\n"
"background-color: rgb(0, 0, 0);")
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 10, 361, 211))
        self.textEdit_2.setStyleSheet("color: rgb(0, 255, 0);\n"
"background-color: rgb(0, 0, 0);")
        self.textEdit_2.setObjectName("textEdit_2")
        self.comboBox_3 = QtWidgets.QComboBox(Form)
        self.comboBox_3.setGeometry(QtCore.QRect(10, 290, 171, 22))
        self.comboBox_3.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255)")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_4 = QtWidgets.QComboBox(Form)
        self.comboBox_4.setGeometry(QtCore.QRect(10, 260, 171, 22))
        self.comboBox_4.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255)")
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(250, 230, 75, 23))
        self.pushButton_6.setStyleSheet("QPushButton\n"
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
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(170, 230, 75, 23))
        self.pushButton_7.setStyleSheet("QPushButton\n"
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
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(Form)
        self.pushButton_8.setGeometry(QtCore.QRect(90, 230, 75, 23))
        self.pushButton_8.setStyleSheet("QPushButton\n"
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
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(Form)
        self.pushButton_9.setGeometry(QtCore.QRect(10, 230, 75, 23))
        self.pushButton_9.setStyleSheet("QPushButton\n"
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
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(Form)
        self.pushButton_10.setGeometry(QtCore.QRect(330, 230, 75, 23))
        self.pushButton_10.setStyleSheet("QPushButton\n"
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
        self.pushButton_10.setObjectName("pushButton_10")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.comboBox_3.setItemText(0, _translate("Form", "AES"))
        self.comboBox_3.setItemText(1, _translate("Form", "RSA"))
        self.comboBox_3.setItemText(2, _translate("Form", "MDB5"))
        self.comboBox_3.setItemText(3, _translate("Form", "FPE"))
        self.comboBox_3.setItemText(4, _translate("Form", "3DES"))
        self.comboBox_3.setItemText(5, _translate("Form", "PGP"))
        self.comboBox_3.setItemText(6, _translate("Form", "BLOW FISH"))
        self.comboBox_3.setItemText(7, _translate("Form", "TWO FISH"))
        self.comboBox_3.setItemText(8, _translate("Form", "CEASER"))
        self.comboBox_4.setItemText(0, _translate("Form", "Local"))
        self.comboBox_4.setItemText(1, _translate("Form", "Global"))
        self.pushButton_6.setText(_translate("Form", "Call"))
        self.pushButton_7.setText(_translate("Form", "Record"))
        self.pushButton_8.setText(_translate("Form", "Send"))
        self.pushButton_9.setText(_translate("Form", "<<"))
        self.pushButton_10.setText(_translate("Form", ">>"))
