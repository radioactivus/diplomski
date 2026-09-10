"""Extract Ethereum-related news from the DLT-Sentiment-News dataset."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

import pandas as pd
from datasets import Dataset, load_dataset, load_from_disk


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATASET_ID = "ExponentialScience/DLT-Sentiment-News"
DEFAULT_LOCAL_PATH = PROJECT_ROOT / "data/DLT-Sentiment-News"
DEFAULT_OUTPUT_PATH = PROJECT_ROOT / "data/ethereum-sentiment-news.csv"

# Word boundaries prevent terms such as "eth" from matching inside other words.
ETHEREUM_PATTERN = re.compile(r"\bethereum\b|\bether\b|\beth\b", re.IGNORECASE)


def load_source_dataset(local_path: Path) -> Dataset:
    """Load the local dataset, or download it from Hugging Face if unavailable."""
    if local_path.exists():
        print(f"Loading local dataset: {local_path}")
        return load_from_disk(str(local_path))

    print(f"Local dataset not found. Downloading: {DATASET_ID}")
    return load_dataset(DATASET_ID, split="train")


def contains_ethereum_reference(row: dict) -> bool:
    """Check whether the title, description, or text contains an Ethereum term."""
    fields = (row.get("title"), row.get("description"), row.get("text"))
    combined_text = " ".join(str(value) for value in fields if value)
    return bool(ETHEREUM_PATTERN.search(combined_text))


def filter_dataset(dataset: Dataset) -> pd.DataFrame:
    required_columns = {"title", "description", "text", "market_direction"}
    missing_columns = required_columns.difference(dataset.column_names)
    if missing_columns:
        raise ValueError(f"Missing required columns: {sorted(missing_columns)}")

    rows = [row for row in dataset if contains_ethereum_reference(row)]
    filtered = pd.DataFrame(rows)

    if filtered.empty:
        raise ValueError("No news items were found using the selected filter.")

    # Remove empty texts and exact text duplicates.
    filtered["text"] = filtered["text"].fillna("").astype(str).str.strip()
    filtered = filtered[filtered["text"] != ""]
    filtered = filtered.drop_duplicates(subset=["text"]).reset_index(drop=True)
    return filtered


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_LOCAL_PATH)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT_PATH)
    args = parser.parse_args()

    dataset = load_source_dataset(args.input)
    filtered = filter_dataset(dataset)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    filtered.to_csv(args.output, index=False)

    print(f"Original number of news items: {len(dataset)}")
    print(f"Number of ETH news items after cleaning: {len(filtered)}")
    print(f"Saved to: {args.output}")
    print("\nmarket_direction distribution:")
    print(filtered["market_direction"].value_counts(dropna=False).sort_index())


if __name__ == "__main__":
    main()
