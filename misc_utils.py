
# misc_utils.py - imported into the main run.py script at runtime.

# contains all methods and utilities that don't really belong anywhere...

import datetime as dt

from datetime import datetime

def return_version():
	"""return the current version number by reading the 
	version.txt file"""
	version_file = open("version.txt", "r")
	version = version_file.read()
	return version

def return_today():
	"""return todays date to be used for a variery of things..."""
	todays_date = dt.datetime.now().strftime('%m/%d/%Y, %H:%M:%S')
	return todays_date

def days_between(d1, d2):
	"""Return the difference between two dates for a
	range of different purposes"""

	d1 = datetime.strptime(d1, "%m/%d/%Y, %H:%M:%S")
	d2 = datetime.strptime(d2, "%m/%d/%Y, %H:%M:%S")
	return abs((d2 - d1).days)