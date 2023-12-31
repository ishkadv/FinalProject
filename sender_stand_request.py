import configuration
import requests
import data

# Функция создания нового пользователя
def post_new_user():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=data.user_body,
                         headers=data.headers)

# Функция создания набора внутри конкретного пользователя
def post_new_client_kit(body):
    if data.AUTH_TOKEN == "":
        response = post_new_user()
        data.AUTH_TOKEN = response.json()['authToken']
    headers_kits = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + data.AUTH_TOKEN
    }
    return requests.post(configuration.URL_SERVICE + configuration.MAIN_KITS_PATH,
                         json=body,
                         headers=headers_kits)


# Функция изменения имени набора
def post_new_kit(name):
    body = data.kit_body.copy()
    body["name"]=name

    return body
