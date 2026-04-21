import pandas as pd
import json

# ============================
# CHARGEMENT CSV
# ============================
def load_csv(file_path):
    return pd.read_csv(file_path)

# ============================
# CHARGEMENT JSON
# ============================
def load_json(file_path):
    with open(file_path) as f:
        data = json.load(f)
    return pd.DataFrame(data)

# ============================
# CHARGEMENT JSONL
# ============================
def load_jsonl(file_path):
    data = []
    with open(file_path) as f:
        for line in f:
            data.append(json.loads(line))
    return pd.DataFrame(data)

# ============================
# PIPELINE INGESTION
# ============================
def run_ingest():

    orders = load_csv("data/raw/orders.csv")
    products = load_csv("data/raw/products.csv")
    stores = load_csv("data/raw/stores.csv")

    inventory = load_json("data/raw/inventory.json")
    reviews = load_jsonl("data/raw/reviews.jsonl")

    # Vérification
    print("Orders :", orders.shape)
    print("Products :", products.shape)
    print("Stores :", stores.shape)
    print("Inventory :", inventory.shape)
    print("Reviews :", reviews.shape)

if __name__ == "__main__":
    run_ingest()
