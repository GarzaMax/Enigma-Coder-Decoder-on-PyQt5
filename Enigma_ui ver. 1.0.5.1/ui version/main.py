# Import PyQt5 libs
import sys
from PySide2 import QtCore, QtGui, QtWidgets
from ui import Ui_Dialog
\
# Import another libs
import pyperclip

# Initiallizing

app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()



# Main logic

def crypt():
	ui.textEdit_2.clear()
	incoming_message = ui.textEdit.toPlainText()
	encode_count_1 = int(ui.lineEdit_2.text())
	encode_count_2 = int(ui.lineEdit_4.text())
	encode_count_3 = int(ui.lineEdit_5.text())

	if encode_count_1 > 11 or encode_count_2 > 11 or encode_count_3 > 11:
		ui.textEdit_2.setText("ЧИСЛА КОДИРОВАНИЯ/ДЕКОДИРОВАНИЯ НЕ ДОЛЖНЫ ПРЕВЫШАТЬ 11-ти!!!")
		
	else:

		list_of_incoming_message = list(incoming_message)

		ascii_symbol_list_incoming_message = []
		crypted_ascii_symbol_list_incoming_message = []

		for i in range(len(list_of_incoming_message)):
			ascii_symbol_list_incoming_message.append(
				ord(list_of_incoming_message[i])
				)
	
		for i in range(len(ascii_symbol_list_incoming_message)):
			crypted_ascii_symbol_list_incoming_message.append(
				ascii_symbol_list_incoming_message[i]*encode_count_1 + encode_count_2 - encode_count_3
				)


		list_crypted_message = []

		for i in range(len(crypted_ascii_symbol_list_incoming_message)):
			list_crypted_message.append(chr(crypted_ascii_symbol_list_incoming_message[i]))

		crypted_string = ""

		for i in range(len(list_crypted_message)):
			crypted_string += list_crypted_message[i]

		ui.textEdit_2.setText(crypted_string)






def encrypt_conf():
	ui.textEdit_2.clear()
	incoming_message = ui.textEdit.toPlainText()
	encode_count_1 = int(ui.lineEdit_2.text())
	encode_count_2 = int(ui.lineEdit_4.text())
	encode_count_3 = int(ui.lineEdit_5.text())

	if encode_count_1 > 11 or encode_count_2 > 11 or encode_count_3 > 11:
		ui.textEdit_2.setText("ЧИСЛА КОДИРОВАНИЯ/ДЕКОДИРОВАНИЯ НЕ ДОЛЖНЫ ПРЕВЫШАТЬ 11-ти!!!")
	

	else:

		dec_list_of_incoming_message = incoming_message.split()

		list_of_incoming_message = dec_list_of_incoming_message[3]
		encode_countbar_1 = int(dec_list_of_incoming_message[0])
		encode_countbar_2 = int(dec_list_of_incoming_message[1])
		encode_countbar_3 = int(dec_list_of_incoming_message[2])


		ascii_symbol_list_incoming_message = []
		crypted_ascii_symbol_list_incoming_message = []

		for i in range(len(list_of_incoming_message)):
			ascii_symbol_list_incoming_message.append(ord(list_of_incoming_message[i]))

		for i in range(len(ascii_symbol_list_incoming_message)):
			crypted_ascii_symbol_list_incoming_message.append(int((ascii_symbol_list_incoming_message[i] + encode_countbar_3 - encode_countbar_2) / encode_countbar_1 ))

		list_crypted_message = []

		for i in range(len(crypted_ascii_symbol_list_incoming_message)):
			list_crypted_message.append(chr(crypted_ascii_symbol_list_incoming_message[i]))

		crypted_string = ""

		for i in range(len(list_crypted_message)):
			crypted_string += list_crypted_message[i]

		ui.textEdit_2.setText(crypted_string)


def copying_conf():
	encode_count_1 = ui.lineEdit_2.text()
	encode_count_2 = ui.lineEdit_4.text()
	encode_count_3 = ui.lineEdit_5.text()
	output_crypt = encode_count_1 + " " + encode_count_2 + " " + encode_count_3 + " " + ui.textEdit_2.toPlainText()
	pyperclip.copy(output_crypt)



def pasting():
	ui.textEdit.clear()
	ui.textEdit_2.clear()
	ui.textEdit.paste()


check_dial = 1





ui.pushButton.clicked.connect( crypt )


ui.pushButton_2.clicked.connect( encrypt_conf )



ui.pushButton_3.clicked.connect( copying_conf )


ui.pushButton_4.clicked.connect( pasting )
#Launch
sys.exit(app.exec_())