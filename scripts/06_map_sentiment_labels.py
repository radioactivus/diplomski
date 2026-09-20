"""Add FinBERT-compatible sentiment labels to the dataset splits."""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT_DIR = PROJECT_ROOT / "data/random"

# Original dataset IDs: 0 = neutral, 1 = bearish, 2 = bullish.
# Model IDs: 0 = bullish, 1 = bearish, 2 = neutral.
LABEL_MAPPING = {
    0: 2,
    1: 1,
    2: 0,
}


def map_split(input_dir: Path, split_name: str) -> pd.DataFrame:
    """Load one split and add the mapped labels column."""
    input_path = input_dir / f"{split_name}.csv"

    if not input_path.exists():
        raise FileNotFoundError(f"Input split not found: {input_path}")

    data = pd.read_csv(input_path)

    if "market_direction" not in data.columns:
        raise ValueError(f"Missing market_direction column in: {input_path}")

    unknown_labels = set(data["market_direction"].dropna().unique()) - set(LABEL_MAPPING)
    if unknown_labels:
        raise ValueError(f"Unknown market_direction labels: {sorted(unknown_labels)}")

    data["labels"] = data["market_direction"].map(LABEL_MAPPING)
    return data


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_INPUT_DIR)
    args = parser.parse_args()

    for split_name in ("train", "validation", "test"):
        data = map_split(args.data_dir, split_name)
        output_path = args.data_dir / f"{split_name}.csv"
        data.to_csv(output_path, index=False)

        print(f"{split_name.capitalize()} set: {len(data)} rows -> {output_path}")
        print("Label distribution:")
        print(data["labels"].value_counts().sort_index())
        print()


if __name__ == "__main__":
    main()
