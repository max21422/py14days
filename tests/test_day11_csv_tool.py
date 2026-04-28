import csv
from pathlib import Path

from src.commands.csv_cmd import read_numeric_column


def test_read_numeric_column(tmp_path: Path):
    p = tmp_path / "scores.csv"
    with p.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["name", "score"])
        w.writerow(["Amy", "78"])
        w.writerow(["Bob", "92"])

    nums = read_numeric_column(p, "score")
    assert nums == [78.0, 92.0]