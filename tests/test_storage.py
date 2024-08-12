import sys
import os
import pytest
from src.storage import JSONFileStorage


def test_write_and_read_data():
    storage = JSONFileStorage('test_vacancies.json')
    vacancy_data = [{
        'title': 'Python Developer',
        'url': 'https://hh.ru/vacancy/1',
        'salary_from': 100000,
        'salary_to': 150000,
        'currency': 'RUR',
        'description': 'Python, Django'
    }]
    storage.write_data(vacancy_data)
    read_data = storage.read_data()
    assert len(read_data) == 1
    assert read_data[0]['title'] == 'Python Developer'

    # Cleanup
    os.remove('test_vacancies.json')
