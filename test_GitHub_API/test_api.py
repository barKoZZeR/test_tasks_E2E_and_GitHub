import os
import requests
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv('USERNAME')
TOKEN = os.getenv('TOKEN')
REPOSITORY_NAME = os.getenv('REPOSITORY_NAME')

HEADERS = {
    'Authorization': f'token {TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

BASE_URL = "https://api.github.com"

def create_repository():
    url = f"{BASE_URL}/user/repos"
    data = {
        "name": REPOSITORY_NAME,
        "auto_init": True,
        "private": False
    }
    response = requests.post(url, headers=HEADERS, json=data)
    if response.status_code == 201:
        print(f"Репозиторий '{REPOSITORY_NAME}' создан успешно.")
    else:
        print(f"Репозиторий уже существует или возникла ошибка при его создании: {response.json()}")

def check_repository():
    url = f"{BASE_URL}/repos/{USERNAME}/{REPOSITORY_NAME}"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        print(f"Репозиторий '{REPOSITORY_NAME}' найден.")
    else:
        print(f"Репозиторий '{REPOSITORY_NAME}' не найден.")

def delete_repository():
    url = f"{BASE_URL}/repos/{USERNAME}/{REPOSITORY_NAME}"
    response = requests.delete(url, headers=HEADERS)
    if response.status_code == 204:
        print(f"Репозиторий '{REPOSITORY_NAME}' успешно удалён.")
    else:
        print(f"Возникла ошибка при попытке удалить репозиторий: {response.json()}")

if __name__ == "__main__":
    create_repository()
    check_repository()
    delete_repository()