import os
import json
from datetime import timedelta
import pandas as pd

# =========================
# PATHS (IMPORTANT)
# =========================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(BASE_DIR)

RAW_PATH = os.path.join(PROJECT_DIR, "data", "raw")
PROCESSED_PATH = os.path.join(PROJECT_DIR, "data", "processed")

os.makedirs(PROCESSED_PATH, exist_ok=True)

# =========================
# LOAD
# =========================
def load_csv(file):
    return pd.read_csv(os.path.join(RAW_PATH, file))

def load_json(file):
    with open(os.path.join(RAW_PATH, file)) as f:
        return pd.DataFrame(json.load(f))

def load_jsonl(file):
    data = []
    with open(os.path.join(RAW_PATH, file)) as f:
        for line in f:
            data.append(json.loads(line))
    return pd.DataFrame(data)

# =========================
# CLEANING
# =========================
def clean_orders(df):
    df = df.drop_duplicates()
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
    df = df.dropna()
    df = df[df["quantity"] > 0]
    return df

def clean_products(df):
    df = df.drop_duplicates(subset=["product_id"])
    df["category"] = df["category"].astype(str).str.lower().str.strip()
    return df

def clean_stores(df):
    df = df.drop_duplicates(subset=["store_id"])
    df["region"] = df["region"].astype(str).str.lower().str.strip()
    return df

def clean_inventory(df):
    df["last_update"] = pd.to_datetime(df["last_update"], errors="coerce")
    df = df.sort_values("last_update")
    df = df.drop_duplicates(["product_id", "store_id"], keep="last")
    df["stock_qty"] = df["stock_qty"].fillna(0)
    return df

def clean_reviews(df):
    df["rating"] = pd.to_numeric(df["rating"], errors="coerce")
    df = df[(df["rating"] >= 1) & (df["rating"] <= 5)]
    return df

# =========================
# FEATURES
# =========================
def build_sales_features(orders):
    max_date = orders["order_date"].max()

    sales_7d = (
        orders[orders["order_date"] >= max_date - timedelta(days=7)]
        .groupby(["product_id", "store_id"])["quantity"]
        .sum()
        .reset_index(name="sales_7d")
    )

    sales_30d = (
        orders[orders["order_date"] >= max_date - timedelta(days=30)]
        .groupby(["product_id", "store_id"])["quantity"]
        .sum()
        .reset_index(name="sales_30d")
    )

    df = pd.merge(sales_30d, sales_7d, on=["product_id", "store_id"], how="outer").fillna(0)
    return df

def build_reviews_features(df):
    return df.groupby("product_id")["rating"].mean().reset_index(name="avg_rating")

# =========================
# BUILD FINAL DATASET
# =========================
def build_dataset():

    orders = clean_orders(load_csv("orders.csv"))
    products = clean_products(load_csv("products.csv"))
    stores = clean_stores(load_csv("stores.csv"))
    inventory = clean_inventory(load_json("inventory.json"))
    reviews = clean_reviews(load_jsonl("reviews.jsonl"))

    sales = build_sales_features(orders)
    ratings = build_reviews_features(reviews)

    df = sales.merge(inventory, on=["product_id", "store_id"], how="left")
    df = df.merge(products[["product_id", "category"]], on="product_id", how="left")
    df = df.merge(stores[["store_id", "region"]], on="store_id", how="left")
    df = df.merge(ratings, on="product_id", how="left")

    df = df.fillna(0)

    # =========================
    # TARGET
    # =========================
    df["stockout_risk"] = (
        (df["stock_qty"] < 10) &
        (df["sales_7d"] > 5)
    ).astype(int)

    return df

# =========================
# SAVE
# =========================
def save(df):
    path = os.path.join(PROCESSED_PATH, "fact_stock_risk.csv")
    df.to_csv(path, index=False)
    print("Fichier sauvegardé :", path)

# =========================
# RUN
# =========================
if __name__ == "__main__":
    df = build_dataset()

    print("Shape :", df.shape)
    print(df.head())

    save(df)
