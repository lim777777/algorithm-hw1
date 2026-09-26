"""유닛 테스트 — 표준 라이브러리의 unittest만 쓴다.

실행: make test-py
"""

import sys
import unittest
from pathlib import Path

# src/를 import 경로에 넣는다. 패키지로 만들지 않아도 되도록.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from sort import heap_sort, insertion_sort, merge_sort  # noqa: E402


ALGORITHMS = (insertion_sort, merge_sort, heap_sort)


class TestSortingAlgorithms(unittest.TestCase):
    CASES = (
        ([6, 8, 5, 9, 10, 1, 7, 2, 4, 3], list(range(1, 11))),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([3, 1, 3, 1, 2], [1, 1, 2, 3, 3]),
        ([0, -3, 5, -1, 2], [-3, -1, 0, 2, 5]),
        ([42], [42]),
        ([], []),
    )

    def test_sorting_cases(self):
        for algorithm in ALGORITHMS:
            for values, expected in self.CASES:
                with self.subTest(algorithm=algorithm.__name__, values=values):
                    actual = values.copy()
                    self.assertIs(algorithm(actual), actual)
                    self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
