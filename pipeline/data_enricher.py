import pandas as pd
from typing import List, Dict, Optional

class DataEnricher:
    def enrich(self, products: List[Dict], users: List[Dict]) -> Optional[pd.DataFrame]:
        try:
            products_df = pd.DataFrame(products)
            users_df = pd.DataFrame(users)
            
            if "rating" in products_df.columns:
                products_df["quantity"] = products_df["rating"].apply(lambda x: x.get("count") if isinstance(x, dict) else 0)
            else:
                products_df["quantity"] = 0

            enriched_df = pd.merge(
                products_df,
                users_df,
                how="left",
                left_on="userId",
                right_on="id",
                suffixes=("", "_user")
            )

            enriched_df["seller_username"] = enriched_df["username"]
            enriched_df["seller_email"] = enriched_df["email"]
            enriched_df["seller_name"] = enriched_df.apply(
                lambda row: f"{row['name']['firstname']} {row['name']['lastname']}"
                if isinstance(row.get("name"), dict)
                else None,
                axis=1
            )

            enriched_df["revenue"] = enriched_df["price"] * enriched_df["quantity"]

            return enriched_df

        except Exception as e:
            print(f"[DataEnricher] Error enriching data: {e}")
            return None
