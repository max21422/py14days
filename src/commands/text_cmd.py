from pathlib import Path

from src.report_utils import write_json_report
from src.stats_utils import parse_numbers, summary


def run(input_path: str, out_path: str, pretty: bool = True, include_sorted: bool = True) -> None:
    in_path = Path(input_path)

    if not in_path.exists():
        raise FileNotFoundError(f"找不到輸入檔：{in_path.resolve()}")

    text = in_path.read_text(encoding="utf-8")
    nums = parse_numbers(text)

    info = summary(nums, include_sorted=include_sorted)
    write_json_report(info, out_path=out_path, pretty=pretty)