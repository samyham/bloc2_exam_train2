# 📦 Projet RNCP Bloc 2 — Pipeline ETL & Machine Learning

---

## 🎯 Objectif

Construire une architecture de données complète permettant de :

* collecter des données multi-sources (CSV, JSON, JSONL)
* transformer et nettoyer les données (ETL)
* construire une table analytique `fact_stock_risk`
* entraîner un modèle de Machine Learning
* prédire le risque de rupture de stock

---

## 🧱 Architecture

```
bloc2_project/
│── data/
│   ├── raw/
│   └── processed/
│── scripts/
│── models/
│── sql/
│── logs/
│── docker-compose.yml
│── README.md
```

---

## 📥 Ingestion (ingest.py)

Chargement de données hétérogènes :

* CSV → pandas
* JSON → json
* JSONL → parsing ligne par ligne

✔ Vérification :

* présence fichiers
* dimensions datasets

---

## 🔄 ETL (etl.py)

### Nettoyage :

* suppression doublons
* conversion types (dates, numériques)
* suppression valeurs incohérentes
* normalisation texte

### Feature Engineering :

* `sales_7d`
* `sales_30d`
* `avg_rating`
* `stock_qty`

### Jointures :

* orders + inventory + products + stores + reviews

### Target :

```
stockout_risk = (stock_qty < 10 AND sales_7d > 5)
```

---

## 📊 Visualisation

Deux visualisations ont été réalisées :

1. Distribution du risque :

* équilibre des classes

2. Corrélation stock vs ventes :

* validation logique métier

---

## 🗄️ Stockage SQL

* Base PostgreSQL via Docker
* Tables :

  * fact_stock_risk

✔ Permet requêtes analytiques

---

## 🤖 Machine Learning

Modèle : RandomForestClassifier

### Pourquoi ce choix ?

* robuste
* peu sensible au bruit
* adapté aux données tabulaires

### Résultat :

* Accuracy élevée (~1.0)

⚠️ Limite :

* risque d’overfitting (dataset petit)

---

## 🐳 Docker

Utilisation de docker-compose pour :

* lancer PostgreSQL
* reproduire environnement

---

## ⚠️ Problèmes rencontrés

* FileNotFoundError → mauvais chemin
* Caractère invisible (U+2028) → copier/coller
* Docker → déconnexion VM
* Git → mauvais repo

---

## 🔐 RGPD & Sécurité

* pas de données sensibles exploitées
* architecture locale sécurisée
* séparation des couches

---

## 🌱 Sobriété numérique

* modèle simple (RandomForest)
* pipeline optimisé
* pas de calcul inutile

---

## 🚀 Améliorations possibles

* API REST
* tests automatisés
* pipeline CI/CD
* optimisation modèle

---

## ✅ Conclusion

Pipeline complet :
✔ ingestion
✔ ETL
✔ ML
✔ stockage

Projet conforme aux exigences RNCP Bloc 2.
