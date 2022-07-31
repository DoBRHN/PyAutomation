from pathlib import Path
from datetime import date,datetime

TODAY = date.today()
START_TIME = datetime.now()

CURR_DIR = Path().absolute()
DATA_DIR = CURR_DIR / 'Sauvegarde'
SAVE_DIR = DATA_DIR / f'{TODAY}'
README_FILE = SAVE_DIR / 'readme.txt'

CISCO_CONF = 'show run'
COMWARE_CONF = 'display current-configuration'