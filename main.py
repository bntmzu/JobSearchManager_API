from src.api import HeadHunterAPI
from src.models import Vacancy
from src.storage import JSONFileStorage
from src.utils import validate_url, parse_salary


def filter_vacancies(vacancies, keywords):
    """Filters vacancies by keywords."""
    return [
        vac for vac in vacancies
        if any(keyword.lower() in vac.description.lower() for keyword in keywords)
    ]


def get_vacancies_by_salary(vacancies, salary_range):
    """Filters vacancies by salary range."""
    min_salary, max_salary = map(int, salary_range.split('-'))
    return [
        vac for vac in vacancies
        if
                (vac.salary_from is not None and vac.salary_from >= min_salary) and
                (vac.salary_to is not None and vac.salary_to <= max_salary)

    ]


def sort_vacancies(vacancies):
    """Sorts vacancies by descending salary."""
    return sorted(vacancies, key=lambda vac: vac.salary_to or vac.salary_from or 0, reverse=True)


def get_top_vacancies(vacancies, top_n):
    """Gets the top N vacancies."""
    return vacancies[:top_n]


def print_vacancies(vacancies):
    """Prints vacancies to the screen."""
    for idx, vac in enumerate(vacancies, start=1):
        print(f"\nVacancy {idx}:")
        print(f"Title: {vac.title}")
        print(f"URL: {vac.url}")
        if vac.salary_from and vac.salary_to:
            salary_display = f"from {vac.salary_from} to {vac.salary_to} {vac.currency}"
        elif vac.salary_from:
            salary_display = f"from {vac.salary_from} {vac.currency}"
        elif vac.salary_to:
            salary_display = f"up to {vac.salary_to} {vac.currency}"
        else:
            salary_display = "Salary not specified"
        print(f"Salary: {salary_display}")
        print(f"Description: {vac.description}")
        print("-" * 40)


def search_and_add_vacancies(hh_api, storage):
    """Searches and adds new vacancies from HeadHunter."""
    search_query = input("Enter search query: ")
    hh_vacancies = hh_api.get_vacancies(search_query)
    vacancies_list = []

    for vac in hh_vacancies:
        try:
            validated_url = validate_url(vac['alternate_url'])
            salary_from, salary_to, currency = parse_salary(vac['salary'])
            print(f"Parsed salary: from {salary_from} to {salary_to} {currency}")  # Отладка зарплаты
            vacancy = Vacancy(
                title=vac['name'],
                url=validated_url,
                salary_from=salary_from,
                salary_to=salary_to,
                currency=currency,
                description=vac['snippet']['requirement'] or "No description available"
            )
            vacancies_list.append(vacancy)
        except ValueError as e:
            print(f"Invalid URL for vacancy '{vac['name']}': {e}")
            continue

    # Save vacancies
    for vacancy in vacancies_list:
        storage.write_data([{
            'title': vacancy.title,
            'url': vacancy.url,
            'salary_from': vacancy.salary_from,
            'salary_to': vacancy.salary_to,
            'currency': vacancy.currency,
            'description': vacancy.description
        }])

    # Debugging: Check if vacancies_list is populated
    if not vacancies_list:
        print("No vacancies found or saved.")
        return

    # Top N vacancies by salary
    top_n = int(input("Enter the number of top vacancies to display: "))

    # Filter by keywords
    filter_words = input("Enter keywords for filtering vacancies: ").split()

    # Filter by salary range
    salary_range = input("Enter salary range (e.g., 100000 - 150000): ")

    # Debugging: Check if filtering works
    filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
    if not filtered_vacancies:
        print("No vacancies matched the filter keywords.")
        return

    print("Vacancies after keyword filtering:")
    for vac in filtered_vacancies:
        print(f"Title: {vac.title}, Salary: from {vac.salary_from} to {vac.salary_to} ")

    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
    if not ranged_vacancies:
        print("No vacancies matched the salary range.")
        return

    sorted_vacancies = sort_vacancies(ranged_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)

    # Print vacancies to the screen
    print_vacancies(top_vacancies)


def view_saved_vacancies(storage):
    """Views saved vacancies from JSON storage."""
    vacancies_data = storage.read_data()
    vacancies = [
        Vacancy(
            title=vac['title'],
            url=validate_url(vac['url']),
            salary_from=vac.get('salary_from'),
            salary_to=vac.get('salary_to'),
            currency=vac.get('currency', '-'),
            description=vac['description']
        )
        for vac in vacancies_data
    ]

    if not vacancies:
        print("No vacancies saved yet.")
    else:
        print_vacancies(vacancies)


def user_interaction():
    """Main interaction loop for the user."""
    storage = JSONFileStorage('data/vacancies.json')
    hh_api = HeadHunterAPI()

    while True:
        print("\n1. Search and add new vacancies from HH.ru")
        print("2. View saved vacancies")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            search_and_add_vacancies(hh_api, storage)

        elif choice == '2':
            view_saved_vacancies(storage)

        elif choice == '3':
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    user_interaction()
