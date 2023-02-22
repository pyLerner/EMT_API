import os
from dotenv import load_dotenv

load_dotenv()

SERVER = os.getenv('SERVER')

AUTH_JSON = {
                "login": os.getenv('LOGIN'),
                "password": os.getenv('PASSWORD')
             }

JWT_STORE = os.getenv('JWT_STORE')


VEHICLE_LIST = 'vehicles.txt'
DIAG_RESULT = 'diag.txt'

ERRORS_DIR = 'Errors'
ERRORS_FILE = 'errors.txt'