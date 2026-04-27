def bucket_label(score: int) -> str:
    # 0-9, 10-19, ..., 90-100
    if score == 100:
        return "100"
    start = (score // 10) * 10
    end = start + 9
    return f"{start:02d}-{end:02d}"


def main():
    raw = input("輸入分數（0~100整數，用逗號或空白分隔）：").strip()
    cleaned = raw.replace(",", " ")
    parts = [p for p in cleaned.split() if p != ""]

    if len(parts) == 0:
        print("輸入錯誤：請至少輸入 1 個分數。")
        return

    scores: list[int] = []
    for p in parts:
        if not p.isdigit():
            print(f"輸入錯誤：{p} 不是整數。")
            return
        v = int(p)
        if v < 0 or v > 100:
            print(f"輸入錯誤：{v} 超出範圍 0~100。")
            return
        scores.append(v)

    hist: dict[str, int] = {}
    for s in scores:
        label = bucket_label(s)
        hist[label] = hist.get(label, 0) + 1

    # 排序輸出：00-09, 10-19, ... , 90-99, 100
    order = [f"{i:02d}-{i+9:02d}" for i in range(0, 100, 10)] + ["100"]

    print("=== 分數分布（直方圖）===")
    for key in order:
        count = hist.get(key, 0)
        bar = "#" * count
        print(f"{key}: {count:2d} {bar}")


if __name__ == "__main__":
    main()