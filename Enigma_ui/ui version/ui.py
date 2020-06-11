# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Админ\Desktop\Prog\Enigma_ui\ui version\enigma_ui.ui',
# licensing of 'C:\Users\Админ\Desktop\Prog\Enigma_ui\ui version\enigma_ui.ui' applies.
#
# Created: Thu Jun 11 19:41:43 2020
#      by: pyside2-uic  running on PySide2 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(630, 213)
        Dialog.setStyleSheet("font-family: Ubuntu; background-color: #5e5e5e;font-size: 13px;")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(260, 70, 111, 41))
        self.pushButton.setStyleSheet("border: 0;\n"
"border-radius: 15px;\n"
"background-color: #fafafa;")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(250, 20, 31, 31))
        self.lineEdit_2.setStyleSheet("text-align: center; border: 0; background-color: #fafafa;vertical-align: middle;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(300, 20, 31, 31))
        self.lineEdit_4.setStyleSheet("text-align: center; border: 0; background-color: #fafafa;vertical-align: middle;")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(350, 20, 31, 31))
        self.lineEdit_5.setStyleSheet("text-align: center; border: 0; background-color: #fafafa;vertical-align: middle;")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 120, 111, 41))
        self.pushButton_2.setStyleSheet("border: 0;\n"
"border-radius: 15px;\n"
"background-color: #fafafa;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(440, 160, 121, 31))
        self.pushButton_3.setStyleSheet("border: 0;\n"
"border-radius: 15px;\n"
"background-color: #fafafa;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(20, 20, 211, 171))
        self.textEdit.setStyleSheet("border-radius: 5px; background-color: #fafafa;vertical-align: top;")
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(400, 20, 201, 121))
        self.textEdit_2.setStyleSheet("border-radius: 5px; background-color: #fafafa;vertical-align: top;")
        self.textEdit_2.setObjectName("textEdit_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Dialog", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("Dialog", "Шифрование", None, -1))
        self.pushButton_2.setText(QtWidgets.QApplication.translate("Dialog", "Дешифрование", None, -1))
        self.pushButton_3.setText(QtWidgets.QApplication.translate("Dialog", "Скоприровать", None, -1))
