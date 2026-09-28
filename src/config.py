"""Project paths and global settings."""
from pathlib import Path

# Project root = the folder that contains src/, notebooks/ and data/
PROJECT_ROOT = Path(__file__).resolve().parents[1]

RAW_DIR = PROJECT_ROOT / "data" / "raw"          # Olist CSVs from Kaggle (not committed to git)
OUTPUT_DIR = PROJECT_ROOT / "outputs"            # CSVs produced by the notebooks
FIGURES_DIR = PROJECT_ROOT / "reports" / "figures"  # charts used in the README

RANDOM_STATE = 42

for _folder in (OUTPUT_DIR, FIGURES_DIR):
    _folder.mkdir(parents=True, exist_ok=True)
