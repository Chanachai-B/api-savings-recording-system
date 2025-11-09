from abc import ABC, abstractmethod
from typing import List, Dict
from app.domain.entities.transaction import Transaction

class TransactionRepository(ABC):
    @abstractmethod
    def add(self, transaction: Transaction) -> Dict:
        pass

    @abstractmethod
    def get_all(self) -> List[Dict]:
        pass
