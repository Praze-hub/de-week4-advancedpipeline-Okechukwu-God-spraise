import requests
from typing import List, Dict
from urllib3.util import Retry
from requests.adapters import HTTPAdapter

class APIClient:
    def __init__(self, base_url: str, products_endpoint: str = "/products", users_endpoint: str = "/users", timeout: int = 30, session: requests.Session = None):
        self.base_url = base_url.rstrip("/")
        self.products_endpoint = products_endpoint
        self.users_endpoint = users_endpoint
        self.timeout = timeout
        self.session = session or self._build_session()
        
        
    def _build_session(self) -> requests.Session:
        s = requests.Session()
        retries = Retry(total=3, backoff_factor=0.5, status_forcelist=[429, 500, 502, 503, 504],
                                                      allowed_methods=["HEAD", "GET", "OPTIONS"])
        s.mount("https://", HTTPAdapter(max_retries=retries))
        s.mount("http://", HTTPAdapter(max_retries=retries))
        return s
    
    def _get(self, path: str, params: dict = None) -> List[Dict]:
        url = f"{self.base_url}{path}"
        resp = self.session.get(url, params=params or {}, timeout=self.timeout)
        if not resp.ok:
            resp.raise_for_status()
        data = resp.json()
        if not isinstance(data, list):
            raise ValueError("Expected list from API, got:: {}".format(type(data)))
        return data
    
    def get_all_products(self, limit: int = 2) -> List[Dict]:
        results = []
        page = 0
        while True:
            params = { "limit": limit, "offset": page * limit}
            page_data = self._get(self.products_endpoint, params=params)
            if not page_data:
                break
            results.extend(page_data)
            page += 1
        return results
    
    def get_all_users(self) -> List[Dict]:
        return self._get(self.users_endpoint)