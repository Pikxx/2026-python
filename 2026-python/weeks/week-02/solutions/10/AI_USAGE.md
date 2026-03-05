# AI_USAGE

## 1. 我問了哪些問題

- 如何在不破壞順序下做去重？
- `sorted(..., key=...)` 多條件排序要怎麼寫才正確？
- `Counter` 與 `defaultdict` 在統計題的取捨是什麼？
- `groupby` 在什麼情況下會分組錯誤？
- 如何設計邊界測試案例（空輸入、同分、同次數）？

## 2. 我採用的 AI 建議

- Task 1 使用 `seen + list` 實作去重保序。
- Task 2 排序 key 使用 `(-score, age, name)`。
- Task 3 使用 `Counter` 計數，並以 `(-count, name)` 做 tie-break。

## 3. 我拒絕的 AI 建議

- 拒絕直接用 `set(nums)` 當作去重輸出，因為會破壞原順序，不符合規格。
- 拒絕手寫雙層迴圈交換排序，改用 `sorted` 滿足作業限制。

## 4. AI 可能誤導但我自行修正

- 誤導點: AI 曾建議 Task 2 同分時年齡由大到小排序。
- 問題: 與題目規格（年齡由小到大）衝突。
- 修正: 實測後改為 `(-score, age, name)`，並補上對應測試防止回歸。
