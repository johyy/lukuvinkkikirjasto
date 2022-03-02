import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, '..', '.env'))
except FileNotFoundError:
    pass

DATABASE_FILENAME = 'sqlite:////' + str(dirname) + '/database.db'
DATABASE_FILE_PATH = os.path.join(dirname, 'database.db')

