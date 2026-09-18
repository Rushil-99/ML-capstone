"""
Download the 'Used Cars' (Uncovering Factors that Affect Used Car Prices)
dataset from Kaggle into data/raw/.

Source: https://www.kaggle.com/datasets/thedevastator/uncovering-factors-that-affect-used-car-prices

Setup (one-time):
    1. pip install kaggle
    2. Create a Kaggle API token: https://www.kaggle.com/settings -> "Create New Token"
       This downloads kaggle.json.
    3. Place it at ~/.kaggle/kaggle.json (Linux/Mac) or
       C:\\Users\\<you>\\.kaggle\\kaggle.json (Windows), and chmod 600 it on Linux/Mac:
           mkdir -p ~/.kaggle
           mv ~/Downloads/kaggle.json ~/.kaggle/kaggle.json
           chmod 600 ~/.kaggle/kaggle.json

Usage:
    python data/download_dataset.py
"""

import os
import zipfile
from pathlib import Path

DATASET = "thedevastator/uncovering-factors-that-affect-used-car-prices"
OUT_DIR = Path(__file__).parent / "raw"


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    try:
        from kaggle.api.kaggle_api_extended import KaggleApi
    except ImportError as exc:
        raise SystemExit(
            "The 'kaggle' package is not installed. Run: pip install kaggle"
        ) from exc

    api = KaggleApi()
    api.authenticate()  # reads ~/.kaggle/kaggle.json

    print(f"Downloading {DATASET} to {OUT_DIR} ...")
    api.dataset_download_files(DATASET, path=str(OUT_DIR), unzip=False)

    # Unzip whatever archive(s) came down
    for zip_path in OUT_DIR.glob("*.zip"):
        print(f"Extracting {zip_path.name} ...")
        with zipfile.ZipFile(zip_path, "r") as zf:
            zf.extractall(OUT_DIR)
        os.remove(zip_path)

    print("Done. Files in data/raw/:")
    for f in sorted(OUT_DIR.iterdir()):
        print(" -", f.name)


if __name__ == "__main__":
    main()
