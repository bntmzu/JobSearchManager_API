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
        # checking API availability
        response = requests.get(self._base_url)
        if response.status_code != 200:
            raise ConnectionError(f"Failed to connect to HH API. Status code: {response.status_code}")

    def get_vacancies(self, search_query: str) -> List[Dict]:
        # Connect to API (internal method)
        self._connect_to_api()

        # Request parameters
        params = {
            'text': search_query,
            'per_page': 20  # Retrieve 20 vacancies per page
        }

        # API request
        response = requests.get(self._base_url, params=params)

        # Check the response
        if response.status_code != 200:
            raise ConnectionError(f"Failed to retrieve vacancies. Status code: {response.status_code}")

        # Process the data
        data = response.json()
        return data['items']  # Return the list of vacancies
