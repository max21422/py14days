from pathlib import Path


def run() -> None:
    data_dir = Path("data")
    data_dir.mkdir(parents=True, exist_ok=True)

    (data_dir / "numbers.txt").write_text("1, 2, 3\n10 20 30\n5\n", encoding="utf-8")
    (data_dir / "scores.csv").write_text(
        "name,score\nAmy,78\nBob,92\nCindy,65\nDavid,88\nEva,90\nFrank,55\n",
        encoding="utf-8",
    )