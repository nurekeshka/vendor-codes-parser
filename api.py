from typing import Dict, List
import requests
import settings


class AutopartsSearch:
    def __init__(self):
        self.host = f'https://{settings.settings.get("ABCP", "HOST")}'
        self.user = settings.settings.get('ABCP', 'USER')
        self.md5p = settings.settings.get('ABCP', 'MD5P')

    @property
    def auth_credits(self) -> Dict[str, str]:
        return {'userlogin': self.user, 
                'userpsw': self.md5p}

    def get_autoparts_from(self, vendor_code: str) -> List[Dict[str, str | int]]:
        params = {**self.auth_credits, **{'number': vendor_code}}
        data = requests.get(url=f'{self.host}/search/brands/', params=params).json()
        return None if data.get('errorCode') == 301 else list(data.values())

    def get_brands_from(self, vendor_code: str) -> List[str]:
        data = self.get_autoparts_from(vendor_code=vendor_code)
        
        if data:
            return [autopart['brand'] for autopart in data]
