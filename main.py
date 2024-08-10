from src.api import HeadHunterAPI
from src.models import Vacancy
from src.storage import JSONFileStorage
from src.utils import validate_url, parse_salary


def search_and_add_vacancies(hh_api, storage):
    search_query = input("Enter search query for vacancies: ")
    try:
        vacancies_data = hh_api.get_vacancies(search_query)
        for vac in vacancies_data:
            title = vac['name']
            url = vac['alternate_url']

            # Валидация URL
            try:
                validated_url = validate_url(url)
            except ValueError as e:
                print(f"Invalid URL for vacancy '{title}': {e}")
                continue

            salary_str = parse_salary(vac.get('salary'))

            description = vac['snippet']['requirement'] or "No description available"

            vacancy = Vacancy(title, validated_url, salary_str, description)
            storage.write_data([{
                'title': vacancy.title,
                'url': vacancy.url,
                'salary': vacancy.salary,
                'description': vacancy.description
            }])
        print(f"{len(vacancies_data)} vacancies added successfully.")
    except Exception as e:
        print(f"Error occurred: {e}")


def view_saved_vacancies(storage):
    vacancies = storage.read_data()
    if not vacancies:
        print("No vacancies saved yet.")
    else:
        for idx, vac in enumerate(vacancies, start=1):
            print(f"\nVacancy {idx}:")
            print(f"Title: {vac['title']}")
            print(f"URL: {vac['url']}")
            print(f"Salary: {vac['salary']}")
            print(f"Description: {vac['description']}")
            print("-" * 40)


def user_interaction():
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
