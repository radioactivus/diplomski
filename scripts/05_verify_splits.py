"""Verify the generated train, validation, and test dataset splits."""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DATA_DIR = PROJECT_ROOT / "data/random"


def load_split(data_dir: Path, split_name: str) -> pd.DataFrame:
    """Load one dataset split from its CSV file."""
    file_path = data_dir / f"{split_name}.csv"

    if not file_path.exists():
        raise FileNotFoundError(f"Split file not found: {file_path}")

    return pd.read_csv(file_path)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA_DIR)
    args = parser.parse_args()

    splits = {
        "train": load_split(args.data_dir, "train"),
        "validation": load_split(args.data_dir, "validation"),
        "test": load_split(args.data_dir, "test"),
    }

    required_columns = {"text", "market_direction"}
    for split_name, split_data in splits.items():
        missing_columns = required_columns.difference(split_data.columns)
        if missing_columns:
            raise ValueError(
                f"Missing columns in {split_name} split: {sorted(missing_columns)}"
            )

    print("Dataset sizes:")
    for split_name, split_data in splits.items():
        print(f"{split_name.capitalize()}: {split_data.shape[0]} rows, {split_data.shape[1]} columns")

    print("\nColumns:")
    print(splits["train"].columns.tolist())

    print("\nLabel values:")
    for split_name, split_data in splits.items():
        print(f"{split_name.capitalize()}: {sorted(split_data['market_direction'].dropna().unique())}")

    print("\nFirst training example:")
    if splits["train"].empty:
        raise ValueError("The training split is empty.")
    print(splits["train"].iloc[0])

    text_sets = {
        split_name: set(split_data["text"].dropna())
        for split_name, split_data in splits.items()
    }

    print("\nOverlapping texts:")
    print(f"Train/validation: {len(text_sets['train'] & text_sets['validation'])}")
    print(f"Train/test: {len(text_sets['train'] & text_sets['test'])}")
    print(f"Validation/test: {len(text_sets['validation'] & text_sets['test'])}")


if __name__ == "__main__":
    main()
