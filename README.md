# ML Capstone — 23CSE301 (AY 2026-27)

End-to-end Machine Learning pipeline covering three tracks — **Regression**, **Classification**, and **Clustering** — built for the 23CSE301 Machine Learning capstone project.

## Project overview

| | |
|---|---|
| Course | 23CSE301 Machine Learning |
| Academic Year | 2026-27 |
| Team size | 3 |
| Tracks | Regression, Classification, Clustering |
| Reviews | Review 1 (Regression + Classification Part A), Review 2 (Classification Part B + Clustering) |

## Problem statement

| Track | Dataset | Target |
|---|---|---|
| Regression | [Used Cars — Uncovering Factors that Affect Used Car Prices](https://www.kaggle.com/datasets/thedevastator/uncovering-factors-that-affect-used-car-prices) (Kaggle) | `price` — predict the resale price of a used car from listing attributes (vehicle type, registration year, power, mileage, brand, etc.) |
| Classification | _TBD_ | |
| Clustering | _TBD_ | |

See `data/README.md` for the full data dictionary and download instructions.

## Repository structure

```
/
├── README.md              # This file
├── requirements.txt        # Python dependencies
├── data/                   # Raw dataset files or scripts to fetch them
├── notebooks/              # regression.ipynb, classification.ipynb, clustering.ipynb
├── models/                 # Saved model files (.pkl via joblib) — optional
└── app/                    # GUI / deployment code for the bonus track
```

## Tracks & algorithms

### Regression (Review 1)
Linear, Ridge, Lasso, ElasticNet, Polynomial, Decision Tree, Random Forest, Gradient Boosting, SVR, KNN Regressor.
Metrics: R², RMSE, MAE, 5-fold CV R² (top 2 models).

### Classification (Part A – Review 1, Part B – Review 2)
Logistic Regression, KNN, Gaussian Naive Bayes, Decision Tree, SVC, Random Forest, AdaBoost, Gradient Boosting, Bagging, MLP Classifier.
Metrics: Accuracy, Precision, Recall, weighted F1, Confusion Matrix, ROC-AUC (OvR for multi-class).

### Clustering (Review 2)
K-Means (Elbow curve), Agglomerative Hierarchical (Dendrogram).
Metrics: Silhouette Score, Davies-Bouldin Index, Calinski-Harabasz Index. PCA (2D) visualisation mandatory; t-SNE encouraged.

## Environment setup

```bash
git clone https://github.com/Rushil-99/ML-capstone.git
cd ML-capstone
python -m venv venv
source venv/bin/activate   # venv\Scripts\activate on Windows
pip install -r requirements.txt
```

## How to run

1. Place the assigned dataset(s) in `data/`.
2. Open the relevant notebook in `notebooks/` (`regression.ipynb`, `classification.ipynb`, `clustering.ipynb`).
3. Run all cells top-to-bottom (`random_state=42` is used throughout for reproducibility).

## Bonus (optional)

A Streamlit/Gradio GUI in `app/`, optionally deployed publicly, for up to +2 bonus marks in Review 2.

## Academic integrity

External code is cited inline via Markdown comments. Any generative AI assistance used is disclosed here as work progresses.
