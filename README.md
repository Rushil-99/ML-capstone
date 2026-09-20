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

Regression and Classification use **separate datasets**, chosen to fit each problem naturally rather than forcing one dataset into three different shapes. Clustering reuses the regression dataset (unsupervised, no separate target needed).

| Track | Dataset | Target | Framing |
|---|---|---|---|
| Regression | [Used Cars — Uncovering Factors that Affect Used Car Prices](https://www.kaggle.com/datasets/thedevastator/uncovering-factors-that-affect-used-car-prices) (`data/raw/autos.csv`) | `price` (continuous) | Predict a car's resale price from its listing attributes (vehicle type, registration year, power, mileage, brand, etc.) |
| Classification | [Vehicle Loan Default Prediction](https://www.kaggle.com/datasets/mamtadhaker/lt-vehicle-loan-default-prediction) (`data/raw/train.csv`) | `loan_default` (binary, 0/1) | Predict whether a vehicle loan defaults, from borrower and credit-bureau attributes |
| Clustering | Used Cars (same as Regression) | — (unsupervised) | Group listings by their attributes |

See `data/README.md` for the full data dictionary of both datasets.

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
Metrics: Accuracy, Precision, Recall, weighted F1, Confusion Matrix, ROC-AUC (binary — `loan_default` is a 2-class target, so plain ROC-AUC rather than OvR).

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

1. `data/raw/autos.csv` (regression + clustering) and `data/raw/train.csv` (classification) are already committed — no download step needed.
2. Open the relevant notebook in `notebooks/` (`regression.ipynb`, `classification.ipynb`, `clustering.ipynb`).
3. **Sections A (Dataset & EDA) and B (Preprocessing & Feature Engineering) are already implemented and run end-to-end** — real plots, cleaning, and feature engineering on the actual dataset.
4. **The algorithms themselves are left as `TODO`s, one per algorithm, for you to fill in** — each has its exact name/notes from the guidelines and a commented skeleton showing which variables to use and which dict keys to populate (`fitted_models`, `predictions`, `probabilities`). Fill each in, then the Evaluation/Tuning/Visualisation cells below them (also `TODO`, since they depend on the trained models) read straight from those dicts.
5. `random_state=42` is used throughout for reproducibility.

## Bonus (optional)

A Streamlit/Gradio GUI in `app/`, optionally deployed publicly, for up to +2 bonus marks in Review 2.

## Academic integrity

External code is cited inline via Markdown comments. Any generative AI assistance used is disclosed here as work progresses.
