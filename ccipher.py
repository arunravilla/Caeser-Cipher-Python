# Caesar Cipher Encryption and Decryption
def encryptMessage(message, key):
	message = message
	message = message.upper()
	key = key
	letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	letterslen = len(letters)
	translated = ""
	for m in message:
		if m in letters:
			myval = letters.find(m)
			myval = myval+key
		
			if myval >= letterslen:
				myval = myval-letterslen
			elif myval < 0:
				myval = myval+letterslen
			translated = translated + letters[myval]
		else:
			translated = translated + m	
	return translated
	
def decryptMessage(message, key):
	message = message
	message = message.upper()
	key = key
	letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	letterslen = len(letters)
	translated = ""
	for m in message:
		if m in letters:
			myval = letters.find(m)
			myval = myval-key
		
			if myval >= letterslen:
				myval = myval-letterslen
			elif myval < 0:
				myval = myval+letterslen
			translated = translated + letters[myval]
		else:
			translated = translated + m	
	return translated
