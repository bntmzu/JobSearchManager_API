
def validate_url(url: str) -> str:
    """
    Validates if the provided URL is correctly formatted.

    :param url: The URL string to validate.
    :return: The validated URL.
    :raises ValueError: If the URL is invalid.
    """
    if not url.startswith("http"):
        raise ValueError("Invalid URL")
    return url


def parse_salary(salary: dict) -> str:
    if salary is None:
        return "Salary not specified"

    salary_from = salary.get('from')
    salary_to = salary.get('to')
    currency = salary.get('currency', 'RUR')

    if salary_from and salary_to:
        return f"от {salary_from} до {salary_to} {currency}"
    elif salary_from:
        return f"от {salary_from} {currency}"
    elif salary_to:
        return f"до {salary_to} {currency}"
    else:
        return "Salary not specified"
