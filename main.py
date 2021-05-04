from aesMain import *
import tkinter as tk

from win10toast import *

class Application(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.pack()
		self.create_widgets()

		self.toaster = ToastNotifier()

	def create_widgets(self):
		self.accountFr = tk.Frame(self)
		self.accountFr.pack()
		self.accountTb = tk.Entry(self.accountFr)
		self.accountTb.pack()
		self.accountL = tk.Label(self.accountFr, text="Account Name")
		self.accountL.pack(side="left")

		self.userIdFr = tk.Frame(self)
		self.userIdFr.pack()
		self.userIdTb = tk.Entry(self.userIdFr)
		self.userIdTb.pack(side="top")
		self.userIdL = tk.Label(self.userIdFr, text="User Name")
		self.userIdL.pack(side="left")

		self.passwordFr = tk.Frame(self)
		self.passwordFr.pack()
		self.passwordTb = tk.Entry(self.passwordFr)
		self.passwordTb.pack(side="top")
		self.passwordL = tk.Label(self.passwordFr, text="Password")
		self.passwordL.pack(side="left")

		self.masterPasswordFr = tk.Frame(self) 
		self.masterPasswordFr.pack()
		self.masterPasswordTb = tk.Entry(self.masterPasswordFr)
		self.masterPasswordTb.pack(side="top")
		self.masterPasswordL = tk.Label(self.masterPasswordFr, text="Master-Password")
		self.masterPasswordL.pack(side="left")


		self.bottomActions = tk.Frame(self)
		self.bottomActions.pack()
		self.createBtn = tk.Button(self.bottomActions, text="Create", command=self.createAccount)
		self.createBtn.pack(side="left")
		self.loadBtn = tk.Button(self.bottomActions, text="Load", command=self.loadAccount)
		self.loadBtn.pack(side="right")



	def createAccount(self):
		accountId = self.accountTb.get()
		userId = self.userIdTb.get()
		password = self.passwordTb.get()
		if managePasswords(Arguments({"newacc": accountId+":"+userId+":"+ password, "password": "asdf"})) is not None:
			self.toaster.show_toast("Success", "Account {0} added".format(accountId))

	def loadAccount(self):
		account = managePasswords(Arguments({"acc": self.accountTb.get(), "password": self.masterPasswordTb.get()}))
		if not account == Account("none", "none", "none"):
			self.userIdTb["text"] = account.userId
			self.passwordTb["text"] = account.password
			self.toaster.show_toast("Success", "{0}-Account successfully read".format(account.id), threaded=True)
			self.update()
		else:
			self.toaster.show_toast("Error", "{0}-Account could not be found, or there is another error".format(account.id))



root = tk.Tk()
app = Application(master=root)
app.mainloop()