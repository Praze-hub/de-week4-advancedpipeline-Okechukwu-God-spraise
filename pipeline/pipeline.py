import json
from config import ConfigManager
from api_client import APIClient
from data_enricher import DataEnricher
from data_analyzer import DataAnalyzer
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class Pipeline:
    def __init__(self, config_path: str = "pipeline.cfg"):
        self.config = ConfigManager(config_path)
        base_url = self.config.get_base_url()
        products_ep = self.config.get_endpoint("products_endpoint")
        users_ep = self.config.get_endpoint("users_endpoint")
        self.api_client = APIClient(base_url, products_endpoint=products_ep, users_endpoint=users_ep)
        self.enricher = DataEnricher()
        self.analyzer = DataAnalyzer()
        self.limit = self.config.get_limit()
        
        
    def run(self, output_path: str = "seller_performance_report.json"):
        logger.info("Fetching products...")
        products = self.api_client.get_all_products(limit=self.limit)
        logger.info("Fetching users...")
        users = self.api_client.get_all_users()
        logger.info(f"Enriching {len(products)} products with {len(users)} users...")
        enriched = self.enricher.enrich(products, users)
        logger.info("Analyzing enriched data...")
        analysis = self.analyzer.analyze(enriched)
        logger.info(f"Writing analysis to {output_path}")
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(analysis, f, indent=2)
            return analysis
        
        
        
if __name__ == "__main__":
    p = Pipeline("pipeline.cfg")
    result = p.run()   
    print("Done. Report keys:", list(result.keys())[:5])