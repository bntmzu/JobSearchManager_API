class Vacancy:
    """
    Represents a job vacancy with details such as title, URL, salary range, currency, and description.
    """

    __slots__ = ['_title', '_url', '_salary_from', '_salary_to', '_currency', '_description']

    def __init__(self, title: str, url: str, salary_from: int, salary_to: int, currency: str, description: str):
        """
        Initializes a new instance of the Vacancy class.

        :param title: The title of the vacancy.
        :param url: The URL to the vacancy.
        :param salary_from: The minimum salary offered for the vacancy.
        :param salary_to: The maximum salary offered for the vacancy.
        :param currency: The currency in which the salary is offered.
        :param description: A brief description of the vacancy.
        """
        self._title = self._validate_title(title)
        self._url = self._validate_url(url)
        self._salary_from = self._validate_salary(salary_from)
        self._salary_to = self._validate_salary(salary_to)
        self._currency = self._validate_currency(currency)
        self._description = self._validate_description(description)

    @property
    def title(self) -> str:
        """Returns the title of the vacancy."""
        return self._title

    @property
    def url(self) -> str:
        """Returns the URL of the vacancy."""
        return self._url

    @property
    def salary_from(self) -> int:
        """Returns the minimum salary for the vacancy."""
        return self._salary_from

    @property
    def salary_to(self) -> int:
        """Returns the maximum salary for the vacancy."""
        return self._salary_to

    @property
    def currency(self) -> str:
        """Returns the currency in which the salary is offered."""
        return self._currency

    @property
    def description(self) -> str:
        """Returns the description of the vacancy."""
        return self._description

    def _validate_title(self, title: str) -> str:
        """
        Validates the title of the vacancy.

        :param title: The title to validate.
        :return: The validated title.
        :raises ValueError: If the title is empty.
        """
        if not title:
            raise ValueError("Title cannot be empty")
        return title

    def _validate_url(self, url: str) -> str:
        """
        Validates the URL of the vacancy.

        :param url: The URL to validate.
        :return: The validated URL.
        :raises ValueError: If the URL does not start with "http".
        """
        if not url.startswith("http"):
            raise ValueError("Invalid URL")
        return url

    def _validate_salary(self, salary: int) -> int:
        """
        Validates the salary value.

        :param salary: The salary value to validate.
        :return: The validated salary.
        :raises ValueError: If the salary is not an integer.
        """
        if salary is not None and not isinstance(salary, int):
            raise ValueError("Salary must be an integer")
        return salary

    def _validate_currency(self, currency: str) -> str:
        """
        Validates the currency of the salary.

        :param currency: The currency to validate.
        :return: The validated currency.
        :raises ValueError: If the currency is empty.
        """
        if not currency:
            raise ValueError("Currency cannot be empty")
        return currency

    def _validate_description(self, description: str) -> str:
        """
        Validates the description of the vacancy.

        :param description: The description to validate.
        :return: The validated description.
        :raises ValueError: If the description is empty.
        """
        if not description:
            raise ValueError("Description cannot be empty")
        return description

    def __lt__(self, other: 'Vacancy') -> bool:
        """
        Compares two vacancies based on their maximum salary.

        :param other: Another vacancy to compare with.
        :return: True if this vacancy's salary is less than the other vacancy's salary, False otherwise.
        """
        return self._get_salary_value() < other._get_salary_value()

    def __le__(self, other: 'Vacancy') -> bool:
        """
        Compares two vacancies to check if this vacancy's salary is less than or equal to the other vacancy's salary.

        :param other: Another vacancy to compare with.
        :return: True if this vacancy's salary is less than or equal to the other vacancy's salary, False otherwise.
        """
        return self._get_salary_value() <= other._get_salary_value()

    def __gt__(self, other: 'Vacancy') -> bool:
        """
        Compares two vacancies to check if this vacancy's salary is greater than the other vacancy's salary.

        :param other: Another vacancy to compare with.
        :return: True if this vacancy's salary is greater than the other vacancy's salary, False otherwise.
        """
        return self._get_salary_value() > other._get_salary_value()

    def __ge__(self, other: 'Vacancy') -> bool:
        """
        Compares two vacancies to check if this vacancy's salary is greater than or equal to the other vacancy's salary.

        :param other: Another vacancy to compare with.
        :return: True if this vacancy's salary is greater than or equal to the other vacancy's salary, False otherwise.
        """
        return self._get_salary_value() >= other._get_salary_value()

    def __eq__(self, other: 'Vacancy') -> bool:
        """
        Checks if two vacancies have the same salary.

        :param other: Another vacancy to compare with.
        :return: True if the salaries are equal, False otherwise.
        """
        return self._get_salary_value() == other._get_salary_value()

    def __ne__(self, other: 'Vacancy') -> bool:
        """
        Checks if two vacancies have different salaries.

        :param other: Another vacancy to compare with.
        :return: True if the salaries are not equal, False otherwise.
        """
        return self._get_salary_value() != other._get_salary_value()

    def _get_salary_value(self) -> int:
        """
        Returns the maximum salary value for comparison.
        If it is not specified, returns the minimum salary value.
        """
        if self._salary_to is not None:
            return self._salary_to
        elif self._salary_from is not None:
            return self._salary_from
        return 0
