import os
import emt_config as em
import auth
import datetime

jwt = auth.login()
# print(jwt)
diag = auth.diag()
# print(diag)


now = datetime.datetime.now().date()

if not os.path.exists(em.ERRORS_DIR):
    os.mkdir(em.ERRORS_DIR)

file_name = f'{now}_{em.ERRORS_FILE}'
file_name = os.path.join(em.ERRORS_DIR, file_name)

with open(file_name, 'w') as file:
    for vehicle in diag:
        if vehicle['BrokenDevices']:
            text = '{} {} {}\n'.format(vehicle['InternalNumber'], vehicle['BrokenDevices'], vehicle['Errors'])
            print(text)
        file.write(text)
