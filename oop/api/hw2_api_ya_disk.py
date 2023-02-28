import requests
import os
from pprint import pprint


TOKEN = ""  # УДАЛИТЬ ПОСЛЕ ТЕСТА

class YandexDisk:
    
    def __init__(self, token) -> None:
        self.token = token
        self.yandex_url = 'https://cloud-api.yandex.net'
        
    def get_headers(self):
        """Метод возвращает словарь с заголовками"""
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
            }

    def get_files(self):
        """Метод возвращает список файлов в формате JSON"""
        full_path = f'{self.yandex_url}/v1/disk/resources/files'
        headers = self.get_headers()
        response = requests.get(url=full_path, headers=headers)

        response.raise_for_status()

        return response.json()
    
    def get_metainformations_resources(self, disk_resources_path):
        """Метод возвращает метаинформацию о ресурсе (файл, папка)"""
        full_path = f'{self.yandex_url}/v1/disk/resources'
        params = {'path': disk_resources_path}
        headers = self.get_headers()
        response = requests.get(url=full_path, params=params, headers=headers)

        response.raise_for_status()

        return response.json()
    
    def create_folder(self, disk_folder_path):
        """Метод создает папку"""
        full_path = f'{self.yandex_url}/v1/disk/resources'
        params = {'path': disk_folder_path}
        headers = self.get_headers()

        response = requests.put(url=full_path, params=params, headers=headers)

        response.raise_for_status()

        if response.status_code == 201:
            return print(f'Папка {disk_folder_path} создана.')
        
    def delete_resource(self, disk_resources_path, permanently=False):
        """
        Метод удаляет ресурс (файл, папку).
        Параметр permanently=True позволяет удалить ресурс не помещая в корзину
        """

        full_path = f'{self.yandex_url}/v1/disk/resources'
        params = {'path': disk_resources_path, 'permanently': permanently}
        headers = self.get_headers()
        response = requests.get(url=full_path, params=params, headers=headers)
        
        response.raise_for_status()

        if response.status_code == 204:
            return print(f'{disk_resources_path} удален.')

    def _get_upload_url(self, disk_file_path):
        """Метод возвращает путь для загрузки файла"""
        full_path = f'{self.yandex_url}/v1/disk/resources/upload'
        params = {'path': disk_file_path, 'overwrite': True}
        headers = self.get_headers()

        response = requests.get(url=full_path, params=params, headers=headers)

        return response.json()

    def upload_file(self, disk_file_path, computer_file_path):
        """Метод загружает файл на Яндекс.Диск"""
        href = self._get_upload_url(disk_file_path=disk_file_path).get('href', '')

        with open(computer_file_path, 'rb') as file:
            response = requests.put(url=href, data=file)
        
        response.raise_for_status()

        if response.status_code == 202:
            return print(f'Файл {computer_file_path} загружен.')


ya = YandexDisk(token=TOKEN)

# ya.create_folder(disk_folder_path='/netology/')
# pprint(ya.get_metainformations_resources(disk_resources_path='/'))

# current = os.getcwd()
# folder = '/oop/api/'
# file = 'test_29-02-2023.txt'

# upload_file_path = f'{current}{folder}{file}'

# ya.upload_file(
#     disk_file_path=f'/netology/{file}',
#     computer_file_path=upload_file_path
#     )
# pprint(ya.get_metainformations_resources(disk_resources_path='/netology/'))