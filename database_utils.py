
# database_utils.py - imported into the main run.py script at runtime.

# contains all methods and utilities that relate to saving or retrieving
# data from the sqlite database along with other smaller utilities.

import os.path
import sqlite3 
import datetime as dt

from datetime import datetime
from sqlite3 import Error

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
			print('jrnl_database.db initalized - happy journaling!')
			return conn
		except:
			print(Error)

def return_last_login():
	"""Return the date the user last logged into the journal
	by returning the max date logged in table login_dates"""

	#PLACEHOLDER
	last_login = dt.datetime.now().strftime('%m/%d/%Y, %H:%M:%S')
	return last_login