"""Add FinBERT-compatible sentiment labels to the dataset splits."""

from __future__ import annotations

from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_DIR = PROJECT_ROOT / "data/splits"
OUTPUT_DIR = PROJECT_ROOT / "data/labeled_splits"

# Original dataset IDs: 0 = neutral, 1 = bearish, 2 = bullish.
# Model IDs: 0 = bullish, 1 = bearish, 2 = neutral.
LABEL_MAPPING = {
    0: 2,
    1: 1,
    2: 0,
}


def map_split(split_name: str) -> pd.DataFrame:
    """Load one split and add the mapped labels column."""
    input_path = INPUT_DIR / f"ethereum_{split_name}.csv"

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
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for split_name in ("train", "validation", "test"):
        data = map_split(split_name)
        output_path = OUTPUT_DIR / f"ethereum_{split_name}.csv"
        data.to_csv(output_path, index=False)

        print(f"{split_name.capitalize()} set: {len(data)} rows -> {output_path}")
        print("Label distribution:")
        print(data["labels"].value_counts().sort_index())
        print()


if __name__ == "__main__":
    main()
