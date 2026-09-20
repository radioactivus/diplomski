"""Create a chronological 80/10/10 split of Ethereum news."""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT_PATH = PROJECT_ROOT / "data/ethereum-sentiment-news.csv"
DEFAULT_OUTPUT_DIR = PROJECT_ROOT / "data/chronological"


def split_dataset(data: pd.DataFrame) -> dict[str, pd.DataFrame]:
    if "timestamp" not in data.columns:
        raise ValueError("Missing required column: timestamp")

    ordered = data.copy()
    ordered["_parsed_timestamp"] = pd.to_datetime(ordered["timestamp"], errors="coerce", utc=True)
    if ordered["_parsed_timestamp"].isna().any():
        raise ValueError("The timestamp column contains invalid or missing dates.")
    ordered = ordered.sort_values("_parsed_timestamp", kind="mergesort").drop(columns="_parsed_timestamp")

    train_end = int(len(ordered) * 0.8)
    validation_end = int(len(ordered) * 0.9)
    return {
        "train": ordered.iloc[:train_end].reset_index(drop=True),
        "validation": ordered.iloc[train_end:validation_end].reset_index(drop=True),
        "test": ordered.iloc[validation_end:].reset_index(drop=True),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT_PATH)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    args = parser.parse_args()

    if not args.input.exists():
        raise FileNotFoundError(f"Input file not found: {args.input}")
    data = pd.read_csv(args.input)
    if data.empty:
        raise ValueError("The input dataset is empty.")

    args.output_dir.mkdir(parents=True, exist_ok=True)
    for name, split in split_dataset(data).items():
        output = args.output_dir / f"{name}.csv"
        split.to_csv(output, index=False)
        print(f"{name.capitalize()}: {len(split)} rows -> {output}")


if __name__ == "__main__":
    main()
