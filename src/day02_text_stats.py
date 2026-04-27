def main():
    text = input("輸入一句話：")

    raw_len = len(text)
    cleaned = text.strip()
    cleaned_len = len(cleaned)

    # 以空白切詞（先用最簡單方式）
    # split() 不帶參數時會自動處理多個空白
    words = cleaned.split()
    word_count = len(words)

    print("=== 統計結果 ===")
    print(f"原始字元數：{raw_len}")
    print(f"去頭尾空白後字元數：{cleaned_len}")
    print(f"單字/詞數（用空白分隔）：{word_count}")
    print(f"切詞結果：{words}")


if __name__ == "__main__":
    main()