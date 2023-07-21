from openpyxl.worksheet.worksheet import Worksheet
from openpyxl.cell import Cell
from openpyxl import load_workbook, Workbook

from typing import Tuple, Generator


class Excel:
    def __init__(self, filename: str):
        self.workbook: Workbook = load_workbook(filename=filename)
        self.worksheet: Worksheet = self.workbook.active
    
    @property
    def values(self) -> Generator[Tuple[Cell], None, None]:
        return self.worksheet.rows
