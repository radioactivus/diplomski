"""Verify the generated train, validation, and test dataset splits."""

from __future__ import annotations

from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data/splits"


def load_split(split_name: str) -> pd.DataFrame:
    """Load one dataset split from its CSV file."""
    file_path = DATA_DIR / f"ethereum_{split_name}.csv"

    if not file_path.exists():
        raise FileNotFoundError(f"Split file not found: {file_path}")

    return pd.read_csv(file_path)


def main() -> None:
    splits = {
        "train": load_split("train"),
        "validation": load_split("validation"),
        "test": load_split("test"),
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
