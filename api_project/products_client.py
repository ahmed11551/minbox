from .api_client import BaseAPIClient
from typing import Dict, List

class ProductsClient(BaseAPIClient):
    def __init__(self):
        super().__init__("https://dummyjson.com")
    
    def get_all(self, **params) -> List[Dict]:
        response = self._make_request("GET", "products", params=params)
        return response.get("products", [])
    
    def get_by_id(self, product_id: int) -> Dict:
        return self._make_request("GET", f"products/{product_id}")
    
    def search(self, query: str, **params) -> List[Dict]:
        params["q"] = query
        response = self._make_request("GET", "products/search", params=params)
        return response.get("products", [])
    
    def get_iphones(self) -> List[Dict]:
        return self.search("iPhone") 