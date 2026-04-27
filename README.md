# py14days

Python 練習專案（Day01–Day12）＋簡單的數字/統計工具（讀 TXT/CSV，輸出 JSON 報表），並使用 pytest 做單元測試。

## Requirements
- Python 3.x

## Setup (Windows)
```powershell
cd E:\pyton\AI\py14days
python -m venv .venv
.\.venv\Scripts\activate
python -m pip install -U pip
pip install -r requirements.txt
```

## Run examples
### Day08：讀取 TXT 統計
```powershell
python src\day08_read_txt.py
```

### Day10：讀取 CSV 欄位統計並輸出 JSON
```powershell
python src\day10_read_csv_stats.py
```

### Day11：CSV 欄位統計工具（可指定欄位）
```powershell
python src\day11_csv_tool.py -i data\scores.csv -c score -o out\report.json
```

## Run tests
```powershell
python -m pytest -v
```