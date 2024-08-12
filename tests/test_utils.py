import sys
import pytest
from src.utils import validate_url, parse_salary


def test_validate_url():
    valid_url = "https://hh.ru/vacancy/1"
    invalid_url = "htp://hh.ru/vacancy/1"

    assert validate_url(valid_url) == valid_url

    with pytest.raises(ValueError):
        validate_url(invalid_url)


def test_parse_salary():
    salary_dict = {'from': 100000, 'to': 150000, 'currency': 'RUR'}
    salary_from, salary_to, currency = parse_salary(salary_dict)

    assert salary_from == 100000
    assert salary_to == 150000
    assert currency == "RUR"

    salary_dict_partial = {'from': 100000, 'currency': 'RUR'}
    salary_from, salary_to, currency = parse_salary(salary_dict_partial)

    assert salary_from == 100000
    assert salary_to is None
    assert currency == "RUR"
