"""
Опрос ТС из ЕМТ по списку из файла. Запись ошибок оборудования на ТС в файл
"""

import os
import emt_config as em
import emt_api_methods as api
import datetime
import pprint


pp = pprint.PrettyPrinter(indent=4)

jwt = api.login()
diag = api.diag()

today = datetime.datetime.now().date()
now = datetime.datetime.now().time()
now = now.strftime('%H-%M')

if not os.path.exists(em.ERRORS_DIR):
    os.mkdir(em.ERRORS_DIR)

file_name = f'{today}_{now}_{em.ERRORS_FILE}'
file_name = os.path.join(em.ERRORS_DIR, file_name)

if os.path.exists(file_name):
    os.remove(file_name)

with open(file_name, 'a') as file:
    try:
        diag['Diagnostics']
    except KeyError:
        print('Раздел диагностики не найден')

    for vehicle in diag['Diagnostics']:
        try:
            if vehicle['Errors']:
                text = '\nТС: {}, категории устройств: {}\n'.format(vehicle['VehicleName'], vehicle['Errors'])

            print(text)
            file.write(text )

            for error in vehicle['ErrorsDescription']:
                text = f'{error}\n'
                print(text)
                file.write(text)
            file.write('\n')

        except KeyError:
            pass

print(f'\nРезультат диагностики записан в файл {file_name}')
