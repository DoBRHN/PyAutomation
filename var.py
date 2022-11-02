import os

from datetime import date, datetime

CURR_DIR = os.path.dirname(__file__)
DATA = os.path.join(CURR_DIR, 'data')

is_exist = os.path.exists(DATA)
today = date.today()
start_time = datetime.now()
