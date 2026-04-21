import pandas as pd
from sqlalchemy import create_engine

# connexion PostgreSQL (docker)
engine = create_engine("postgresql://user:password@localhost:5432/rncp_db")

# charger le dataset
df = pd.read_csv("data/processed/fact_stock_risk.csv")

# envoyer dans la base
df.to_sql("fact_stock_risk", engine, if_exists="replace", index=False)

print("Données envoyées dans PostgreSQL")
