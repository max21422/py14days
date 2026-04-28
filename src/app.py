import argparse
import sys

from src.commands import csv_cmd, demo_cmd, text_cmd


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="stats", description="小型統計工具（TXT/CSV -> JSON 報表）")
    sub = p.add_subparsers(dest="command", required=True)

    stats_p = sub.add_parser("stats", help="統計相關功能")
    stats_sub = stats_p.add_subparsers(dest="kind", required=True)

    # 通用選項：pretty / no-sorted
    def add_common_flags(sp: argparse.ArgumentParser) -> None:
        sp.add_argument("--pretty", action="store_true", help="輸出漂亮縮排 JSON（預設）")
        sp.add_argument("--compact", action="store_true", help="輸出壓縮 JSON（無縮排）")
        sp.add_argument("--no-sorted", action="store_true", help="不輸出 sorted 欄位（避免 JSON 太大）")

    # stats text
    text_p = stats_sub.add_parser("text", help="讀取 TXT 數字並輸出統計 JSON")
    text_p.add_argument("-i", "--input", required=True, help="輸入 TXT 路徑，例如 data/numbers.txt")
    text_p.add_argument("-o", "--out", default="out/text_report.json", help="輸出 JSON 路徑")
    add_common_flags(text_p)

    # stats csv
    csv_p = stats_sub.add_parser("csv", help="讀取 CSV 指定欄位並輸出統計 JSON")
    csv_p.add_argument("-i", "--input", required=True, help="輸入 CSV 路徑，例如 data/scores.csv")
    csv_p.add_argument("-c", "--column", required=True, help="要統計的欄位，例如 score")
    csv_p.add_argument("-o", "--out", default="out/csv_report.json", help="輸出 JSON 路徑")
    add_common_flags(csv_p)

    # stats demo
    stats_sub.add_parser("demo", help="產生範例資料到 data/（numbers.txt, scores.csv）")

    return p


def resolve_pretty(args) -> bool:
    # 預設 pretty=True；若指定 compact 則 pretty=False
    if getattr(args, "compact", False):
        return False
    return True


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    try:
        if args.command == "stats" and args.kind == "demo":
            demo_cmd.run()
            print("完成：已產生 data/numbers.txt 與 data/scores.csv")
            return 0

        if args.command == "stats" and args.kind == "text":
            pretty = resolve_pretty(args)
            include_sorted = not args.no_sorted
            text_cmd.run(input_path=args.input, out_path=args.out, pretty=pretty, include_sorted=include_sorted)
            print(f"完成：{args.out}")
            return 0

        if args.command == "stats" and args.kind == "csv":
            pretty = resolve_pretty(args)
            include_sorted = not args.no_sorted
            csv_cmd.run(
                input_path=args.input,
                column=args.column,
                out_path=args.out,
                pretty=pretty,
                include_sorted=include_sorted,
            )
            print(f"完成：{args.out}")
            return 0

        print("錯誤：未知指令", file=sys.stderr)
        return 2
    except Exception as e:
        print(f"錯誤：{e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())