# Ввод сообщения и кодировочных чисел
incoming_message = str(input("Введите текст для шифрования/дешифрования: "))
encode_count_1 = int(input("Введите число кодировки №1: "))
encode_count_2 = int(input("Введите число кодировки №2: "))
encode_count_3 = int(input("Введите число кодировки №3: "))

type_of_encoding = int(input("Выберите функцию, 0 - шифрование, 1 - дешифрование: "))

if type_of_encoding == 0:

	list_of_incoming_message = list(incoming_message)

	# Создание списка под забивку кодами символов в кодировке ASCII и его кодированного собрата

	ascii_symbol_list_incoming_message = []
	crypted_ascii_symbol_list_incoming_message = []
	# Забивка списка

	for i in range(len(list_of_incoming_message)):
		ascii_symbol_list_incoming_message.append(ord(list_of_incoming_message[i]))

	# Дополнительное шифрование кодов числами из int(input())

	for i in range(len(ascii_symbol_list_incoming_message)):
		crypted_ascii_symbol_list_incoming_message.append(ascii_symbol_list_incoming_message[i]*encode_count_1 + encode_count_2 - encode_count_3)

	# Переход от чисел к символам:

	list_crypted_message = []

	for i in range(len(crypted_ascii_symbol_list_incoming_message)):
		list_crypted_message.append(chr(crypted_ascii_symbol_list_incoming_message[i]))

	crypted_string = ""

	for i in range(len(list_crypted_message)):
		crypted_string += list_crypted_message[i]

	print(crypted_string)

else:
	list_of_incoming_message = list(incoming_message)

	# Создание списка под забивку кодами символов в кодировке ASCII и его кодированного собрата

	ascii_symbol_list_incoming_message = []
	crypted_ascii_symbol_list_incoming_message = []
	# Забивка списка

	for i in range(len(list_of_incoming_message)):
		ascii_symbol_list_incoming_message.append(ord(list_of_incoming_message[i]))

	# Дополнительное шифрование кодов числами из int(input())
	for i in range(len(ascii_symbol_list_incoming_message)):
		crypted_ascii_symbol_list_incoming_message.append(int((ascii_symbol_list_incoming_message[i] + encode_count_3 - encode_count_2) / encode_count_1 ))

	# Переход от чисел к символам:

	list_crypted_message = []

	for i in range(len(crypted_ascii_symbol_list_incoming_message)):
		list_crypted_message.append(chr(crypted_ascii_symbol_list_incoming_message[i]))

	crypted_string = ""

	for i in range(len(list_crypted_message)):
		crypted_string += list_crypted_message[i]

	print(crypted_string)
