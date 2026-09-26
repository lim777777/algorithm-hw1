"""세 정렬의 실행 결과 확인. 실행: make run-py"""

from sort import heap_sort, insertion_sort, merge_sort

if __name__ == "__main__":
    data = [6, 8, 5, 9, 10, 1, 7, 2, 4, 3]
    algorithms = (insertion_sort, merge_sort, heap_sort)

    for algorithm in algorithms:
        result = data.copy()
        algorithm(result)
        print(f"{algorithm.__name__:14}:", " ".join(str(x) for x in result))
