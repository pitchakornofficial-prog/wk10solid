from interfaces.data_source import ILogSource
from services.file_source import FileLogSource
from services.mock_source import MockLogSource
from services.csv_source import CsvLogSource   # สำหรับ Challenge

class SourceFactory:

    @staticmethod
    def create_source(source_type: str) -> ILogSource:
        if source_type == "file":
            return FileLogSource("app.log")
        elif source_type == "mock":
            return MockLogSource()
        elif source_type == "csv":
            return CsvLogSource("app.csv")
        else:
            raise ValueError("Unknown source type")