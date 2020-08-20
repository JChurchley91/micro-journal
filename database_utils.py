
# database_utils.py - imported into the main run.py script at runtime.

# contains all methods and utilities that relate to saving or retrieving
# data from the sqlite database along with other smaller utilities.

import os.path
import sqlite3 
import datetime as dt

from datetime import datetime
from sqlite3 import Error
from misc_utils import return_today

def initialize_database():
	"""initialize and return a sqlite database that will appear in the user's
	directory - will only be initalized once if it does not already exist.
	"""

	if os.path.isfile('jrnl_database.db'):
		conn = sqlite3.connect('jrnl_database.db')
		cursor = conn.cursor()
		return conn

	else:

		try:
			conn = sqlite3.connect('jrnl_database.db')
			cursor = conn.cursor()
			print('\njrnl_database.db initalized - happy journaling!')
			return conn
		except:
			print(Error)

def store_username():
	"""Prompt the user for a username if username table is empty
	and store the username within a sqlite table"""

	create_statement = """
	CREATE TABLE IF NOT EXISTS user_name
	(
	user_id INTEGER PRIMARY KEY AUTOINCREMENT,
	user_name text 
	);"""

	cursor.execute(create_statement)

	cursor.execute('SELECT * FROM user_name')
	row = cursor.fetchone()

	if row == None:
		given_username = input("\nit looks like it's your first time logging in - what's your name? ")
		insert_statement = f"""
		INSERT INTO user_name (user_name) VALUES('{given_username}')
		"""
		cursor.execute(insert_statement)
		conn.commit()
	else:
		pass

def store_login_date():
	"""store the user's login date in user_logins table
	in sqlite database"""

	today = return_today()

	create_statement = """
	CREATE TABLE IF NOT EXISTS user_logins
	(
	login_id INTEGER PRIMARY KEY AUTOINCREMENT,
	login_date text
	);"""

	cursor.execute(create_statement)

	insert_statement = f"""
	INSERT INTO user_logins (login_date) VALUES ('{today}')
	"""
	cursor.execute(insert_statement)
	conn.commit()

def return_name():
	"""return the user's name stored in user_name table 
	in sqlite database"""

	conn = initialize_database()
	cursor = conn.cursor()


	cursor.execute('SELECT user_name from user_name')
	name = cursor.fetchone()
	return name[0]

def return_last_login():
	"""Return the date the user last logged into the journal
	by returning the max date logged in table login_dates"""

	conn = initialize_database()
	cursor = conn.cursor()

	cursor.execute('SELECT max(login_date) from user_logins')
	last_login = cursor.fetchone()
	return last_login[0]