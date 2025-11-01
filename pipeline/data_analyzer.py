import pandas as pd
from typing import Dict

class DataAnalyzer:
    def analyze(self, enriched_df: pd.DataFrame) -> Dict[str, Dict]:
        enriched_df["seller_key"] = enriched_df["seller_username"].fillna(enriched_df["seller_email"]).fillna("UNKNOWN")
        
        grouped = enriched_df.groupby("seller_key").agg(
            total_revenue=pd.NamedAgg(column="revenue", aggfunc="sum"),
            product_count=pd.NamedAgg(column="id", aggfunc="count"),
            avg_price=pd.NamedAgg(column="price", aggfunc="mean")
            
        ).reset_index()
        
        
        result = {}
        for _, row in grouped.iterrows():
            result[row["seller_key"]] = {
                "total_revenue": float(row["total_revenue"]),
                "product_count": int(row["product_count"]),
                "avg_price": float(row["avg_price"]) if pd.notna(row["avg_price"]) else 0.0
            }
            
        return result