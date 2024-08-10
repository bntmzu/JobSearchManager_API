import requests
from typing import List, Dict
from abc import ABC, abstractmethod


class JobAPI(ABC):
    @abstractmethod
    def _connect_to_api(self) -> None:
        pass

    @abstractmethod
    def get_vacancies(self, search_query: str) -> List[Dict]:
        pass


class HeadHunterAPI(JobAPI):
    def __init__(self):
        self._base_url = 'https://api.hh.ru/vacancies'

    def _connect_to_api(self) -> None:
        # Пример подключения (проверка доступности API)
        response = requests.get(self._base_url)
        if response.status_code != 200:
            raise ConnectionError(f"Failed to connect to HH API. Status code: {response.status_code}")

    def get_vacancies(self, search_query: str) -> List[Dict]:
        # Подключение к API (внутренний метод)
        self._connect_to_api()

        # Параметры запроса
        params = {
            'text': search_query,
            'per_page': 10  # Получаем 10 вакансий на страницу
        }

        # Запрос к API
        response = requests.get(self._base_url, params=params)

        # Проверка ответа
        if response.status_code != 200:
            raise ConnectionError(f"Failed to retrieve vacancies. Status code: {response.status_code}")

        # Обработка данных
        data = response.json()
        return data['items']  # Возвращаем список вакансий
