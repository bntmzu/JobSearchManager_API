import requests
from typing import List, Dict
from abc import ABC, abstractmethod


class JobAPI(ABC):
    """
    Abstract base class for job API interfaces.
    """
    @abstractmethod
    def _connect_to_api(self) -> None:
        """
        Establishes a connection to the job API.
        This method should be implemented in subclasses to handle the specific API connection logic.
        """
        pass

    @abstractmethod
    def get_vacancies(self, search_query: str) -> List[Dict]:
        """
        Retrieves a list of vacancies based on the search query.

        :param search_query: The search query string used to find relevant job vacancies.
        :return: A list of dictionaries containing vacancy details.
        """
        pass


class HeadHunterAPI(JobAPI):
    """
    A concrete implementation of the JobAPI interface for interacting with the HeadHunter API.
    """
    def __init__(self):
        """
        Initializes the HeadHunterAPI with the base URL for API requests.
        """
        self._base_url = 'https://api.hh.ru/vacancies'

    def _connect_to_api(self) -> None:
        """
        Checks the availability of the HeadHunter API by making a request to the base URL.
        :raises ConnectionError: If the API is not accessible.
        """
        # checking API availability
        response = requests.get(self._base_url)
        if response.status_code != 200:
            raise ConnectionError(f"Failed to connect to HH API. Status code: {response.status_code}")

    def get_vacancies(self, search_query: str) -> List[Dict]:
        """
        Retrieves a list of vacancies from the HeadHunter API based on the provided search query.

        :param search_query: The search query string used to find relevant job vacancies.
        :return: A list of dictionaries containing vacancy details.
        :raises ConnectionError: If the API request fails.
        """
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
