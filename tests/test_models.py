import sys
import pytest
from src.models import Vacancy


def test_vacancy_creation():
    vac = Vacancy(
        title="Python Developer",
        url="https://hh.ru/vacancy/1",
        salary_from=100000,
        salary_to=150000,
        currency="RUR",
        description="Python, Django"
    )
    assert vac.title == "Python Developer"
    assert vac.salary_from == 100000
    assert vac.salary_to == 150000
    assert vac.currency == "RUR"
    assert vac.description == "Python, Django"


def test_salary_comparison():
    vac1 = Vacancy("Dev", "https://hh.ru/vacancy/1", 100000, 150000, "RUR", "Some desc")
    vac2 = Vacancy("Dev", "https://hh.ru/vacancy/2", 90000, 140000, "RUR", "Some desc")
    assert vac1 > vac2
    assert vac2 < vac1
