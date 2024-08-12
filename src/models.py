class Vacancy:
    __slots__ = ['_title', '_url', '_salary_from', '_salary_to', '_currency', '_description']

    def __init__(self, title: str, url: str, salary_from: int, salary_to: int, currency: str, description: str):
        self._title = self._validate_title(title)
        self._url = self._validate_url(url)
        self._salary_from = self._validate_salary(salary_from)
        self._salary_to = self._validate_salary(salary_to)
        self._currency = self._validate_currency(currency)
        self._description = self._validate_description(description)

    @property
    def title(self) -> str:
        return self._title

    @property
    def url(self) -> str:
        return self._url

    @property
    def salary_from(self) -> int:
        return self._salary_from

    @property
    def salary_to(self) -> int:
        return self._salary_to

    @property
    def currency(self) -> str:
        return self._currency

    @property
    def description(self) -> str:
        return self._description

    def _validate_title(self, title: str) -> str:
        if not title:
            raise ValueError("Title cannot be empty")
        return title

    def _validate_url(self, url: str) -> str:
        if not url.startswith("http"):
            raise ValueError("Invalid URL")
        return url

    def _validate_salary(self, salary: int) -> int:
        if salary is not None and not isinstance(salary, int):
            raise ValueError("Salary must be an integer")
        return salary

    def _validate_currency(self, currency: str) -> str:
        if not currency:
            raise ValueError("Currency cannot be empty")
        return currency

    def _validate_description(self, description: str) -> str:
        if not description:
            raise ValueError("Description cannot be empty")
        return description

    def __lt__(self, other: 'Vacancy') -> bool:
        return self._get_salary_value() < other._get_salary_value()

    def __le__(self, other: 'Vacancy') -> bool:
        return self._get_salary_value() <= other._get_salary_value()

    def __gt__(self, other: 'Vacancy') -> bool:
        return self._get_salary_value() > other._get_salary_value()

    def __ge__(self, other: 'Vacancy') -> bool:
        return self._get_salary_value() >= other._get_salary_value()

    def __eq__(self, other: 'Vacancy') -> bool:
        return self._get_salary_value() == other._get_salary_value()

    def __ne__(self, other: 'Vacancy') -> bool:
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
