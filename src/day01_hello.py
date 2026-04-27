def main():
    print("Hello, Python!")
    name = input("請輸入你的名字：").strip()
    if name == "":
        name = "匿名"
    print(f"你好，{name}！")


if __name__ == "__main__":
    main()