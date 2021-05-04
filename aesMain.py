import pyAesCrypt
import argparse
import pickle
import os
import consoleColor as cc

class Account:
	def __init__(self, id: str, userId:str, password:str):
		self.id=id
		self.userId = userId
		self.password = password
	
	def __str__(self):
		return "id: {0}, userId: {1}, password: {2}".format(self.id, self.userId, self.password)
	
	def __eq__(self, value):
		return self.id == value.id and self.userId == value.userId and self.password == value.password

class Arguments:
	def __init__(self, args:dict):
		args.setdefault("password", "")
		args.setdefault("acc", "")
		args.setdefault("newacc", "")
		args.setdefault("out", "./.encr")
		self.__dict__ = args
	
	def __str__(self):
		return str(self.__dict__)


tmpFile = "tmp"
bufferSize = 64 * 1023

def managePasswords(args:Arguments):
	print(args)
	
	passwd = args.password
	if args.acc is not None:
		if os.path.exists(args.out):
			pyAesCrypt.decryptFile(args.out, tmpFile, passwd, bufferSize)

		with open(tmpFile, "rb+") as data:
			try:
				accounts = pickle.load(data)
			except Exception as e:
				cc.cPrint("File could not be read", cc.RED)
				print(e)
				accounts = dict()

			account = accounts.get(args.acc, Account("none", "none", "none"))
			return account
		os.remove(tmpFile)

	elif args.newacc is not None:
		tmp = args.newacc.split(':')
		newAccount = Account(tmp[0], tmp[1], tmp[2])

		if os.path.exists(args.out):
			pyAesCrypt.decryptFile(args.out, tmpFile, passwd, bufferSize)
		else:
			with open(tmpFile, "w"):
				pass

		with open(tmpFile, "rb+") as data:
			try:
				accounts = pickle.load(data)
			except EOFError as eof:
				cc.cPrint("File could not be read because it is empty", cc.RED)
				accounts = dict()
			accounts.setdefault(newAccount.id, newAccount)
			pickle.dump(accounts, data)
		pyAesCrypt.encryptFile(tmpFile, args.out, passwd, bufferSize)
		
		try:
			os.remove(tmpFile)
			return "Successfully added {0} to {1}".format(newAccount, args.out)
		except Exception as e:
			cc.cPrint("Security Breach!", cc.RED)
			print(e)	


if __name__ == "__main__":

	descr = "A local passwordmanager."
	parser = argparse.ArgumentParser(description=descr)
	parser.add_argument('password', metavar='P', type=str, help='The password')
	parser.add_argument('-acc', metavar='ACCOUNT', type=str, help='The name of the account')
	parser.add_argument('-out', metavar='OUTFILE', type=str, default="./.encr", help='The file to use as a outputfile')
	parser.add_argument('-newacc', metavar='New Account', type=str, help='AccountID:UserID:Password')

	args = parser.parse_args()
	managePasswords(Arguments(args.__dict__))