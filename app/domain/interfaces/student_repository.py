from abc import ABC, abstractmethod
from typing import List, Dict

class StudentRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Dict]:
        pass
