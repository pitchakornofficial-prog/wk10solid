from abc import ABC, abstractmethod
from typing import List

class ILogSource(ABC):

    @abstractmethod
    def get_logs(self) -> List[str]:
        """Return logs as list of strings"""
        pass