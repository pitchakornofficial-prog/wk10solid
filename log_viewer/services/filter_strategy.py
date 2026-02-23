from abc import ABC, abstractmethod
from typing import List

class IFilterStrategy(ABC):

    @abstractmethod
    def filter(self, logs: List[str]) -> List[str]:
        pass


class NoFilter(IFilterStrategy):

    def filter(self, logs: List[str]) -> List[str]:
        return logs


class ErrorOnlyFilter(IFilterStrategy):

    def filter(self, logs: List[str]) -> List[str]:
        return [log for log in logs if "ERROR" in log]