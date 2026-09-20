# Dataset and Results Scripts

These scripts are intended to be run from the `diplomski` directory.

## Pipeline

```text
DLT-Sentiment-News dataset
        |
        v
02_filter_ethereum_news.py
        |
        +--> 03_split_random.py   --> data/random/
        |
        +--> 04_split_chronological.py --> data/chronological/
                         |
                         v
              05_verify_splits.py
                         |
                         v
              06_map_sentiment_labels.py
```

## Script overview

### `01_convert_to_csv.py` (optional)

Converts a local Hugging Face dataset or a supported tabular file into CSV format. This is a general-purpose helper and is not required in the main project pipeline because `02_filter_ethereum_news.py` reads the local Hugging Face dataset directly.

**Input:** A Hugging Face dataset directory, CSV, JSON, JSONL, or Parquet file. The default dataset directory is `data/DLT-Sentiment-News/`.

**Output:** A user-selected CSV file. In the project workflow, this is `data/ethereum-sentiment-news.csv`.

### `02_filter_ethereum_news.py`

Extracts Ethereum-related news and removes empty texts and exact text duplicates.

**Input:** `data/DLT-Sentiment-News/` by default, or another dataset path supplied with `--input`.

**Output:** `data/ethereum-sentiment-news.csv` by default.

### `03_split_random.py`

Creates one reproducible random split using an 80/10/10 train/validation/test ratio.

**Input:** `data/ethereum-sentiment-news.csv`.

**Output:** `data/random/train.csv`, `data/random/validation.csv`, and `data/random/test.csv`.

**Default seed:** `42`. The input and output paths can be changed with `--input`, `--output-dir`, and `--seed`.

### `04_split_chronological.py`

Creates a chronological 80/10/10 split. Older records are assigned to training, the following records to validation, and the newest records to testing.

**Input:** `data/ethereum-sentiment-news.csv`. The file must contain a valid `timestamp` column.

**Output:** `data/chronological/train.csv`, `data/chronological/validation.csv`, and `data/chronological/test.csv`.

This script does not use a random seed.

### `05_verify_splits.py`

Checks a split directory for required files and columns, reports dataset sizes and label values, and detects identical texts shared between splits.

**Input:** A split directory supplied with `--data-dir`. The default is `data/random/`.

**Output:** Verification information printed in the terminal. No files are modified.

Example:

```bash
python3 scripts/05_verify_splits.py --data-dir data/chronological
```

### `06_map_sentiment_labels.py`

Adds the numeric `labels` column required for FinBERT training. The original `market_direction` column is preserved.

**Input:** A split directory supplied with `--data-dir`. The default is `data/random/`.

**Output:** The `train.csv`, `validation.csv`, and `test.csv` files in the same directory, updated with the `labels` column.

The mapping is:

```text
neutral -> 2
bearish -> 1
bullish -> 0
```

### `07_create_result_figures.py`

Creates academic figures from the actual random and chronological datasets and the completed repeated-experiment results.

**Inputs:**

- `data/random/{train,validation,test}.csv`;
- `data/chronological/{train,validation,test}.csv`;
- `results/repeated_experiments/` with baseline, TF-IDF, fine-tuned and McNemar JSON files.

**Outputs:**

- `class_distribution_comparison.png` and `class_distribution.csv`;
- `model_macro_f1_comparison.png` and `model_comparison_summary.csv`;
- `fine_tuned_seed_variability.png`;
- `mcnemar_p_values.png` and `mcnemar_results.csv`;
- `confusion_matrices_actual_results.png`.

The confusion-matrix figure uses three model rows and two split-strategy columns. Fine-tuned matrices use the best seed by test macro F1 for each split. No values are manually entered in the script.

Example:

```bash
python3 scripts/07_create_result_figures.py
```

For results copied from another location:

```bash
python3 scripts/07_create_result_figures.py \
  --results-dir /path/to/repeated_experiments \
  --output-dir /path/to/figure_output
```

## Recommended execution order

```bash
python3 scripts/02_filter_ethereum_news.py
python3 scripts/03_split_random.py
python3 scripts/04_split_chronological.py
python3 scripts/05_verify_splits.py --data-dir data/random
python3 scripts/05_verify_splits.py --data-dir data/chronological
python3 scripts/06_map_sentiment_labels.py --data-dir data/random
python3 scripts/06_map_sentiment_labels.py --data-dir data/chronological
```
