import sys
import pytest
import requests_mock
from src.api import HeadHunterAPI

def test_connect_to_api_success():
    api = HeadHunterAPI()
    # Mocking requests.get to simulate API response
    with requests_mock.Mocker() as m:
        m.get(api._base_url, status_code=200)
        assert api._connect_to_api() is None

def test_connect_to_api_failure():
    api = HeadHunterAPI()
    with requests_mock.Mocker() as m:
        m.get(api._base_url, status_code=500)
        with pytest.raises(ConnectionError):
            api._connect_to_api()

def test_get_vacancies():
    api = HeadHunterAPI()
    sample_response = {"items": [{"name": "Developer", "alternate_url": "https://hh.ru/vacancy/1"}]}
    with requests_mock.Mocker() as m:
        m.get(api._base_url, json=sample_response)
        vacancies = api.get_vacancies("Developer")
        assert len(vacancies) == 1
        assert vacancies[0]['name'] == "Developer"

