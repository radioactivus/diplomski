"""Create one reproducible random 80/10/10 split of Ethereum news."""

from __future__ import annotations

import argparse
import random
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT_PATH = PROJECT_ROOT / "data/ethereum-sentiment-news.csv"
DEFAULT_OUTPUT_DIR = PROJECT_ROOT / "data/random"
DEFAULT_SEED = 42


def split_dataset(data: pd.DataFrame, seed: int) -> dict[str, pd.DataFrame]:
    generator = random.Random(seed)
    assignments = []
    for _ in range(len(data)):
        value = generator.random()
        assignments.append("train" if value < 0.8 else "validation" if value < 0.9 else "test")

    marked = data.copy()
    marked["split"] = assignments
    return {
        name: marked.loc[marked["split"] == name].drop(columns="split").reset_index(drop=True)
        for name in ("train", "validation", "test")
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

    args.output_dir.mkdir(parents=True, exist_ok=True)
    for name, split in split_dataset(data, args.seed).items():
        output = args.output_dir / f"{name}.csv"
        split.to_csv(output, index=False)
        print(f"{name.capitalize()}: {len(split)} rows -> {output}")
    print(f"Random seed: {args.seed}")


if __name__ == "__main__":
    main()
