def main():
    s = input("請輸入 N（正整數）：").strip()

    if not s.isdigit():
        print("輸入錯誤：請輸入正整數。")
        return

    n = int(s)
    if n <= 0:
        print("輸入錯誤：N 必須 > 0。")
        return

    total = 0
    even_total = 0
    square_total = 0

    for i in range(1, n + 1):
        total += i
        square_total += i * i
        if i % 2 == 0:
            even_total += i

    print("=== 統計結果 ===")
    print(f"1~{n} 的總和：{total}")
    print(f"1~{n} 的偶數總和：{even_total}")
    print(f"1~{n} 的平方和：{square_total}")


if __name__ == "__main__":
    main()