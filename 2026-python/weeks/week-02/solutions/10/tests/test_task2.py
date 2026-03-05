import os
import sys
import unittest

# Allow importing task files from parent directory when running unittest discover.
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from task2_student_ranking import Student, rank_students, solve


class TestTask2StudentRanking(unittest.TestCase):
    def test_sample_case_top3(self):
        text = "\n".join(
            [
                "6 3",
                "amy 88 20",
                "bob 88 19",
                "zoe 92 21",
                "ian 88 19",
                "leo 75 20",
                "eva 92 20",
            ]
        )
        expected = "\n".join(["eva 92 20", "zoe 92 21", "bob 88 19"])
        self.assertEqual(solve(text), expected)

    def test_tie_break_by_name(self):
        students = [
            Student("ian", 88, 19),
            Student("bob", 88, 19),
            Student("amy", 88, 19),
        ]
        ranked = rank_students(students)
        self.assertEqual([s.name for s in ranked], ["amy", "bob", "ian"])

    def test_k_larger_than_n(self):
        text = "\n".join(["2 5", "amy 90 20", "bob 80 19"])
        expected = "\n".join(["amy 90 20", "bob 80 19"])
        self.assertEqual(solve(text), expected)


if __name__ == "__main__":
    unittest.main()
