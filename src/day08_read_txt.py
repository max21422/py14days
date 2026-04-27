from pathlib import Path

from stats_utils import parse_numbers, summary


def read_text_file(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def main():
    path = Path("data") / "numbers.txt"
    if not path.exists():
        print(f"找不到檔案：{path.resolve()}")
        return

    text = read_text_file(path)

    try:
        nums = parse_numbers(text)
        info = summary(nums)
    except ValueError as e:
        print(f"錯誤：{e}")
        return

    print(f"已讀取：{path}，共 {info['count']} 筆數字")
    print("=== 統計摘要 ===")
    print(f"min: {info['min']}")
    print(f"max: {info['max']}")
    print(f"mean: {info['mean']}")
    print(f"median: {info['median']}")
    print(f"stddev_population: {info['stddev_population']}")


if __name__ == "__main__":
    main()