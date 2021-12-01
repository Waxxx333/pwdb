#!/usr/bin python
#-*- encoding: utf-8 -*-
from Crypto.Cipher import AES;
import base64, re, os, sys, readline, getpass;
from time import sleep;
from tabulate import tabulate;
"""
# To install pycrypto in Windows:
$ pip install pycryptodome
# Windows doesn't come with readline
$ pip install pyreadline
"""
#Global Variables
home = (os.path.expanduser("~"))
path = (f"{home}/.")
pass_db = (f"{path}pass.txt")
account_db = (f"{path}accounts.txt")
user_db = (f"{path}users.txt")
notes_db = (f"{path}notes.txt")
user = (getpass.getuser())
readline.parse_and_bind("tab: complete")
Version=('V-0.2');
#Colors
RED='\033[38;5;1m'
RRED='\033[38;5;9m'
GREEN='\033[38;5;46m'
GGREEN='\033[38;5;10m'
INVISIBLE='\033[08m'
RESET='\033[0m'
BOLD='\033[01m'
DARK='\033[38;5;245m'
def complete(text,state):
    volcab = ['create','view','exit','yes','no']
    results = [x for x in volcab if x.startswith(text)] + [None]
    return results[state]
readline.set_completer(complete)
print(f"""
				{GGREEN}┳{RED}━{GREEN}┓{RRED}┓ {GREEN}┳┳{RRED}━{GGREEN}┓{RED}┳━{GREEN}┓
				{RRED}┃{GREEN}━{RED}┛{GGREEN}┃{RED}┃{RRED}┃{GREEN}┃ {GGREEN}┃{GREEN}┃{RED}━{GGREEN}┃
				{GGREEN}┇  {RED}┗{GREEN}┻{RRED}┇{GGREEN}┇{RED}━{GGREEN}┛{RRED}┇{GREEN}━{RED}┛
			Ｐａｓｓｗｏｒｄ Ｄａｔａｂａｓｅ
				    {Version}
			{GGREEN}▓{RRED}█{GREEN}█{RED}▓{GGREEN}▓{RRED}█{GREEN}█{RED}█{GGREEN}▓{RED}▒{GREEN}▒{RRED}▒{GGREEN}▒{RED}▓{GREEN}▓{RRED}▓{GGREEN}▓{RED}▒{GGREEN}▒{RRED}▓{GREEN}█{RED}█{RRED}▓{GGREEN}▓{RED}█{GREEN}█{RRED}█{GGREEN}▓{RED}▒{GREEN}▒
""")
def echo_s(data):
	blank = ' '
	s = ''
	for l in blank:
		sys.stdout.write('\r')
		sys.stdout.write(f"{DARK}[{GREEN}-{GGREEN}*{GREEN}-{DARK}] {GGREEN}{data} {DARK}[{GREEN}-{GGREEN}*{GREEN}-{DARK}]")
		s+='%s'%l
		sys.stdout.flush()
		sleep(0.1)
	print()
def echo_f(data):
	blank = ' '
	s = ''
	for l in blank:
		sys.stdout.write('\r')
		sys.stdout.write(f"{DARK}[{RED}-{RRED}!{RED}-{DARK}] {RRED}{data} {DARK}[{RED}-{RRED}!{RED}-{DARK}]")
		s+='%s'%l
		sys.stdout.flush()
		sleep(0.1)
	print()

