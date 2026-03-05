# TEST_CASES

## Case 1: Task 1 一般情況

- 對應測試: `tests/test_task1.py::test_sample_case`
- 輸入:

```text
5 3 5 2 9 2 8 3 1
```

- 預期輸出:

```text
dedupe: 5 3 2 9 8 1
asc: 1 2 2 3 3 5 5 8 9
desc: 9 8 5 5 3 3 2 2 1
evens: 2 2 8
```

- 實際輸出: 與預期一致
- 結果: PASS
- 關鍵修改點: 補上去重流程中 `seen` 判斷，保留第一次出現順序。

## Case 2: Task 1 邊界情況（空輸入）

- 對應測試: `tests/test_task1.py::test_empty_input`
- 輸入:

```text
(空字串)
```

- 預期輸出:

```text
dedupe:
asc:
desc:
evens:
```

- 實際輸出: 與預期一致
- 結果: PASS
- 關鍵修改點: `parse_numbers` 增加 `if not text` 分支。

## Case 3: Task 2 同分排序情況

- 對應測試: `tests/test_task2.py::test_tie_break_by_name`
- 輸入:

```text
3 3
ian 88 19
bob 88 19
amy 88 19
```

- 預期輸出:

```text
amy 88 19
bob 88 19
ian 88 19
```

- 實際輸出: 與預期一致
- 結果: PASS
- 關鍵修改點: key 內加入 `name` 作為第三排序條件。

## Case 4: Task 3 反例（top action 次數相同）

- 對應測試: `tests/test_task3.py::test_action_tie_lexicographic`
- 輸入:

```text
2
u1 view
u2 login
```

- 預期輸出末行:

```text
top_action: login 1
```

- 實際輸出末行: `top_action: login 1`
- 結果: PASS
- 關鍵修改點: action 排序採 `(-count, action)`，同次數時字母序較小者優先。

## Case 5: 最容易出錯的一組（Task 2 綜合排序）

- 對應測試: `tests/test_task2.py::test_sample_case_top3`
- 輸入:

```text
6 3
amy 88 20
bob 88 19
zoe 92 21
ian 88 19
leo 75 20
eva 92 20
```

- 預期輸出:

```text
eva 92 20
zoe 92 21
bob 88 19
```

- 實際輸出: 與預期一致
- 結果: PASS
- 關鍵修改點: 同分時先比年齡，再比姓名，不能只看分數。
