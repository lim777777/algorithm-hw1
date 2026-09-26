"""세 정렬을 같은 입력에서 측정하고 CSV를 표준 출력으로 내보낸다."""

import random
import statistics
import sys
from pathlib import Path
from time import perf_counter_ns


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from sort import heap_sort, insertion_sort, merge_sort  # noqa: E402


REPETITIONS = 5
SIZES = (1_000, 3_000, 5_000, 10_000)
ALGORITHMS = (insertion_sort, merge_sort, heap_sort)


def make_input(input_type, size, seed):
    rng = random.Random(seed)
    if input_type == "sorted":
        return list(range(size))
    if input_type == "reversed":
        return list(range(size, 0, -1))
    if input_type == "few_unique":
        return [rng.randrange(8) for _ in range(size)]
    return [rng.randrange(size * 4) for _ in range(size)]


def benchmark(algorithm, original):
    samples = []
    expected = sorted(original)
    for _ in range(REPETITIONS):
        values = original.copy()
        start = perf_counter_ns()
        algorithm(values)
        elapsed = perf_counter_ns() - start
        if values != expected:
            raise RuntimeError(f"{algorithm.__name__} 정렬 결과가 올바르지 않습니다.")
        samples.append(elapsed / 1_000_000)
    return statistics.median(samples)


def main():
    print("input_type,n,algorithm,median_ms")
    for input_type in ("random", "sorted", "reversed", "few_unique"):
        for size_index, size in enumerate(SIZES):
            original = make_input(input_type, size, 20260926 + size_index)
            for algorithm in ALGORITHMS:
                median = benchmark(algorithm, original)
                print(f"{input_type},{size},{algorithm.__name__},{median:.6f}")


if __name__ == "__main__":
    main()
