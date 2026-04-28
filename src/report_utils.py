import json
from pathlib import Path
from typing import Any


def write_json_report(data: Any, out_path: str, pretty: bool = True) -> None:
    outp = Path(out_path)
    outp.parent.mkdir(parents=True, exist_ok=True)

    if pretty:
        text = json.dumps(data, ensure_ascii=False, indent=2)
    else:
        text = json.dumps(data, ensure_ascii=False, separators=(",", ":"))

    outp.write_text(text, encoding="utf-8")