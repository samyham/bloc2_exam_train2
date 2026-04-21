import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed/fact_stock_risk.csv")

# 1. Distribution du target
df["stockout_risk"].value_counts().plot(kind="bar")
plt.title("Distribution du risque de rupture")
plt.savefig("logs/plot_risk.png")
plt.clf()

# 2. Corrélation stock vs ventes
plt.scatter(df["stock_qty"], df["sales_7d"])
plt.title("Stock vs ventes")
plt.xlabel("Stock")
plt.ylabel("Ventes 7j")
plt.savefig("logs/plot_stock_sales.png")

print("Visualisations générées")