class password_db:
	""" Class doc """	
	def __init__ (self):
		key = '1234567890123456'
		self.cipher = AES.new(key,AES.MODE_ECB)
		self.failed_attempts = 0
		self.Asymmetrical = 0
		self.login()
	def login(self):
		try:
			with open(f"{pass_db}",'r') as confirm:
				confirm.readlines()
		except:
			data = (f"{RRED}No database found {GREEN}| {RRED}You must setup a database password")
			echo_f(data)
			data = (f"{GGREEN}Enter password")
			echo_s(data)
			password_raw = input(f"{RED}=={GREEN}> {INVISIBLE} ").rjust(32);print(RESET,BOLD)
			data = (f"Confirm password")
			echo_s(data)
			check = input(f"{RED}=={GREEN}> {INVISIBLE} ").rjust(32);print(RESET,BOLD)
			if check != password_raw:
				data = (f"{RRED}Passwords don't match. Try again")
				echo_f(data)
				self.login()
			elif check == password_raw:
				encoded = base64.b64encode(self.cipher.encrypt(password_raw)).decode('utf-8')
				os.system('echo mainkey %s > %s'%(encoded,pass_db))
				data = (f"{GGREEN}Database password successfully stored{DARK}.{RED} Be sure to remember this{DARK}.")
				echo_s(data)
				data = (f"{RED}Failure to do so will result in database self-destruction{DARK}.")
				echo_f(data)
		try:
			with open(account_db,'r') as confirm2:
				confirm2.readlines()
		except:
			data = (f"{RED}No account database found{DARK}. {GGREEN}Creating one now{DARK}.")
			echo_f(data)
			os.system('touch %s'%account_db)
			data = (f"{GREEN}{account_db} {GGREEN}has been created{DARK}.")
			echo_s(data)
		try: 
			with open(user_db, 'r') as confirm3:
				confirm3.readlines()
		except:
			data = (f"{RED}No user database found{DARK}. {GGREEN}Creating one now{DARK}.")
			echo_f(data)
			os.system('touch %s'%(user_db))
			data = (f"{GREEN}{user_db}{GGREEN} has been created{DARK}.")
			echo_s(data)
		try: 
			with open(notes_db, 'r') as confirm4:
				confirm4.readlines()
		except:
			data = (f"{RED}No notes database found{DARK}. {GGREEN}Creating one now{DARK}.")
			echo_f(data)
			os.system('touch %s'%(notes_db))
			data = (f"{GREEN}{notes_db} {GGREEN}has been created{DARK}.")
			echo_s(data)
		if self.failed_attempts == 5:
			data = (f"{RED}Database self-destruction beginning. . .")
			echo_f(data)
			os.remove(pass_db)
			data = (f"{RED}Removed{DARK}:{RRED} {pass_db}")
			echo_f(data)
			os.remove(notes_db)
			data = (f"{RED}Removed{DARK}:{RRED} {notes_db}")
			echo_f(data)
			os.remove(account_db)
			data = (f"{RED}Removed{DARK}:{RRED} {account_db}")
			echo_f(data)
			os.remove(user_db)
			data = (f"{RED}Removed{DARK}:{RRED} {user_db}")
			echo_f(data)
			data = (f"{RED}All databases have been removed{DARK}. {GGREEN}Rerun the script to setup databases again{DARK}.")
			echo_f(data)
			exit(0)
		data = (f"{GGREEN}Enter the database password to continue{DARK}.")
		echo_s(data)
		security = input(f"{RED}=={GREEN}>{INVISIBLE}  ");print(RESET,BOLD)
		account = 'mainkey'
		remove = len(account)
		with open(pass_db, 'r') as lol:
				database_entry = lol.readlines()
		j = len(database_entry)-1
		for i, line in enumerate(database_entry):
			if account in line.lower():
				recovered = line[remove+1:].rjust(32)
		decoded = self.cipher.decrypt(base64.b64decode(recovered)).decode('utf-8')
		unlock = decoded.strip()
		if security != unlock:
			self.failed_attempts += 1
			data = (f"{RED}Failed attempt{DARK}: {GGREEN}{self.failed_attempts}{DARK}. {RED}5 more failed attempts will result in database self-destruction{DARK}.")
			echo_f(data)
			self.login()
		data = (f"{GGREEN}Database unlocking successfull{DARK}, {GREEN}{user}{DARK}. {GGREEN}You can now access your entries{DARK}.")
		echo_s(data)
		self.init()
	def init(self):
		data = (f"{GGREEN}Create{DARK}, {GREEN}view {DARK}or {RRED}exit {DARK} ?")
		echo_s(data)
		task = input(f"{RED}=={GREEN}> ").lower()
		if 'c' in task:
			self.create_encryption()
		elif 'v' in task:
			self.decrypt()
		elif 'exit' in task:
			data = (f"{RRED}Exiting")
			echo_f(data)
		else:
			data = (f"{RRED}Exiting")
			echo_f(data)
	def create_encryption(self):
		""" Create Encrypion """	
		if self.Asymmetrical == 3:
			data = (f"{RED}Too many failed attempts{DARK}.{RED} Exiting{DARK}.")
			echo_f(data)
			exit(0)
		data = (f"{GGREEN}Account")
		echo_s(data)
		account = input(f"{RED}=={GREEN}> ")
		data = (f"{GGREEN}Username{DARK}/{GGREEN}email")
		echo_s(data)
		username = input(f"{RED}=={GREEN}> ")
		data = (f"{GGREEN}Notes")
		echo_s(data)
		notes = input(f"{RED}=={GREEN}> ")
		data = (f"{GGREEN}Password")
		echo_s(data)
		check = input(f"{RED}=={GREEN}>{INVISIBLE}  ").rjust(32);print(RESET,BOLD)
		data = (f"{RRED}Confirm password")
		echo_f(data)
		password_raw = input(f"{RED}=={GREEN}>{INVISIBLE}  ").rjust(32);print(RESET,BOLD)
		if check != password_raw:
			data = (f"{RED}Passwords don{DARK}'{RED}t match{DARK}. {RRED}Try again{DARK}.")
			echo_f(data)
			self.Asymmetrical += 1
			self.create_encryption()
		encoded = base64.b64encode(self.cipher.encrypt(password_raw)).decode('utf-8')
		entry = '%s %s'%(account, encoded)
		uname_entry = '%s %s'%(account,username)
		notes_entry = '%s %s'%(account,notes)
		with open(user_db, 'a') as n:
			n.write('{}\n'.format(uname_entry))
		with open(pass_db,'a') as o:
			o.write('{}\n'.format(entry))
		with open(account_db,'a') as out:
			out.write('{}\n'.format(account))
		with open(notes_db,'a') as l:
			l.write('{}\n'.format(notes_entry))
		data = (f"{GGREEN}Entry created{DARK}. {GGREEN}Account added to account database")
		echo_s(data)
		self.init()
	def decrypt(self):
		""" Decryption """
		data = (f"{GGREEN}Would you like to take a look at the accounts in the database {DARK}? {GGREEN}No passwords will be visible{DARK}.")
		echo_s(data)
		answer = input(f"{RED}=={GREEN}> ")
		if 'Y' in answer or 'y' in answer:
			with open(account_db,'r') as view:
				lines=view.readlines()
			for line in lines:
				sys.stdout.write(f"{DARK}[{GREEN}::{DARK}] {GGREEN}{line}")
				sleep(1)
		data = (f"{GGREEN}Account to decrypt {DARK}?")
		echo_s(data)
		account = input(f"{RED}=={GREEN}> ")
		remove = len(account)
		try:
			with open(notes_db, 'r') as mynotes:
				notes_entry = mynotes.readlines()
			h = len(notes_entry)-1
			for q, mynotes in enumerate(notes_entry):
				if account.lower() in mynotes.lower():
					note = mynotes[remove+1:].rjust(32)
			with open(user_db, 'r') as name:
				username_entry = name.readlines()
			f = len(username_entry)-1
			for p, name in enumerate(username_entry):
				if account.lower() in name.lower():
					uname = name[remove+1:].rjust(32)
			with open(pass_db, 'r') as lol:
				database_entry = lol.readlines()
			j = len(database_entry)-1
			for i, line in enumerate(database_entry):
				if account.lower() in line.lower():
					recovered = line[remove+1:].rjust(32)
			decoded = self.cipher.decrypt(base64.b64decode(recovered)).decode('utf-8')
			#print(f"{GGREEN}Account: {RRED}{account}\n{GGREEN}Username{DARK}: {RRED}{uname.strip()}\n{GGREEN}Password{DARK}: {RRED}{decoded.strip()}\n{GGREEN}Notes{DARK}: {RRED}{note.strip()}")
			headers = ["Account","Username","Password","Notes"]
			table = [[account,uname.strip(),decoded.strip(),note.strip()]]
			print(tabulate(table, headers, tablefmt="fancy_grid"))
		except:
			data = (f"{RED}No entry found")
			echo_f(data)
		self.init()
password_db()
