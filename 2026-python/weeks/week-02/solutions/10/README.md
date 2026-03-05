# Week 02 Homework - 10

## 1. 完成題目清單

- [x] Task 1: Sequence Clean
- [x] Task 2: Student Ranking
- [x] Task 3: Log Summary

## 2. 執行方式

- Python 版本: `3.9+`

程式執行指令:

```bash
python task1_sequence_clean.py
python task2_student_ranking.py
python task3_log_summary.py
```

測試執行指令:

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

## 3. 資料結構選擇理由

- Task 1: 使用 `list` 保留原始順序、使用 `set` 只作為 membership 檢查，達成去重且不破壞順序。
- Task 2: 使用 `dataclass Student` 讓欄位意義清楚，再用 `sorted(..., key=...)` 完成多條件排序。
- Task 3: 使用 `Counter` 快速統計 user/action 次數，並搭配排序規則處理同次數 tie-break。

## 4. 遇到的錯誤與修正

- 錯誤: Task 2 一開始把同分時年齡排序寫成由大到小，導致案例不符規格。
- 修正: 將 key 改為 `(-score, age, name)`，確保年齡為由小到大。

## 5. Red -> Green -> Refactor 摘要

- Task 1:
  - Red: 先寫 `test_sample_case`，初版未處理空輸入，測試失敗。
  - Green: 補上 `parse_numbers` 的空字串分支，測試通過。
  - Refactor: 抽出 `format_line`，減少輸出字串重複邏輯。

- Task 2:
  - Red: 先寫同分 tie-break 測試，排序順序不符預期。
  - Green: 改用單一 key tuple `(-score, age, name)`。
  - Refactor: 用 `Student` dataclass 提高可讀性與維護性。

- Task 3:
  - Red: 先寫 `m=0` 測試，初版回傳格式不完整。
  - Green: 空輸入時固定輸出 `top_action: none 0`。
  - Refactor: 抽出 `summarize` 函式，讓解析與統計責任分離。
