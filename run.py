
# run.py - the central script where the program will execute from.

# imports methods from jrnl_utils and other (unwritten) files...
# greets the user and displays some basic stats and other info before
# asking the user what they want to do next - this action will keep looping
# until the user quits the program.


from jrnl_utils import test

import colorama
from colorama import Fore, Back, Style

import datetime as dt
from datetime import datetime
import sys

colorama.init()

def get_input():
	"""ask the user to choose from a range of options,
	should be called again every time an action is complete."""
	given_input = input("\ninput your selection:  ")

	if given_input == 'quit':
		print('\nquitting micro-journal - see you next time!')
		print("")
		sys.exit()
	else:
		get_input()

def days_between(d1, d2):
	"""Return the difference between two dates for a
	range of different purposes"""
	d1 = datetime.strptime(d1, "%m/%d/%Y, %H:%M:%S")
	d2 = datetime.strptime(d2, "%m/%d/%Y, %H:%M:%S")
	return abs((d2 - d1).days)

def welcome_user():
	"""welcome the user back and display basic info (version number,
	outstanding tasks, upcoming deadlines, motivational quotes, etc) 
	and then ask the user to select an option."""

	# will need to be abstracted away into a seperate method
	version_file = open("version.txt", "r")
	version = version_file.read()
	todays_date = dt.datetime.now().strftime('%m/%d/%Y, %H:%M:%S')

	# will need to come out of database_utils when in place and return
	# the max (last) login date
	last_login = dt.datetime.now().strftime('%m/%d/%Y, %H:%M:%S')
	login_diff = days_between(last_login, todays_date)

	print("\nwelcome to " + Fore.CYAN + "micro-journal " + Style.RESET_ALL + "- version " + Fore.CYAN + f"{version} " + Style.RESET_ALL + f"- you've logged on at {todays_date}...")
	print(f"your last login date was {last_login} - {login_diff} days ago!\n")
	print("you can type 'help' for help or 'quit' to exit at any time.")
	return get_input()

if __name__ == '__main__':
	print(welcome_user())