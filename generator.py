from typing import Dict
import pandas as pd


class Generator:
    def __init__(self, data: Dict[str, str]):
        self.data = data
        self.dataframe = pd.DataFrame(data)

    def export_as_xlsx(self, filename: str):
        self.dataframe.to_excel(filename)
