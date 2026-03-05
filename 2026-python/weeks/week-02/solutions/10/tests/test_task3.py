import os
import sys
import unittest

# Allow importing task files from parent directory when running unittest discover.
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from task3_log_summary import solve


class TestTask3LogSummary(unittest.TestCase):
    def test_sample_case(self):
        text = "\n".join(
            [
                "8",
                "alice login",
                "bob login",
                "alice view",
                "alice logout",
                "bob view",
                "bob view",
                "chris login",
                "bob logout",
            ]
        )
        expected = "\n".join(["bob 4", "alice 3", "chris 1", "top_action: login 3"])
        self.assertEqual(solve(text), expected)

    def test_empty_input_m0(self):
        self.assertEqual(solve("0"), "top_action: none 0")

    def test_action_tie_lexicographic(self):
        text = "\n".join(["2", "u1 view", "u2 login"])
        self.assertEqual(solve(text).splitlines()[-1], "top_action: login 1")


if __name__ == "__main__":
    unittest.main()
