import os
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# =========================
# PATH
# =========================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(BASE_DIR)

DATA_PATH = os.path.join(PROJECT_DIR, "data", "processed", "fact_stock_risk.csv")
MODEL_PATH = os.path.join(PROJECT_DIR, "models", "model.pkl")

# =========================
# LOAD DATA
# =========================
df = pd.read_csv(DATA_PATH)

print("Shape dataset :", df.shape)

# =========================
# PREPARE DATA
# =========================
# Suppression colonnes inutiles
X = df.drop(columns=["stockout_risk"])
y = df["stockout_risk"]

# Supprimer identifiants
X = X.drop(columns=["product_id", "store_id"], errors="ignore")

# Encodage des catégories
for col in X.select_dtypes(include=["object"]).columns:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col].astype(str))

# =========================
# SPLIT
# =========================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# =========================
# TRAIN
# =========================
model = RandomForestClassifier()
model.fit(X_train, y_train)

# =========================
# EVALUATION
# =========================
y_pred = model.predict(X_test)

print("\n=== EVALUATION ===")
print("Accuracy :", accuracy_score(y_test, y_pred))
print("\nClassification report :")
print(classification_report(y_test, y_pred))

# =========================
# SAVE MODEL
# =========================
joblib.dump(model, MODEL_PATH)
print("\nModèle sauvegardé :", MODEL_PATH)
