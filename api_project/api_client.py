import requests
from typing import Dict, List, Optional
import json
from abc import ABC, abstractmethod

class BaseAPIClient(ABC):
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = requests.Session()
    
    def _make_request(self, method: str, endpoint: str, **kwargs) -> Dict:
        url = f"{self.base_url}/{endpoint}"
        response = self.session.request(method, url, **kwargs)
        response.raise_for_status()
        return response.json()
    
    @abstractmethod
    def get_all(self, **params) -> List[Dict]:
        pass
    
    @abstractmethod
    def get_by_id(self, item_id: int) -> Dict:
        pass
    
    @abstractmethod
    def search(self, query: str, **params) -> List[Dict]:
        pass 