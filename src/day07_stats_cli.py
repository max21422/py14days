from stats_utils import parse_numbers, summary


def main():
    text = input("輸入數字（逗號或空白分隔）：").strip()

    try:
        nums = parse_numbers(text)
        info = summary(nums)
    except ValueError as e:
        print(f"錯誤：{e}")
        return

    print("=== 統計摘要 ===")
    for k, v in info.items():
        print(f"{k}: {v}")


if __name__ == "__main__":
    main()