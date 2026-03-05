import os
import sys
import unittest

# Allow importing task files from parent directory when running unittest discover.
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from task1_sequence_clean import dedupe_preserve_order, solve


class TestTask1SequenceClean(unittest.TestCase):
    def test_sample_case(self):
        text = "5 3 5 2 9 2 8 3 1"
        expected = "\n".join(
            [
                "dedupe: 5 3 2 9 8 1",
                "asc: 1 2 2 3 3 5 5 8 9",
                "desc: 9 8 5 5 3 3 2 2 1",
                "evens: 2 2 8",
            ]
        )
        self.assertEqual(solve(text), expected)

    def test_empty_input(self):
        expected = "\n".join(["dedupe:", "asc:", "desc:", "evens:"])
        self.assertEqual(solve(""), expected)

    def test_dedupe_order_kept(self):
        self.assertEqual(dedupe_preserve_order([2, 1, 2, 1, 3]), [2, 1, 3])


if __name__ == "__main__":
    unittest.main()
