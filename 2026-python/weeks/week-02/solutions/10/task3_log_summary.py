from collections import Counter
from typing import List, Tuple


Record = Tuple[str, str]


def parse_input(text: str) -> List[Record]:
    lines = [line.strip() for line in text.splitlines()]
    if not lines:
        return []

    m = int(lines[0] or 0)
    records: List[Record] = []
    for line in lines[1 : 1 + m]:
        if not line:
            continue
        user, action = line.split()
        records.append((user, action))
    return records


def summarize(records: List[Record]) -> Tuple[List[Tuple[str, int]], Tuple[str, int]]:
    user_counter = Counter(user for user, _ in records)
    action_counter = Counter(action for _, action in records)

    user_rows = sorted(user_counter.items(), key=lambda x: (-x[1], x[0]))

    if action_counter:
        top_action = sorted(action_counter.items(), key=lambda x: (-x[1], x[0]))[0]
    else:
        top_action = ("none", 0)

    return user_rows, top_action


def solve(text: str) -> str:
    records = parse_input(text)
    user_rows, top_action = summarize(records)

    lines = [f"{user} {count}" for user, count in user_rows]
    lines.append(f"top_action: {top_action[0]} {top_action[1]}")
    return "\n".join(lines)


if __name__ == "__main__":
    import sys

    print(solve(sys.stdin.read()))
