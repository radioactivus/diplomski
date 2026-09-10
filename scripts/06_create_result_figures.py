"""Create figures used in the project documentation from saved experiment data."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RESULTS_DIR = PROJECT_ROOT / "results"
SPLITS_DIR = PROJECT_ROOT / "data/labeled_splits"
LABEL_NAMES = {0: "Bullish", 1: "Bearish", 2: "Neutral"}
SPLIT_NAMES = ("train", "validation", "test")
COLORS = {
    "Bullish": "#2A9D8F",
    "Bearish": "#D1495B",
    "Neutral": "#6C757D",
    "Baseline": "#457B9D",
    "Fine-tuned": "#E76F51",
}


def configure_style() -> None:
    """Configure a restrained style suitable for academic figures."""
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


def create_class_distribution() -> None:
    """Plot sentiment class counts for each dataset split."""
    split_labels = {"train": "Obuka", "validation": "Validacija", "test": "Test"}
    records = []
    for split_name in SPLIT_NAMES:
        split_path = SPLITS_DIR / f"ethereum_{split_name}.csv"
        data = pd.read_csv(split_path)
        counts = data["labels"].value_counts()
        for label_id, label_name in LABEL_NAMES.items():
            records.append(
                {
                    "split": split_labels[split_name],
                    "label": label_name,
                    "count": int(counts.get(label_id, 0)),
                }
            )

    distribution = pd.DataFrame(records)
    splits = [split_labels[name] for name in SPLIT_NAMES]
    x_positions = np.arange(len(splits))
    bar_width = 0.24

    fig, ax = plt.subplots(figsize=(8.2, 4.8))
    for offset, label_name in enumerate(LABEL_NAMES.values()):
        values = [
            distribution.loc[
                (distribution["split"] == split) &
                (distribution["label"] == label_name),
                "count",
            ].iloc[0]
            for split in splits
        ]
        bars = ax.bar(
            x_positions + (offset - 1) * bar_width,
            values,
            width=bar_width,
            label=label_name,
            color=COLORS[label_name],
        )
        ax.bar_label(bars, padding=3, fontsize=8)

    ax.set_title("Raspodela klasa sentimenta po skupovima")
    ax.set_xlabel("Skup podataka")
    ax.set_ylabel("Broj vesti")
    ax.set_xticks(x_positions, splits)
    ax.legend(frameon=False, ncols=3, loc="upper right")
    fig.tight_layout()
    fig.savefig(RESULTS_DIR / "class_distribution.png", bbox_inches="tight")
    plt.close(fig)


def create_model_comparison() -> None:
    """Plot baseline and fine-tuned test metrics on a shared scale."""
    comparison = pd.read_csv(RESULTS_DIR / "model_comparison.csv")
    x_positions = np.arange(len(comparison))
    bar_width = 0.36

    fig, ax = plt.subplots(figsize=(9, 4.8))
    baseline_bars = ax.bar(
        x_positions - bar_width / 2,
        comparison["baseline"],
        width=bar_width,
        label="Original FinBERT",
        color=COLORS["Baseline"],
    )
    tuned_bars = ax.bar(
        x_positions + bar_width / 2,
        comparison["fine_tuned"],
        width=bar_width,
        label="Ethereum fine-tuned FinBERT",
        color=COLORS["Fine-tuned"],
    )

    ax.bar_label(baseline_bars, fmt="%.3f", padding=3, fontsize=8)
    ax.bar_label(tuned_bars, fmt="%.3f", padding=3, fontsize=8)
    ax.set_title("Poređenje performansi na test skupu")
    ax.set_xlabel("Evaluaciona metrika")
    ax.set_ylabel("Vrednost")
    ax.set_ylim(0, 0.67)
    ax.set_xticks(x_positions, comparison["metric"])
    ax.legend(frameon=False, ncols=2, loc="upper center")
    fig.tight_layout()
    fig.savefig(RESULTS_DIR / "model_performance_comparison.png", bbox_inches="tight")
    plt.close(fig)


def create_training_history() -> None:
    """Plot loss and validation metrics recorded after each epoch."""
    history = pd.read_csv(RESULTS_DIR / "training_history.csv")

    fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.4))

    axes[0].plot(
        history["epoch"],
        history["training_loss"],
        marker="o",
        linewidth=2,
        label="Gubitak na obuci",
        color=COLORS["Baseline"],
    )
    axes[0].plot(
        history["epoch"],
        history["validation_loss"],
        marker="o",
        linewidth=2,
        label="Validacioni gubitak",
        color=COLORS["Fine-tuned"],
    )
    axes[0].set_title("Funkcija gubitka po epohama")
    axes[0].set_xlabel("Epoha")
    axes[0].set_ylabel("Gubitak")
    axes[0].set_xticks(history["epoch"])
    axes[0].legend(frameon=False)

    metric_columns = {
        "accuracy": "Tačnost",
        "precision_macro": "Makro preciznost",
        "recall_macro": "Makro odziv",
        "f1_macro": "Makro F1",
    }
    metric_colors = ("#2A9D8F", "#E9C46A", "#9B5DE5", "#D1495B")
    for (column, label), color in zip(metric_columns.items(), metric_colors):
        axes[1].plot(
            history["epoch"],
            history[column],
            marker="o",
            linewidth=2,
            label=label,
            color=color,
        )

    axes[1].set_title("Validacione metrike po epohama")
    axes[1].set_xlabel("Epoha")
    axes[1].set_ylabel("Vrednost")
    axes[1].set_xticks(history["epoch"])
    axes[1].set_ylim(0.42, 0.58)
    axes[1].legend(frameon=False, fontsize=8)

    fig.tight_layout()
    fig.savefig(RESULTS_DIR / "training_history.png", bbox_inches="tight")
    plt.close(fig)


def create_confusion_matrices() -> None:
    """Plot confusion matrices for the baseline and fine-tuned models."""
    matrices = {
        "Originalni FinBERT": np.array(
            [[62, 19, 78], [21, 51, 36], [95, 25, 70]]
        ),
        "Ethereum fine-tuned FinBERT": np.array(
            [[80, 14, 65], [15, 65, 28], [53, 22, 115]]
        ),
    }
    labels = list(LABEL_NAMES.values())
    figure, axes = plt.subplots(1, 2, figsize=(10.5, 4.4))

    for axis, (title, matrix) in zip(axes, matrices.items()):
        image = axis.imshow(matrix, cmap="Blues", vmin=0, vmax=115)
        threshold = matrix.max() / 2
        for row in range(matrix.shape[0]):
            for column in range(matrix.shape[1]):
                axis.text(
                    column,
                    row,
                    str(matrix[row, column]),
                    ha="center",
                    va="center",
                    color="white" if matrix[row, column] > threshold else "black",
                    fontsize=11,
                )

        axis.set_title(title)
        axis.set_xlabel("Predviđena klasa")
        axis.set_ylabel("Stvarna klasa")
        axis.set_xticks(range(len(labels)), labels)
        axis.set_yticks(range(len(labels)), labels)
        axis.grid(False)

    # Leave enough room between the right-hand matrix and the shared colorbar.
    figure.colorbar(image, ax=axes, fraction=0.025, pad=0.10, label="Broj primera")
    figure.subplots_adjust(left=0.08, right=0.86, bottom=0.13, top=0.88, wspace=0.32)
    figure.savefig(RESULTS_DIR / "confusion_matrices.png", bbox_inches="tight")
    plt.close(figure)


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    configure_style()
    create_class_distribution()
    create_model_comparison()
    create_training_history()
    create_confusion_matrices()
    print("Result figures created successfully.")


if __name__ == "__main__":
    main()
