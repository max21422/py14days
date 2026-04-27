import csv
import json
from pathlib import Path

from stats_utils import summary


def read_scores_from_csv(path: Path, score_field: str = "score") -> list[float]:
    nums: list[float] = []

    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            raise ValueError("CSV 沒有 header（欄位名稱）")

        if score_field not in reader.fieldnames:
            raise ValueError(f"找不到欄位：{score_field}，目前欄位：{reader.fieldnames}")

        for i, row in enumerate(reader, start=2):  # header 是第 1 行，所以資料從第 2 行開始算
            raw = (row.get(score_field) or "").strip()
            if raw == "":
                raise ValueError(f"第 {i} 行 {score_field} 是空的")
            try:
                nums.append(float(raw))
            except ValueError:
                raise ValueError(f"第 {i} 行 {score_field} 不是數字：{raw}")

    if len(nums) == 0:
        raise ValueError("CSV 裡沒有任何數字資料")

    return nums


def main():
    in_path = Path("data") / "scores.csv"
    out_dir = Path("out")
    out_path = out_dir / "scores_report.json"

    if not in_path.exists():
        print(f"找不到檔案：{in_path.resolve()}")
        return

    try:
        scores = read_scores_from_csv(in_path, score_field="score")
        info = summary(scores)
    except ValueError as e:
        print(f"錯誤：{e}")
        return

    out_dir.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8") as f:
        json.dump(info, f, ensure_ascii=False, indent=2)

    print(f"已讀取：{in_path}")
    print(f"筆數：{info['count']}, 平均：{info['mean']}, 中位數：{info['median']}")
    print(f"已輸出：{out_path.resolve()}")


if __name__ == "__main__":
    main()