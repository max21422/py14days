import argparse
import csv
import json
from pathlib import Path

from stats_utils import summary


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
                continue  # 這裡選擇跳過空值
            try:
                nums.append(float(raw))
            except ValueError:
                raise ValueError(f"第 {i} 行 {column} 不是數字：{raw}")

    return nums


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="CSV 欄位統計小工具")
    p.add_argument("--input", "-i", required=True, help="CSV 檔案路徑，例如 data/scores.csv")
    p.add_argument("--column", "-c", required=True, help="要統計的欄位名稱，例如 score")
    p.add_argument("--out", "-o", default="out/report.json", help="輸出 JSON 路徑（預設 out/report.json）")
    return p


def main():
    args = build_parser().parse_args()

    in_path = Path(args.input)
    out_path = Path(args.out)

    if not in_path.exists():
        print(f"找不到輸入檔：{in_path.resolve()}")
        return

    try:
        nums = read_numeric_column(in_path, args.column)
        if len(nums) == 0:
            raise ValueError("欄位沒有任何可用數字（可能都空白）")
        info = summary(nums)
    except ValueError as e:
        print(f"錯誤：{e}")
        return

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8") as f:
        json.dump(info, f, ensure_ascii=False, indent=2)

    print("=== 完成 ===")
    print(f"輸入：{in_path}")
    print(f"欄位：{args.column}")
    print(f"筆數：{info['count']}")
    print(f"平均：{info['mean']}")
    print(f"中位數：{info['median']}")
    print(f"輸出：{out_path.resolve()}")


if __name__ == "__main__":
    main()