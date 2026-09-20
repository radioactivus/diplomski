"""Create academic figures from the completed dataset and experiment results."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_RANDOM_DATA_DIR = PROJECT_ROOT / "data" / "random"
DEFAULT_CHRONOLOGICAL_DATA_DIR = PROJECT_ROOT / "data" / "chronological"
DEFAULT_RESULTS_DIR = PROJECT_ROOT / "results" / "repeated_experiments"
DEFAULT_OUTPUT_DIR = DEFAULT_RESULTS_DIR / "figures"

SPLITS = ("random", "chronological")
SPLIT_LABELS = {"random": "Random split", "chronological": "Chronological split"}
LABEL_NAMES = {0: "Bullish", 1: "Bearish", 2: "Neutral"}
LABEL_COLORS = {"Bullish": "#2A9D8F", "Bearish": "#D1495B", "Neutral": "#6C757D"}
MODEL_LABELS = {
    "original_finbert": "Original FinBERT",
    "tfidf_logistic_regression": "TF-IDF + Logistic Regression",
    "fine_tuned": "Fine-tuned FinBERT",
}
MODEL_COLORS = {
    "original_finbert": "#457B9D",
    "tfidf_logistic_regression": "#E9C46A",
    "fine_tuned": "#E76F51",
}
SEEDS = (43, 47, 53, 59, 61)


def configure_style() -> None:
    """Set a restrained style suitable for academic figures."""
    plt.rcParams.update(
        {
            "figure.dpi": 120,
            "savefig.dpi": 300,
            "font.size": 10,
            "axes.titlesize": 12,
            "axes.labelsize": 10,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.grid": True,
            "grid.alpha": 0.2,
            "grid.linewidth": 0.7,
        }
    )


def load_json(path: Path) -> dict:
    """Load one JSON result file."""
    with path.open(encoding="utf-8") as file:
        return json.load(file)


def create_class_distribution(random_data_dir: Path, chronological_data_dir: Path, output_dir: Path) -> None:
    """Plot class counts for all three subsets of both split strategies."""
    records = []
    for split_name, data_dir in (("random", random_data_dir), ("chronological", chronological_data_dir)):
        for subset in ("train", "validation", "test"):
            frame = pd.read_csv(data_dir / f"{subset}.csv")
            counts = frame["labels"].value_counts()
            for label_id, label_name in LABEL_NAMES.items():
                records.append({
                    "split": SPLIT_LABELS[split_name],
                    "subset": subset.capitalize(),
                    "label": label_name,
                    "count": int(counts.get(label_id, 0)),
                })

    distribution = pd.DataFrame(records)
    distribution.to_csv(output_dir / "class_distribution.csv", index=False)
    groups = [(split, subset) for split in SPLIT_LABELS.values() for subset in ("Train", "Validation", "Test")]
    x = np.arange(len(groups))
    width = 0.24
    figure, axis = plt.subplots(figsize=(11, 5.2))
    for offset, label_name in enumerate(LABEL_NAMES.values()):
        values = [
            distribution.loc[
                (distribution["split"] == split)
                & (distribution["subset"] == subset)
                & (distribution["label"] == label_name),
                "count",
            ].iloc[0]
            for split, subset in groups
        ]
        axis.bar(x + (offset - 1) * width, values, width=width, label=label_name, color=LABEL_COLORS[label_name])
    axis.set_title("Class distribution by split strategy and subset")
    axis.set_xlabel("Dataset subset")
    axis.set_ylabel("Number of examples")
    axis.set_xticks(x, [f"{split}\n{subset}" for split, subset in groups])
    axis.legend(frameon=False, ncols=3)
    figure.tight_layout()
    figure.savefig(output_dir / "class_distribution_comparison.png", bbox_inches="tight")
    plt.close(figure)


def load_model_metrics(results_dir: Path) -> pd.DataFrame:
    """Load baseline, TF-IDF, and all fine-tuned metrics into one table."""
    records = []
    for split_name in SPLITS:
        split_dir = results_dir / split_name
        for filename in ("baseline_metrics.json", "tfidf_metrics.json"):
            records.append(load_json(split_dir / filename))
        for seed in SEEDS:
            records.append(load_json(split_dir / f"seed_{seed}" / "metrics.json"))
    return pd.DataFrame(records)


def create_model_comparison(metrics: pd.DataFrame, output_dir: Path) -> None:
    """Plot mean macro F1 for all models and both split strategies."""
    summaries = []
    for split_name in SPLITS:
        for model_name in MODEL_LABELS:
            model_rows = metrics[(metrics["split"] == split_name) & (metrics["model"] == model_name)]
            summaries.append({
                "split": split_name,
                "model": model_name,
                "mean_f1_macro": model_rows["f1_macro"].mean(),
                "std_f1_macro": model_rows["f1_macro"].std(ddof=1) if len(model_rows) > 1 else 0.0,
            })

    summary = pd.DataFrame(summaries)
    summary.to_csv(output_dir / "model_comparison_summary.csv", index=False)
    figure, axes = plt.subplots(1, 2, figsize=(11, 4.8), sharex=True)
    y_positions = np.arange(len(MODEL_LABELS))
    for axis, split_name in zip(axes, SPLITS):
        rows = summary[summary["split"] == split_name].set_index("model").loc[list(MODEL_LABELS)]
        for y_position, model_name in zip(y_positions, MODEL_LABELS):
            value = rows.loc[model_name, "mean_f1_macro"]
            error = rows.loc[model_name, "std_f1_macro"]
            axis.errorbar(
                value,
                y_position,
                xerr=error if model_name == "fine_tuned" else None,
                fmt="o",
                markersize=9,
                capsize=4,
                color=MODEL_COLORS[model_name],
            )
            label = f"{value:.3f}"
            if model_name == "fine_tuned":
                label += f" ± {error:.3f}"
            axis.text(value + 0.012, y_position, label, va="center", fontsize=9)
        axis.set_title(SPLIT_LABELS[split_name])
        axis.set_yticks(y_positions, [MODEL_LABELS[name] for name in MODEL_LABELS])
        axis.set_xlim(0.30, 0.65)
        axis.set_xlabel("Macro F1")
        axis.grid(axis="x", alpha=0.25)
        axis.grid(axis="y", visible=False)
    figure.suptitle("Macro F1 comparison by split strategy", y=1.02)
    figure.tight_layout()
    figure.savefig(output_dir / "model_macro_f1_comparison.png", bbox_inches="tight")
    plt.close(figure)


def create_seed_variability(metrics: pd.DataFrame, output_dir: Path) -> None:
    """Plot fine-tuned macro F1 for every seed with mean lines."""
    fine_tuned = metrics[metrics["model"] == "fine_tuned"].copy()
    fine_tuned["seed"] = fine_tuned["seed"].astype(int)
    figure, axis = plt.subplots(figsize=(9, 5.2))
    for split_name, color in (("random", "#E76F51"), ("chronological", "#457B9D")):
        rows = fine_tuned[fine_tuned["split"] == split_name].sort_values("seed")
        axis.plot(rows["seed"], rows["f1_macro"], marker="o", linewidth=2,
                  label=SPLIT_LABELS[split_name], color=color)
        mean = rows["f1_macro"].mean()
        axis.axhline(mean, color=color, linestyle="--", alpha=0.6)
        axis.text(rows["seed"].max() + 0.25, mean, f"mean={mean:.3f}", color=color, va="center")
    axis.set_title("Fine-tuned FinBERT macro F1 across seeds")
    axis.set_xlabel("Training seed")
    axis.set_ylabel("Macro F1")
    axis.set_xticks(SEEDS)
    axis.set_ylim(0.3, 0.65)
    axis.legend(frameon=False)
    figure.tight_layout()
    figure.savefig(output_dir / "fine_tuned_seed_variability.png", bbox_inches="tight")
    plt.close(figure)


def create_mcnemar_plot(results_dir: Path, output_dir: Path) -> None:
    """Plot exact McNemar p-values for all fine-tuned runs."""
    rows = []
    for split_name in SPLITS:
        for seed in SEEDS:
            result = load_json(results_dir / split_name / f"seed_{seed}" / "mcnemar.json")
            rows.append({"split": split_name, "seed": seed, "p_value": result["exact_mcnemar_p_value"]})
    mcnemar = pd.DataFrame(rows)
    mcnemar.to_csv(output_dir / "mcnemar_results.csv", index=False)
    figure, axis = plt.subplots(figsize=(8.5, 5.2))
    y = np.arange(len(SEEDS))
    split_offsets = {"random": -0.18, "chronological": 0.18}
    split_colors = {"random": "#457B9D", "chronological": "#E76F51"}
    for split_name in SPLITS:
        split_rows = mcnemar[mcnemar["split"] == split_name].set_index("seed")
        values = np.array(
            [-np.log10(max(split_rows.loc[seed, "p_value"], 1e-300)) for seed in SEEDS]
        )
        clipped_values = np.minimum(values, 10)
        bars = axis.barh(
            y + split_offsets[split_name],
            clipped_values,
            height=0.32,
            color=split_colors[split_name],
            label=SPLIT_LABELS[split_name],
        )
        for bar, value in zip(bars, values):
            if value > 10:
                axis.text(9.82, bar.get_y() + bar.get_height() / 2, ">10", ha="right", va="center", color="white", fontsize=8, fontweight="bold")
    axis.axvline(-np.log10(0.05), color="#6C757D", linestyle="--", label="p = 0.05")
    axis.set_title("Exact McNemar test results")
    axis.set_xlabel("−log10(p-value)")
    axis.set_ylabel("Training seed")
    axis.set_yticks(y, SEEDS)
    axis.set_xlim(0, 10)
    axis.set_ylim(-0.5, len(SEEDS) - 0.5)
    axis.invert_yaxis()
    axis.grid(axis="x", alpha=0.2)
    axis.set_axisbelow(True)
    axis.legend(frameon=False, loc="center left", bbox_to_anchor=(1.02, 0.5))
    figure.tight_layout()
    figure.savefig(output_dir / "mcnemar_p_values.png", bbox_inches="tight")
    plt.close(figure)


def create_confusion_matrices(metrics: pd.DataFrame, output_dir: Path) -> None:
    """Plot actual baseline, TF-IDF, and best fine-tuned confusion matrices."""
    selected = []
    for split_name in SPLITS:
        split_rows = metrics[metrics["split"] == split_name]
        for model_name in ("original_finbert", "tfidf_logistic_regression"):
            row = split_rows[split_rows["model"] == model_name].iloc[0]
            selected.append((split_name, MODEL_LABELS[model_name], np.array(row["confusion_matrix"]), None))
        fine_rows = split_rows[split_rows["model"] == "fine_tuned"].sort_values("f1_macro", ascending=False)
        best = fine_rows.iloc[0]
        selected.append((split_name, MODEL_LABELS["fine_tuned"], np.array(best["confusion_matrix"]), int(best["seed"])))

    # Arrange model rows against split columns so each matrix gets more room.
    model_order = {label: index for index, label in enumerate(MODEL_LABELS.values())}
    selected.sort(key=lambda item: (model_order[item[1]], SPLITS.index(item[0])))
    figure, axes = plt.subplots(3, 2, figsize=(11, 14), sharex=True, sharey=True)
    labels = list(LABEL_NAMES.values())
    image = None
    for axis, (split_name, model_label, matrix, seed) in zip(axes.flat, selected):
        image = axis.imshow(matrix, cmap="Blues")
        threshold = matrix.max() / 2
        for row in range(matrix.shape[0]):
            for column in range(matrix.shape[1]):
                axis.text(column, row, str(matrix[row, column]), ha="center", va="center",
                          fontsize=14,
                          color="white" if matrix[row, column] > threshold else "black")
        title = f"{SPLIT_LABELS[split_name]}\n{model_label}"
        if seed is not None:
            title += f" (best seed {seed})"
        axis.set_title(title, fontsize=14, pad=10)
        axis.set_xlabel("Predicted class", fontsize=12)
        axis.set_ylabel("True class", fontsize=12)
        axis.set_xticks(range(3), labels, fontsize=11)
        axis.set_yticks(range(3), labels, fontsize=11)
        axis.grid(False)
    figure.subplots_adjust(left=0.12, right=0.88, bottom=0.06, top=0.96, wspace=0.35, hspace=0.45)
    colorbar_axis = figure.add_axes([0.91, 0.14, 0.025, 0.72])
    colorbar = figure.colorbar(image, cax=colorbar_axis)
    colorbar.set_label("Number of examples", fontsize=12)
    figure.savefig(output_dir / "confusion_matrices_actual_results.png", bbox_inches="tight")
    plt.close(figure)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--random-data-dir", type=Path, default=DEFAULT_RANDOM_DATA_DIR)
    parser.add_argument("--chronological-data-dir", type=Path, default=DEFAULT_CHRONOLOGICAL_DATA_DIR)
    parser.add_argument("--results-dir", type=Path, default=DEFAULT_RESULTS_DIR)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    args = parser.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)
    configure_style()
    metrics = load_model_metrics(args.results_dir)
    create_class_distribution(args.random_data_dir, args.chronological_data_dir, args.output_dir)
    create_model_comparison(metrics, args.output_dir)
    create_seed_variability(metrics, args.output_dir)
    create_mcnemar_plot(args.results_dir, args.output_dir)
    create_confusion_matrices(metrics, args.output_dir)
    print(f"Created figures in {args.output_dir}")


if __name__ == "__main__":
    main()
