import csv
from typing import List
from interfaces.data_source import ILogSource

class CsvLogSource(ILogSource):

    def __init__(self, filepath: str):
        self.filepath = filepath

    def get_logs(self) -> List[str]:
        try:
            with open(self.filepath, newline="") as csvfile:
                reader = csv.reader(csvfile)
                return [" | ".join(row) for row in reader]
        except FileNotFoundError:
            return ["Error: CSV file not found"]