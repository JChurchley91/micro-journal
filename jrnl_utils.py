
# jrnl_utils.py - imported into the main run.py script at runtime.

# contains all methods and utilities that relate to journaling - logging entries, setting tags,
# showing outstanding logs, and so on...

import datetime
import sys

def get_input():
	"""ask the user to choose from a range of options,
	should be called again every time an action is complete."""

	given_input = input("\ninput your selection: ")

	if given_input == 'quit':
		print('\nquitting micro-journal - see you next time!')
		print("")
		sys.exit()
	else:
		get_input()

def create_log():
	"""create a daily/weekly/monthly log and save the log into
	the user's sqlite database"""