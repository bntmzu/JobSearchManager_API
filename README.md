# JobSearchManager API

JobSearchManager API is a Python-based application that interacts with the HeadHunter API to search for job vacancies, filter and sort them based on user-defined criteria, and save the results in a JSON file. The application is modular, with separate components for interacting with the API, handling job vacancies, and managing file storage.

## Features

- **Search for Vacancies**: Connects to the HeadHunter API to retrieve job vacancies based on a search query.
- **Filter and Sort**: Filters vacancies by keywords and salary range, and sorts them by salary.
- **Save and View**: Saves the filtered vacancies in a JSON file and allows users to view the saved vacancies.
- **Modular Design**: The project is organized into modules for API interaction, vacancy handling, and file storage.
- **Test Coverage**: The project includes unit tests with 88% code coverage.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/username/JobSearchManager_API.git
   cd JobSearchManager_API
2. **Create and activate a virtual environment:**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows, use .venv\Scripts\activate
3. **Install dependencies:**
   
   ```bash
   poetry install

## Usage
1. **Run the application:**

   ```bash
   python main.py
2. **Search for Vacancies:**
   ```bash
   1. Enter a search query (e.g., `"Data Analyst"`).
   2. Enter the number of top vacancies to display: Specify how many top vacancies you want to see.
   3. Enter keywords for filtering vacancies: Provide keywords to filter the vacancies.
   4. Enter a salary range (e.g., `"50000-150000"`).
4. **View Saved Vacancies:**
   Choose the option to view saved vacancies from the menu.
   
## Running Tests

  pytest --cov=src tests/

This will show you the test results and the code coverage.

## Project Structure
The project is organized as follows:
```bash
JobSearchManager_API/
│
├── data/
│   └── vacancies.json          # JSON file to store saved vacancies
│
├── src/
│   ├── api.py                  # Module for interacting with the HeadHunter API
│   ├── models.py               # Module for handling job vacancy objects
│   ├── storage.py              # Module for managing file storage
│   └── utils.py                # Module for utility functions
│
├── tests/
│   ├── test_api.py             # Unit tests for the API module
│   ├── test_models.py          # Unit tests for the models module
│   ├── test_storage.py         # Unit tests for the storage module
│   └── test_utils.py           # Unit tests for the utility functions
│
├── .gitignore                  # Git ignore file
├── pyproject.toml              # Project configuration file
├── README.md                   # Project README file
└── main.py                     # Main entry point for the application
