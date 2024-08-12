import json
import os
from abc import ABC, abstractmethod
from typing import List, Dict


class FileStorage(ABC):
    """
    Abstract base class for file storage operations.
    """

    @abstractmethod
    def read_data(self) -> List[Dict]:
        """
        Reads data from the storage file.
        :return: A list of dictionaries containing the stored data.
        """
        pass

    @abstractmethod
    def write_data(self, data: List[Dict]) -> None:
        """
        Writes data to the storage file.
        :param data: A list of dictionaries containing the data to be written.
        """
        pass

    @abstractmethod
    def delete_data(self, data: Dict) -> None:
        """
        Deletes specific data from the storage file.
        :param data: A dictionary containing the data to be deleted.
        """
        pass


class JSONFileStorage(FileStorage):
    """
    Concrete implementation of the FileStorage class for handling JSON files.
    """

    def __init__(self, filename: str = "data/vacancies.json"):
        """
        Initializes the JSONFileStorage with a specific file name.
        :param filename: The name of the file to be used for storing data. Defaults to 'data/vacancies.json'.
        """
        self._filename = filename

    def read_data(self) -> List[Dict]:
        """
        Reads data from a JSON file. If the file does not exist, it returns an empty list.
        :return: A list of dictionaries containing the data from the JSON file.
        """
        if not os.path.exists(self._filename):
            return []
        with open(self._filename, 'r', encoding='utf-8') as file:
            return json.load(file)

    def write_data(self, data: List[Dict]) -> None:
        """
        Writes data to a JSON file. If the data already exists, it is not duplicated.
        :param data: A list of dictionaries containing the data to be written to the file.
        """
        current_data = self.read_data()
        for item in data:
            if item not in current_data:
                current_data.append(item)
        with open(self._filename, 'w', encoding='utf-8') as file:
            json.dump(current_data, file, ensure_ascii=False, indent=4)

    def delete_data(self, data: Dict) -> None:
        """
        Deletes specific data from the JSON file.
        :param data: A dictionary containing the data to be deleted.
        """
        current_data = self.read_data()
        current_data = [item for item in current_data if item != data]
        with open(self._filename, 'w', encoding='utf-8') as file:
            json.dump(current_data, file, ensure_ascii=False, indent=4)
