# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Админ\Desktop\ \Prog\Enigma_ui\ui version\ui files\enigma_ui.ui',
# licensing of 'C:\Users\Админ\Desktop\ \Prog\Enigma_ui\ui version\ui files\enigma_ui.ui' applies.
#
# Created: Fri Jun 12 15:05:32 2020
#      by: pyside2-uic  running on PySide2 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(630, 340)
        Dialog.setMinimumSize(QtCore.QSize(630, 330))
        Dialog.setMaximumSize(QtCore.QSize(630, 340))
        Dialog.setWindowOpacity(1.0)
        Dialog.setAccessibleName("")
        Dialog.setStyleSheet("font-family: Montserrat;\n"
"background-color: #353535; \n"
"font-size: 13px;")
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(250, 80, 130, 40))
        self.pushButton.setStyleSheet("background: #353535;\n"
"border: 1px solid #00FFFF;\n"
"box-sizing: border-box;\n"
"border-radius: 20px;\n"
"color: white;\n"
"font-size: 10pt;\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(250, 30, 30, 30))
        self.lineEdit_2.setStyleSheet("background: #353535;\n"
"border: 1px solid #00FFFF;\n"
"box-sizing: border-box;\n"
"border-radius: 15px;\n"
"color: white;\n"
"")
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(300, 30, 30, 30))
        self.lineEdit_4.setStyleSheet("background: #353535;\n"
"border: 1px solid #00FFFF;\n"
"box-sizing: border-box;\n"
"border-radius: 15px;\n"
"color: white;\n"
"")
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(350, 30, 30, 30))
        self.lineEdit_5.setStyleSheet("background: #353535;\n"
"border: 1px solid #00FFFF;\n"
"box-sizing: border-box;\n"
"border-radius: 15px;\n"
"color: white;\n"
"")
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 150, 130, 40))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background: #353535;\n"
"border: 1px solid #00FFFF;\n"
"box-sizing: border-box;\n"
"border-radius: 20px;\n"
"color: white;\n"
"font-size: 10pt;\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(250, 215, 130, 40))
        self.pushButton_3.setStyleSheet("background: #353535;\n"
"border: 1px solid #00FFFF;\n"
"box-sizing: border-box;\n"
"border-radius: 20px;\n"
"color: white;\n"
"font-size: 10pt;\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(20, 30, 210, 290))
        self.textEdit.setStyleSheet("background-color: #353535;\n"
"border: 1px solid #00FFFF;\n"
"box-sizing: border-box;\n"
"border-radius: 5px;\n"
"color: white;\n"
"")
        self.textEdit.setFrameShape(QtWidgets.QFrame.Panel)
        self.textEdit.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(400, 30, 211, 291))
        self.textEdit_2.setStyleSheet("background-color: #353535;\n"
"border: 1px solid #00FFFF;\n"
"box-sizing: border-box;\n"
"border-radius: 5px;\n"
"color: white;")
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(250, 280, 130, 40))
        self.pushButton_4.setStyleSheet("background: #353535;\n"
"border: 1px solid #00FFFF;\n"
"box-sizing: border-box;\n"
"border-radius: 20px;\n"
"color: white;\n"
"font-size: 10pt;\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(279, 4, 71, 21))
        self.label.setStyleSheet("color: white;\n"
"font-size: 17px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Enigma", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("Dialog", "Шифрование", None, -1))
        self.pushButton_2.setText(QtWidgets.QApplication.translate("Dialog", "Дешифрование", None, -1))
        self.pushButton_3.setText(QtWidgets.QApplication.translate("Dialog", "Скоприровать", None, -1))
        self.pushButton_4.setText(QtWidgets.QApplication.translate("Dialog", "Вставить шифр", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Dialog", "ENIGMA", None, -1))
