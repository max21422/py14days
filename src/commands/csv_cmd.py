import csv
from pathlib import Path

from src.report_utils import write_json_report
from src.stats_utils import summary


def read_numeric_column(path: Path, column: str) -> list[float]:
    nums: list[float] = []
    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            raise ValueError("CSV 沒有 header（欄位名稱）")
        if column not in reader.fieldnames:
            raise ValueError(f"找不到欄位：{column}，目前欄位：{reader.fieldnames}")

        for i, row in enumerate(reader, start=2):
            raw = (row.get(column) or "").strip()
            if raw == "":
                continue
            try:
                nums.append(float(raw))
            except ValueError:
                raise ValueError(f"第 {i} 行 {column} 不是數字：{raw}")

    return nums


def run(input_path: str, column: str, out_path: str, pretty: bool = True, include_sorted: bool = True) -> None:
    in_path = Path(input_path)

    if not in_path.exists():
        raise FileNotFoundError(f"找不到輸入檔：{in_path.resolve()}")

    nums = read_numeric_column(in_path, column)
    if len(nums) == 0:
        raise ValueError("欄位沒有任何可用數字（可能都空白）")

    info = summary(nums, include_sorted=include_sorted)
    write_json_report(info, out_path=out_path, pretty=pretty)