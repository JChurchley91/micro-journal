
# run.py - the central script where the program will execute from.

# imports methods from jrnl_utils and other (unwritten) files...
# greets the user and displays some basic stats and other info before
# asking the user what they want to do next - this action will keep looping
# until the user quits the program.

from jrnl_utils import create_log, get_input
from database_utils import initialize_database, store_username, store_login_date, return_last_login, return_name
from misc_utils import return_version, return_today, days_between

conn = initialize_database()
cursor = conn.cursor()

version = return_version()
today = return_today()
last_login = return_last_login()
login_diff = days_between(last_login, today)
name = return_name()


def welcome_user(*args):
	"""welcome the user back and display basic info (version number,
	outstanding tasks, upcoming deadlines, motivational quotes, etc) 
	and then ask the user to select an option."""

	print(f"\nwelcome to micro-journal - version {version} - you've logged on at {today}...")
	print(f"\nyour last login date was {last_login} - {login_diff} days ago.")
	print(f"\ndon't forget, you can type 'help' for help or 'quit' to exit at any time.")
	print(f"\nhappy journalling, {name}!")

	return get_input()
	

if __name__ == '__main__':
	print(welcome_user(conn, cursor, version, today, last_login, login_diff, name))