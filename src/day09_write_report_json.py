import json
from pathlib import Path

from stats_utils import parse_numbers, summary


def main():
    in_path = Path("data") / "numbers.txt"
    out_dir = Path("out")
    out_path = out_dir / "report.json"

    if not in_path.exists():
        print(f"找不到檔案：{in_path.resolve()}")
        return

    text = in_path.read_text(encoding="utf-8")

    try:
        nums = parse_numbers(text)
        info = summary(nums)
    except ValueError as e:
        print(f"錯誤：{e}")
        return

    out_dir.mkdir(parents=True, exist_ok=True)

    with out_path.open("w", encoding="utf-8") as f:
        json.dump(info, f, ensure_ascii=False, indent=2)

    print(f"已輸出報表：{out_path.resolve()}")


if __name__ == "__main__":
    main()