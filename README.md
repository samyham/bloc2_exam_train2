# 📦 Projet RNCP — Pipeline Data Engineering & Machine Learning

---

## 🎯 Objectif du projet

Ce projet a pour but de construire un pipeline complet de données permettant de :

* ingérer plusieurs sources de données (CSV, JSON, JSONL)
* transformer et nettoyer ces données (ETL)
* construire une table analytique
* entraîner un modèle de Machine Learning
* prédire un risque métier : **stockout_risk (rupture de stock)**
* stocker et industrialiser avec Docker et PostgreSQL

---

## 🧱 1. Construction de l’architecture

Nous avons structuré le projet comme en entreprise avec :

* `data/raw` → données brutes
* `data/processed` → données transformées
* `scripts` → code Python
* `models` → modèles ML
* `sql` → requêtes SQL
* `logs` → logs

👉 Objectif : séparer les responsabilités et rendre le projet maintenable.

---

## 📂 2. Ingestion des données

### 📌 Données utilisées

* orders.csv
* products.csv
* stores.csv
* inventory.json
* reviews.jsonl
* events_api_sample.json

### ⚙️ Méthode

Nous avons créé un script `ingest.py` permettant de :

* lire différents formats (CSV, JSON, JSONL)
* charger les données avec pandas
* vérifier leur structure (dimensions)

👉 Pourquoi ?

Parce qu’en Data Engineering, les données viennent souvent de sources multiples.

---

## 🔄 3. ETL — Transformation des données

### 🎯 Objectif

Construire une table analytique :

👉 `fact_stock_risk.csv`

---

### 🧹 Nettoyage

Nous avons :

* supprimé les doublons
* converti les types (dates, numériques)
* filtré les données incohérentes (quantité > 0)
* normalisé les colonnes texte

👉 Pourquoi ?

Pour garantir la qualité des données avant analyse.

---

### 📊 Feature Engineering

Nous avons créé :

* `sales_7d` → ventes sur 7 jours
* `sales_30d` → ventes sur 30 jours
* `avg_rating` → moyenne des avis
* `stock_qty` → stock actuel

👉 Pourquoi ?

Ces variables permettent de mieux représenter la demande et le stock.

---

### 🎯 Variable cible

```python
stockout_risk = (stock faible ET forte demande)
```

👉 Logique métier :

* stock < 10
* ventes récentes élevées

👉 Pourquoi ?

Cela permet de transformer un problème métier en problème de classification.

---

### 🔗 Jointures

Nous avons fusionné :

* ventes
* stock
* produits
* magasins
* avis

👉 Objectif : avoir une vision complète par produit et magasin.

---

## 🤖 4. Machine Learning

### 🎯 Objectif

Prédire `stockout_risk`

---

### ⚙️ Préparation

* suppression des identifiants (`product_id`, `store_id`)
* encodage des variables catégorielles
* séparation train/test

---

### 🧠 Modèle choisi

👉 **RandomForestClassifier**

---

### ❓ Pourquoi ce choix ?

* robuste aux données bruitées
* fonctionne bien sans tuning complexe
* adapté aux datasets tabulaires
* évite l’overfitting (arbres multiples)

---

### 📊 Résultat

* Accuracy ≈ 1.0

👉 Attention :

* dataset petit → risque d’overfitting
* mais suffisant pour un projet pédagogique

---

## 🐳 5. Docker & PostgreSQL

### 🎯 Objectif

Mettre en place une base de données

---

### ⚙️ Ce qu’on a fait

* création d’un `docker-compose.yml`
* lancement d’un container PostgreSQL
* préparation pour stockage des données

---

### ❓ Pourquoi Docker ?

* environnement reproductible
* isolation
* standard en entreprise

---

## 🗄️ 6. Stockage des données

Nous avons utilisé un script pour :

* lire `fact_stock_risk.csv`
* insérer dans PostgreSQL

👉 Objectif : passer d’un fichier à une base de données.

---

## 🚀 7. Versioning avec Git

### ⚙️ Actions réalisées

* `git init`
* `git add`
* `git commit`
* `git push`

---

### ❓ Pourquoi ?

* suivre les modifications
* partager le projet
* collaborer

---

## ⚠️ 8. Erreurs rencontrées

### ❌ FileNotFoundError

👉 Cause : mauvais chemin
👉 Solution : vérifier avec `ls`

---

### ❌ ModuleNotFoundError

👉 Cause : package non installé
👉 Solution : pip install

---

### ❌ Problème Docker

👉 VM qui se déconnecte
👉 Solution : reconnecter SSH

---

### ❌ Caractère invisible (U+2028)

👉 Cause : copier/coller
👉 Solution : réécrire la ligne

---

## ✅ Conclusion

Ce projet démontre :

* la mise en place d’un pipeline data complet
* la maîtrise des étapes ETL
* l’utilisation du Machine Learning
* l’industrialisation avec Docker
* la gestion de projet avec Git

👉 Il s’agit d’un projet complet de Data Engineering + Data Science.

---
