import configparser
from pathlib import Path

class ConfigManager:
    def __init__(self, config_path: str = "pipeline.cfg"):
        self._parser = configparser.ConfigParser()
        self._parser.read(config_path)
        self._config_path = Path(config_path)
        
    def get_base_url(self) -> str:
        return self._parser.get("api", "base_url")
    
    def get_endpoint(self, key: str) -> str:
        return self._parser.get("api", key)
    
    def get_limit(self) -> int:
        return self._parser.getint("pagination", "limit")
    
    
    