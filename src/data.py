"""Loading the raw Olist tables with consistent types."""
import pandas as pd

from src.config import RAW_DIR

KAGGLE_URL = "https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce"

FILES = {
    "customers": "olist_customers_dataset.csv",
    "orders": "olist_orders_dataset.csv",
    "payments": "olist_order_payments_dataset.csv",
    "reviews": "olist_order_reviews_dataset.csv",
    "items": "olist_order_items_dataset.csv",
    "products": "olist_products_dataset.csv",
    "sellers": "olist_sellers_dataset.csv",
    "category_names": "product_category_name_translation.csv",
}

READ_OPTIONS = {
    "customers": {"dtype": {"customer_zip_code_prefix": str}},  # keep leading zeros in postcodes
    "orders": {"parse_dates": ["order_purchase_timestamp", "order_approved_at", "order_delivered_carrier_date",
                               "order_delivered_customer_date", "order_estimated_delivery_date"]},
    "reviews": {"parse_dates": ["review_creation_date", "review_answer_timestamp"]},
    "sellers": {"dtype": {"seller_zip_code_prefix": str}},
}


def load_tables(names=None) -> dict:
    """Load the Olist tables as a dict of DataFrames, e.g. load_tables()["orders"]."""
    names = list(FILES) if names is None else list(names)
    missing = [FILES[n] for n in names if not (RAW_DIR / FILES[n]).exists()]
    if missing:
        raise FileNotFoundError(
            f"Missing data files in {RAW_DIR}:\n  " + "\n  ".join(missing)
            + f"\nDownload the dataset from {KAGGLE_URL} and unzip the CSVs into data/raw/ (see README)."
        )
    return {n: pd.read_csv(RAW_DIR / FILES[n], **READ_OPTIONS.get(n, {})) for n in names}
