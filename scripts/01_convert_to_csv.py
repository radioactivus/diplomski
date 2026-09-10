"""Interactively convert a local dataset or tabular file to CSV."""

from __future__ import annotations

from pathlib import Path

import pandas as pd
from datasets import Dataset, load_from_disk


SUPPORTED_SUFFIXES = {".csv", ".json", ".jsonl", ".parquet"}


def load_input(path: Path) -> pd.DataFrame:
    """Load a Hugging Face dataset directory or a common tabular file."""
    if path.is_dir():
        dataset = load_from_disk(str(path))
        if not isinstance(dataset, Dataset):
            raise ValueError("The selected directory does not contain a single Dataset object.")
        return dataset.to_pandas()

    suffix = path.suffix.lower()
    if suffix == ".csv":
        return pd.read_csv(path)
    if suffix in {".json", ".jsonl"}:
        return pd.read_json(path, lines=suffix == ".jsonl")
    if suffix == ".parquet":
        return pd.read_parquet(path)

    supported = ", ".join(sorted(SUPPORTED_SUFFIXES))
    raise ValueError(
        f"Unsupported input format: {suffix or '(no extension)'}. "
        f"Supported formats are: {supported}, as well as a Hugging Face Dataset directory."
    )


def ask_for_path(prompt: str, must_exist: bool = False) -> Path:
    """Ask for a non-empty filesystem path."""
    while True:
        value = input(prompt).strip().strip('"')
        if not value:
            print("The path cannot be empty.")
            continue

        path = Path(value).expanduser()
        if must_exist and not path.exists():
            print(f"Path does not exist: {path}")
            continue
        return path


def main() -> None:
    print("Dataset to CSV conversion")
    print("You can enter a file (.csv, .json, .jsonl, .parquet) or a Hugging Face Dataset directory.")
    print()

    input_path = ask_for_path("Enter the input file or directory path: ", must_exist=True)
    output_path = ask_for_path("Enter the output CSV filename: ")

    if output_path.suffix.lower() != ".csv":
        output_path = output_path.with_suffix(".csv")

    if output_path.exists():
        answer = input(f"The file already exists ({output_path}). Overwrite it? [y/N]: ").strip().lower()
        if answer not in {"y", "yes"}:
            print("Conversion cancelled.")
            return

    try:
        dataframe = load_input(input_path)
    except Exception as error:
        print(f"Error while loading input: {error}")
        raise SystemExit(1) from error

    output_path.parent.mkdir(parents=True, exist_ok=True)
    dataframe.to_csv(output_path, index=False)

    print()
    print("Conversion completed successfully.")
    print(f"Rows: {len(dataframe)}")
    print(f"Columns: {len(dataframe.columns)}")
    print(f"Column names: {', '.join(str(column) for column in dataframe.columns)}")
    print(f"Saved to: {output_path}")


if __name__ == "__main__":
    main()
