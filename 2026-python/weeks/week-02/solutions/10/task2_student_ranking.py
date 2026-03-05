from dataclasses import dataclass
from typing import List, Tuple


@dataclass(frozen=True)
class Student:
    name: str
    score: int
    age: int


def parse_input(text: str) -> Tuple[int, List[Student]]:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if not lines:
        return 0, []

    n, k = map(int, lines[0].split())
    students = []
    for line in lines[1 : 1 + n]:
        name, score, age = line.split()
        students.append(Student(name=name, score=int(score), age=int(age)))
    return k, students


def rank_students(students: List[Student]) -> List[Student]:
    return sorted(students, key=lambda s: (-s.score, s.age, s.name))


def solve(text: str) -> str:
    k, students = parse_input(text)
    ranked = rank_students(students)[:k]
    return "\n".join(f"{s.name} {s.score} {s.age}" for s in ranked)


if __name__ == "__main__":
    import sys

    print(solve(sys.stdin.read()))
