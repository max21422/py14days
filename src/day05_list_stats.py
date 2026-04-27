import math


def parse_numbers(text: str) -> list[float]:
    # 允許用逗號或空白分隔
    # 例："1,2, 3" 或 "1 2 3"
    cleaned = text.replace(",", " ")
    parts = [p for p in cleaned.split() if p != ""]

    numbers = []
    for p in parts:
        try:
            numbers.append(float(p))
        except ValueError:
            raise ValueError(f"無法解析成數字：{p}")
    return numbers


def mean(nums: list[float]) -> float:
    return sum(nums) / len(nums)


def median(nums: list[float]) -> float:
    s = sorted(nums)
    n = len(s)
    mid = n // 2
    if n % 2 == 1:
        return s[mid]
    return (s[mid - 1] + s[mid]) / 2


def stddev_population(nums: list[float]) -> float:
    # 這裡先用「母體標準差」版本：sqrt( sum((x-avg)^2)/n )
    avg = mean(nums)
    var = sum((x - avg) ** 2 for x in nums) / len(nums)
    return math.sqrt(var)


def main():
    text = input("輸入數字（用逗號或空白分隔，例如 1,2,3）：").strip()

    try:
        nums = parse_numbers(text)
    except ValueError as e:
        print(f"輸入錯誤：{e}")
        return

    if len(nums) == 0:
        print("輸入錯誤：請至少輸入 1 個數字。")
        return

    print("=== 統計結果 ===")
    print(f"數量：{len(nums)}")
    print(f"最小值：{min(nums)}")
    print(f"最大值：{max(nums)}")
    print(f"平均：{mean(nums)}")
    print(f"中位數：{median(nums)}")
    print(f"標準差(母體)：{stddev_population(nums)}")
    print(f"排序後：{sorted(nums)}")


if __name__ == "__main__":
    main()