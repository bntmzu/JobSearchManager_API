import json
import os
from abc import ABC, abstractmethod
from typing import List, Dict

class FileStorage(ABC):
    @abstractmethod
    def read_data(self) -> List[Dict]:
        pass

    @abstractmethod
    def write_data(self, data: List[Dict]) -> None:
        pass

    @abstractmethod
    def delete_data(self, data: Dict) -> None:
        pass

class JSONFileStorage(FileStorage):
    def __init__(self, filename: str = "data/vacancies.json"):
        self._filename = filename

    def read_data(self) -> List[Dict]:
        if not os.path.exists(self._filename):
            return []
        with open(self._filename, 'r', encoding='utf-8') as file:
            return json.load(file)

    def write_data(self, data: List[Dict]) -> None:
        current_data = self.read_data()
        for item in data:
            if item not in current_data:
                current_data.append(item)
        with open(self._filename, 'w', encoding='utf-8') as file:
            json.dump(current_data, file, ensure_ascii=False, indent=4)

    def delete_data(self, data: Dict) -> None:
        current_data = self.read_data()
        current_data = [item for item in current_data if item != data]
        with open(self._filename, 'w', encoding='utf-8') as file:
            json.dump(current_data, file, ensure_ascii=False, indent=4)
