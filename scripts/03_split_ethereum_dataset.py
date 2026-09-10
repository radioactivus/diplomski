"""Randomly split the filtered Ethereum dataset into train, validation, and test sets."""

from __future__ import annotations

import argparse
import random
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT_PATH = PROJECT_ROOT / "data/ethereum-sentiment-news.csv"
DEFAULT_OUTPUT_DIR = PROJECT_ROOT / "data/splits"
DEFAULT_SEED = 42


def assign_split(random_value: float) -> str:
    """Assign one row to a split according to the 80/10/10 probabilities."""
    if random_value < 0.80:
        return "train"
    if random_value < 0.90:
        return "validation"
    return "test"


def split_dataset(data: pd.DataFrame, seed: int) -> dict[str, pd.DataFrame]:
    """Assign every row independently and return the three resulting datasets."""
    random_generator = random.Random(seed)
    split_names = [
        assign_split(random_generator.random())
        for _ in range(len(data))
    ]

    data_with_split = data.copy()
    data_with_split["split"] = split_names

    return {
        split_name: data_with_split[data_with_split["split"] == split_name]
        .drop(columns=["split"])
        .reset_index(drop=True)
        for split_name in ("train", "validation", "test")
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT_PATH)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    args = parser.parse_args()

    if not args.input.exists():
        raise FileNotFoundError(f"Input file not found: {args.input}")

    data = pd.read_csv(args.input)
    if data.empty:
        raise ValueError("The input dataset is empty.")

    splits = split_dataset(data, seed=args.seed)
    args.output_dir.mkdir(parents=True, exist_ok=True)

    for split_name, split_data in splits.items():
        output_path = args.output_dir / f"ethereum_{split_name}.csv"
        split_data.to_csv(output_path, index=False)
        print(f"{split_name.capitalize()} set: {len(split_data)} rows -> {output_path}")

    print(f"Total rows: {len(data)}")
    print(f"Random seed: {args.seed}")
    print("\nLabel distribution by split:")
    print(
        pd.concat(
            {
                split_name: split_data["market_direction"].value_counts(normalize=True)
                for split_name, split_data in splits.items()
            },
            axis=1,
        ).fillna(0)
    )


if __name__ == "__main__":
    main()
