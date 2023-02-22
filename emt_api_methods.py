import json
import os.path
import emt_config as em
import requests
import pprint

pp = pprint.PrettyPrinter(indent=4)


def login():
    """
    Возвращает Jason Web Token (JWT)
    :return: JWT
    """
    server = em.SERVER + 'auth/auth/authenticate'
    payload = json.dumps(em.AUTH_JSON)
    headers = {"Content-Type": "application/json"}
    response = requests.request("POST", server, headers=headers, data=payload).json()
    # print(response)
    jwt = response["JsonWebToken"]["Value"]
    with open(em.JWT_STORE, 'w') as jwt_file:
        jwt_file.write(jwt)
    return jwt


def get_refresh_token():
    """
    Возвращает значение ключа RefreshToken
    :return:
    """
    server = em.SERVER + 'auth/auth/authenticate'
    auth = em.AUTH_JSON
    request = requests.post(server, json=auth).json()
    return request['RefreshToken']


def refresh_token():
    server = em.SERVER + 'auth/auth/rotateRefreshToken'
    token = get_refresh_token()
    payload = json.dumps({"RefreshToken": token})
    headers = {'refreshToken': token,
               'Content-Type': 'application/json'}
    response = requests.get(server, headers=headers, data=payload).json()
    print(response)
    return response["RefreshToken"]


def diag():
    # server = em.SERVER + 'core/Vehicle/realtime'
    server = em.SERVER + 'diagnostics/diagnostics/search/by_garage_numbers'
    if os.path.exists(em.VEHICLE_LIST):
        vehicle_list = open(em.VEHICLE_LIST, 'r').read().split()
    else:
        # vehicle_list = []
        print('Список ТС отсутствует.')
        return -1
    payload = json.dumps(vehicle_list)
    # print(payload)
    jwt = open(em.JWT_STORE)
    jwt = jwt.read()
    headers = {'Authorization': f'Bearer {jwt}', 'Content-Type': 'application/json'}
    response = requests.request("POST", server, headers=headers, data=payload).json()
    # pp.pprint(response)
    # Раскомментировать, если нужен полный текст запроса. Результат будет записан в файл diag.txt
    with open('diag.txt', 'w') as file:
        file.write(pp.pformat(response))
    return response


def coordinates_last_multiple(vehicle_list):
    server = em.SERVER + 'discreteServiceRead/Coordinates/last/multiple/by_garage_nums'
    # if os.path.exists(em.VEHICLE_LIST):
    #     vehicle_list = open(em.VEHICLE_LIST, 'r').read().split()
    # else:
    #     # vehicle_list = []
    #     print('Список ТС отсутствует.')
    #     return -1
    payload = json.dumps(vehicle_list)
    # print(payload)
    jwt = open(em.JWT_STORE)
    jwt = jwt.read()
    headers = {'Authorization': f'Bearer {jwt}', 'Content-Type': 'application/json'}
    response = requests.request("POST", server, headers=headers, data=payload).json()
    pp.pprint(response)



if __name__ == "__main__":
    pass
    # jwt = login()
    # print(jwt)
    # diag()
    # coordinates_last_multiple(['d912e320-17ed-4021-af6d-6e47044ac186'])
    coordinates_last_multiple(['8550'])
