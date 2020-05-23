#!/usr/bin python
#-*- encoding: utf-8 -*-
from Crypto.Cipher import AES;
import base64,re,os;
from time import sleep;
#Global Variables
path = '%s/.'% os.getenv("HOME")
pass_db='%spass.txt'%(path)
account_db='%saccounts.txt'%(path)
user_db='%susers.txt'%(path)
notes_db='%snotes.txt'%(path)
user = os.getenv('USER')
#Colors
bg_red='\033[48;5;9m'
red='\033[38;5;196m'
white='\033[38;5;15m'
green='\033[38;5;118m'
invisible='\033[08m'
reset='\033[0m'
bold='\033[01m'
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
			with open(pass_db,'r') as confirm:
				confirm.readlines()
		except:
			print  red + '['+white+'!'+red+'] '+red + 'No password database found in system, please enter the password you\'d like to use for the database'
			password_raw= raw_input(red+'=='+green+'> '+invisible).rjust(32);print reset + bold
			print white + '['+red+'!'+white+'] '+red + 'Confirm password'
			check = raw_input(red+'=='+green+'> '+invisible).rjust(32);print reset + bold
			if check != password_raw:
				print red + '['+white+'!'+red+'] '+red + 'Passwords don\'t match, try again'
				self.login()
			elif check == password_raw:
				encoded = base64.b64encode(self.cipher.encrypt(password_raw))
				os.system('echo mainkey %s > %s'%(encoded,pass_db))
				print white + '['+red+'!'+white+'] '+green + 'Database password successfully stored. Be sure to remember it. Failure to do so will result in self-destruction of the password database.'
		try:
			with open(account_db,'r') as confirm2:
				confirm2.readlines()
		except:
			print  red + '['+white+'!'+red+'] '+red + 'No account database found. Creating one now.'
			os.system('touch %s'%account_db)
			print '%s has been created'%(account_db)
		try: 
			with open(user_db, 'r') as confirm3:
				confirm3.readlines()
		except:
			print  red + '['+white+'!'+red+'] '+red + 'No user database found. Creating one now.'
			os.system('touch %s'%(user_db))
			print '%s has been created'%(user_db)
		try: 
			with open(notes_db, 'r') as confirm4:
				confirm4.readlines()
		except:
			print  red + '['+white+'!'+red+'] '+red + 'No notes database found. Creating one now.'
			os.system('touch %s'%(notes_db))
			print '%s has been created'%(notes_db)
		if self.failed_attempts == 5:
			print red + '['+white+'!'+red+'] '+red + 'Game over. You\'re not getting my passwords'
			os.system('rm -f %s'%pass_db)
		print white + '['+red+'!'+white+']'+green+' Enter the unlock passwd to continue'
		security = raw_input(red+'=='+green+'> '+invisible);print reset + bold
		account = 'mainkey'
		remove = len(account)
		with open(pass_db, 'r') as lol:
				database_entry = lol.readlines()
		j = len(database_entry)-1
		for i, line in enumerate(database_entry):
			if account in line.lower():
				recovered = line[remove+1:].rjust(32)
		decoded = self.cipher.decrypt(base64.b64decode(recovered))
		unlock = decoded.strip()
		if security != unlock:
			self.failed_attempts += 1
			print red + '['+white+'!'+red+'] '+red + 'Wrong attempt #'+green+'%s'%(self.failed_attempts)+red+'... 5 Wrong attempts will result in the database being destroyed.'
			self.login()
		print white + '['+green+'!'+white+']'+green+' Your password matches the database, %s, you can now access it.'%(user)
		self.init()
	def init(self):
		print white + '['+red+'!'+white+']'+green+' Create, view, or exit?'
		task = raw_input(red+'=='+green+'> ').lower()
		if 'c' in task:
			self.create_encryption()
		elif 'v' in task:
			self.decrypt()
		else:
			print red + '['+white+'!'+red+']'+red+' Exiting.'
	def create_encryption(self):
		""" Create Encrypion """	
		if self.Asymmetrical == 3:
			print red + '['+white+'!'+red+'] '+bg_red+'Too many failed attempts. Get some sleep and try again later.'+red+reset
			exit(0)
		print white + '['+red+'!'+white+'] '+green + 'Account'
		account = raw_input(red+'=='+green+'> ')
		print white + '['+red+'!'+white+'] '+green + 'Username'
		username = raw_input(red+'=='+green+'> ')
		print white + '['+red+'!'+white+'] '+green + 'Notes'
		notes = raw_input(red+'=='+green+'> ')
		print white + '['+red+'!'+white+'] '+green + 'Password'
		check = raw_input(red+'=='+green+'> '+invisible).rjust(32);print reset + bold
		print white + '['+red+'!'+white+'] '+red + 'Confirm password'
		password_raw= raw_input(red+'=='+green+'> '+invisible).rjust(32);print reset + bold
		if check != password_raw:
			print red + '['+white+'!'+red+'] '+red + 'Passwords don\'t match, try again'
			self.Asymmetrical += 1
			self.create_encryption()
		encoded = base64.b64encode(self.cipher.encrypt(password_raw))
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
		print white + '['+red+'!'+white+']'+green+' Entry created. Account added to %s'%(account_db)
		self.init()
	def decrypt(self):
		""" Decryption """
		print white + '['+red+'!'+white+']'+green+' Would you like to take a look at the accounts in your database? No passwords will be visible.'
		answer = raw_input(red+'=='+green+'> ')
		if 'Y' in answer or 'y' in answer:
			with open(account_db,'r') as view:
				lines=view.readlines()
			for line in lines:
				print line 
				sleep(1)
		print white + '['+red+'!'+white+'] '+green + 'Account to decrypt'
		account = raw_input(red+'=='+green+'> ')
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
			decoded = self.cipher.decrypt(base64.b64decode(recovered))
			print green + 'Account: %s\nUsername: %s\nPass: %s\nNotes %s' %(account,uname.strip(),decoded.strip(),note.strip())
		except:
			print red + '['+white+'!'+red+'] '+red + 'No entry found'
		self.init()
password_db()
