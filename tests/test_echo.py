import requests
import pytest


@pytest.fixture(scope="module")
def base_url():
    return "https://postman-echo.com"

#GET запрос
def test_get_request(base_url):
    params = {"param1": "value1", "param2": "value2"}
    response = requests.get(f"{base_url}/get", params=params)

    #Проверка статуса ответа
    assert response.status_code == 200

    #Проверка наличия параметров в ответе
    json_response = response.json()
    assert json_response["args"] == params

#Post запрос
def test_post_request(base_url):
    data = {"key1": "value1", "key2": "value2"}
    response = requests.post(f"{base_url}/post", json=data)

    # Проверка статуса ответа
    assert response.status_code == 200

    # Проверка наличия данных в ответе
    json_response = response.json()
    assert json_response["json"] == data

#PUT запрос
def test_put_request(base_url):
    data = {"updated_key": "new_value"}
    response = requests.put(f"{base_url}/put", json=data)

    #Проверка статуса ответа
    assert response.status_code == 200

    #Проверка наличия обновленных данных в ответе
    json_response = response.json()
    assert json_response["json"] == data

#DELETE запрос
def test_delete_request(base_url):
    response = requests.delete(f"{base_url}/delete")

    # Проверка статуса ответа
    assert response.status_code == 200

def test_patch_request(base_url):
    # Подготовка данных для запроса
    patch_data = {"title": "Updated Title"}
    headers = {"Content-Type": "application/json"}

    # Отправка PATCH-запроса
    response = requests.patch(
        url=f"{base_url}/patch",
        json=patch_data,
        headers=headers
    )

    # Проверка статуса ответа
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    # Проверка содержимого ответа
    response_data = response.json()
    assert response_data["json"] == patch_data, f"Response data does not match sent data."
