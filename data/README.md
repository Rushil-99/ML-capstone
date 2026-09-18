# data/

Place the instructor-assigned dataset(s) here, one per track if applicable.

Raw data files are git-ignored (see `.gitignore`) rather than committed directly — use `download_dataset.py` to fetch them locally into `data/raw/`.

## Datasets

| Track | Dataset | Source | Notes |
|---|---|---|---|
| Regression | Used Cars — Uncovering Factors that Affect Used Car Prices | [Kaggle](https://www.kaggle.com/datasets/thedevastator/uncovering-factors-that-affect-used-car-prices) | See below. Target: `price` |
| Classification | TBD | | |
| Clustering | TBD | | |

### Regression dataset: Used Cars

A cleaned republication of the eBay Kleinanzeigen (German eBay classifieds) used-car listings dataset. Each row is one used-car listing.

**How to get it:**
```bash
pip install kaggle
# place your Kaggle API token at ~/.kaggle/kaggle.json (see download_dataset.py docstring)
python data/download_dataset.py
```
This downloads and unzips the dataset into `data/raw/`.

**Data dictionary:**

| Column | Description |
|---|---|
| `dateCrawled` | When the ad was first crawled |
| `name` | Name/title of the car listing |
| `seller` | Whether the seller is private or a dealer |
| `offerType` | Type of listing (offer/request) |
| `price` | **Target variable** — listed price of the car |
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

Known data quality issues to handle in preprocessing (see `notebooks/regression.ipynb`): missing values in `vehicleType`, `gearbox`, `model`, `fuelType`, and `notRepairedDamage`; some unrealistic `price` and `yearOfRegistration` outliers to filter.
