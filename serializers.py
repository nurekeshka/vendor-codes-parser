from typing import Tuple, Generator, List, Dict
from openpyxl.cell import Cell
from api import AutopartsSearch

import pandas as pd


class Serializer:
    autopart_brand = 'Professional Parts Sweden'
    search = AutopartsSearch()
    headers = {'crosses': 1, 'vendor_code': 0}
    
    def __init__(self, values: Generator[Tuple[Cell], None, None]):
        self.dataframe = pd.DataFrame(data=values)
        self.data: List[Dict[str, str]] = list()

        self.format()
    
    def format(self):
        for autopart in self.dataframe.itertuples():
            if autopart[self.headers['crosses']]:
                
                for vendor_code in autopart[self.headers['crosses']].split(' '):
                    brands = self.search.get_brands_from(vendor_code)

                    if brands:
                        for brand in brands:
                            self.data.append(self.create_row(
                                (self.autopart_brand, brand),
                                (autopart[self.headers['vendor_code']], vendor_code)))
    
    @staticmethod
    def create_row(brands: Tuple[str], codes: Tuple[str]):
        return {'brand_one': brands[0], 'code_one': codes[0],
                'brand_two': brands[1], 'code_two': codes[1]}
