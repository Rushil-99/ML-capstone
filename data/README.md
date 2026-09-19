# data/

`data/raw/autos.csv` is the single dataset used across **all three tracks** (Regression, Classification, Clustering) — it's committed directly to the repo (68MB, under GitHub's 100MB limit) so notebooks run out-of-the-box without a separate download step. `download_dataset.py` is kept as a fallback / reproducibility script in case the file needs to be re-fetched.

## Dataset: Used Cars — Uncovering Factors that Affect Used Car Prices

Source: [Kaggle](https://www.kaggle.com/datasets/thedevastator/uncovering-factors-that-affect-used-car-prices) — a cleaned republication of the eBay Kleinanzeigen (German eBay classifieds) used-car listings dataset. Each row is one used-car listing (~371k rows raw, ~312k after cleaning).

| Track | Target | Framing |
|---|---|---|
| Regression | `price` (continuous) | Predict resale price directly |
| Classification | `price_category` (4 classes) | `price` binned into quartiles: `Budget` / `Economy` / `Premium` / `Luxury` |
| Clustering | — (unsupervised) | Cluster listings by attributes; `price_category` used only post-hoc to validate/interpret clusters |

**Re-fetching it (if ever needed):**
```bash
pip install kaggle
# place your Kaggle API token at ~/.kaggle/kaggle.json (see download_dataset.py docstring)
python data/download_dataset.py
```

**Data dictionary:**

| Column | Description |
|---|---|
| `dateCrawled` | When the ad was first crawled |
| `name` | Name/title of the car listing |
| `seller` | Whether the seller is private or a dealer |
| `offerType` | Type of listing (offer/request) |
| `price` | Listed price of the car — regression target / source of `price_category` |
| `abtest` | Whether the listing was part of an A/B test |
| `vehicleType` | Vehicle body type (e.g. sedan, SUV, bus) |
| `yearOfRegistration` | Year the car was first registered |
| `gearbox` | Transmission type (manual/automatic) |
| `powerPS` | Engine power, in PS (metric horsepower) |
| `model` | Car model name |
| `kilometer` | Kilometers driven (odometer reading) |
| `monthOfRegistration` | Month the car was first registered |
| `fuelType` | Fuel type (petrol, diesel, LPG, etc.) |
| `brand` | Car manufacturer/brand |
| `notRepairedDamage` | Whether the car has unrepaired damage |
| `dateCreated` | Date the ad was created on the site |
| `nrOfPictures` | Number of pictures in the listing |
| `postalCode` | Postal code of the seller |
| `lastSeen` | Last time the crawler saw this ad online |

**Cleaning applied (all three notebooks, consistently):** filter to realistic `price` (€100–150,000), `yearOfRegistration` (1950–2016), and `powerPS` (1–1000); drop duplicates and non-predictive columns (IDs, timestamps, picture count); engineer `vehicle_age = 2016 - yearOfRegistration`. Regression/Classification notebooks subsample to 8,000 rows (Clustering to a smaller sample) for computational feasibility of SVR/SVC/GridSearchCV on this environment's hardware — documented inline in each notebook.
