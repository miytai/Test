import os
import requests
from dotenv import load_dotenv

# Загружаем переменные окружения из файла .env
load_dotenv('setting.env')

# Получаем значения из переменных окружения
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
GITHUB_USERNAME = os.getenv('GITHUB_USERNAME')
repo_name = os.getenv('REPO_NAME')

# Вывод переменных для проверки
print('GITHUB_TOKEN:', GITHUB_TOKEN)
print('GITHUB_USERNAME:', GITHUB_USERNAME)
print('REPO_NAME:', repo_name)

headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}


# Функция для создания нового репозитория
def create_repository(repo_name):
    url = 'https://api.github.com/user/repos'
    json_data = {
        'name': repo_name,
        'private': False  # Публикация репозитория
    }
    response = requests.post(url, headers=headers, json=json_data)

    if response.status_code == 201:
        print(f'Репозиторий "{repo_name}" успешно создан.')
    else:
        print(f'Ошибка при создании репозитория: {response.content}')
        return None

    return repo_name


# Функция для проверки существования репозитория
def check_repository(repo_name):
    url = f'https://api.github.com/users/{GITHUB_USERNAME}/repos'
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        repos = response.json()
        repo_names = [repo['name'] for repo in repos]

        if repo_name in repo_names:
            print(f'Репозиторий "{repo_name}" существует в списке репозиториев.')
            return True
        else:
            print(f'Репозиторий "{repo_name}" не найден.')
            return False
    else:
        print(f'Ошибка при получении списка репозиториев: {response.content}')
        return False


# Функция для удаления репозитория
def delete_repository(repo_name):
    url = f'https://api.github.com/repos/{GITHUB_USERNAME}/{repo_name}'
    response = requests.delete(url, headers=headers)

    if response.status_code == 204:
        print(f'Репозиторий "{repo_name}" успешно удален.')
    else:
        print(f'Ошибка при удалении репозитория: {response.content}')


# Основной процесс
if __name__ == '__main__':
    # Создание репозитория
    repo_name_created = create_repository(repo_name)

    # Проверка, что репозиторий был создан
    if repo_name_created:
        if check_repository(repo_name_created):
            # Удаление репозитория
            delete_repository(repo_name_created)