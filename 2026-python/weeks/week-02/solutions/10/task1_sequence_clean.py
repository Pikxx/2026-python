from typing import List


def parse_numbers(text: str) -> List[int]:
    text = text.strip()
    if not text:
        return []
    return [int(part) for part in text.split()]


def dedupe_preserve_order(nums: List[int]) -> List[int]:
    seen = set()
    result = []
    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result


def format_line(label: str, nums: List[int]) -> str:
    body = " ".join(str(x) for x in nums)
    return f"{label}: {body}" if body else f"{label}:"


def solve(text: str) -> str:
    nums = parse_numbers(text)
    dedupe = dedupe_preserve_order(nums)
    asc = sorted(nums)
    desc = sorted(nums, reverse=True)
    evens = [x for x in nums if x % 2 == 0]

    lines = [
        format_line("dedupe", dedupe),
        format_line("asc", asc),
        format_line("desc", desc),
        format_line("evens", evens),
    ]
    return "\n".join(lines)


if __name__ == "__main__":
    import sys

    print(solve(sys.stdin.read()))
