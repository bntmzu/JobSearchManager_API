class Vacancy:
    __slots__ = ['_title', '_url', '_salary', '_description']

    def __init__(self, title: str, url: str, salary: str, description: str):
        self._title = self._validate_title(title)
        self._url = self._validate_url(url)
        self._salary = self._validate_salary(salary)
        self._description = self._validate_description(description)

    @property
    def title(self) -> str:
        return self._title

    @property
    def url(self) -> str:
        return self._url

    @property
    def salary(self) -> str:
        return self._salary

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

    def _validate_salary(self, salary: str) -> str:
        return salary

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
        parts = self._salary.replace('руб', '').replace(' ', '').split('до')
        if len(parts) == 2:
            return int(parts[1])
        elif len(parts) == 1:
            return int(parts[0])
        return 0
