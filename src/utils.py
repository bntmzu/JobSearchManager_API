
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


def parse_salary(salary: dict) -> tuple:
    """
    Parses the salary dictionary to extract minimum and maximum salary values along with the currency.

    :param salary: The salary dictionary from the API response.
    :return: A tuple with (salary_from, salary_to, currency).
             - salary_from: Minimum salary (int or None if not available).
             - salary_to: Maximum salary (int or None if not available).
             - currency: The currency of the salary (default is 'RUR').
    """
    if salary is None:
        return (None, None, "RUR")

    salary_from = salary.get('from')
    salary_to = salary.get('to')
    currency = salary.get('currency', 'RUR')

    return (salary_from, salary_to, currency)