def main():
    s = input("請輸入分數（0~100）：").strip()

    # 先用最直覺的檢查方式：只接受純數字
    if not s.isdigit():
        print("輸入錯誤：請輸入 0~100 的整數。")
        return

    score = int(s)

    if score < 0 or score > 100:
        print("輸入錯誤：分數必須在 0~100。")
        return

    if score >= 90:
        level = "優秀"
    elif score >= 60:
        level = "及格"
    else:
        level = "不及格"

    print(f"你的分數：{score}，結果：{level}")


if __name__ == "__main__":
    main()