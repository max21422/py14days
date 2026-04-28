import math


def parse_numbers(text: str) -> list[float]:
    """
    解析數字字串，允許用逗號或空白分隔。
    例：
      "1,2, 3"
      "1 2 3"
    回傳：list[float]
    """
    cleaned = text.replace(",", " ")
    parts = [p for p in cleaned.split() if p != ""]

    numbers: list[float] = []
    for p in parts:
        try:
            numbers.append(float(p))
        except ValueError:
            raise ValueError(f"無法解析成數字：{p}")
    return numbers


def mean(nums: list[float]) -> float:
    if len(nums) == 0:
        raise ValueError("nums 不可為空")
    return sum(nums) / len(nums)


def median(nums: list[float]) -> float:
    if len(nums) == 0:
        raise ValueError("nums 不可為空")

    s = sorted(nums)
    n = len(s)
    mid = n // 2
    if n % 2 == 1:
        return s[mid]
    return (s[mid - 1] + s[mid]) / 2


def stddev_population(nums: list[float]) -> float:
    """母體標準差：sqrt( sum((x-avg)^2)/n )"""
    if len(nums) == 0:
        raise ValueError("nums 不可為空")

    avg = mean(nums)
    var = sum((x - avg) ** 2 for x in nums) / len(nums)
    return math.sqrt(var)


def summary(nums: list[float], include_sorted: bool = True) -> dict:
    """
    回傳統計摘要（用 dict，方便輸出 JSON）
    include_sorted=False 可避免輸出排序後清單（資料多時很大）
    """
    if len(nums) == 0:
        raise ValueError("nums 不可為空")

    result = {
        "count": len(nums),
        "min": min(nums),
        "max": max(nums),
        "mean": mean(nums),
        "median": median(nums),
        "stddev_population": stddev_population(nums),
    }

    if include_sorted:
        result["sorted"] = sorted(nums)

    return result