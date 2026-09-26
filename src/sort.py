"""과제에서 비교할 세 정렬 알고리즘."""


def insertion_sort(a):
    """삽입 정렬로 a를 제자리에서 오름차순 정렬한다."""
    for i in range(1, len(a)):
        value = a[i]
        j = i - 1
        while j >= 0 and a[j] > value:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = value
    return a


def merge_sort(a):
    """병합 정렬로 a를 제자리에서 오름차순 정렬한다."""
    temp = [0] * len(a)

    def sort_range(left, right):
        if right - left <= 1:
            return

        middle = left + (right - left) // 2
        sort_range(left, middle)
        sort_range(middle, right)

        i, j, k = left, middle, left
        while i < middle and j < right:
            if a[i] <= a[j]:
                temp[k] = a[i]
                i += 1
            else:
                temp[k] = a[j]
                j += 1
            k += 1

        while i < middle:
            temp[k] = a[i]
            i += 1
            k += 1
        while j < right:
            temp[k] = a[j]
            j += 1
            k += 1
        a[left:right] = temp[left:right]

    sort_range(0, len(a))
    return a


def heap_sort(a):
    """힙 정렬로 a를 제자리에서 오름차순 정렬한다."""

    def sift_down(root, end):
        while root * 2 + 1 < end:
            child = root * 2 + 1
            if child + 1 < end and a[child] < a[child + 1]:
                child += 1
            if a[root] >= a[child]:
                return
            a[root], a[child] = a[child], a[root]
            root = child

    n = len(a)
    for root in range(n // 2 - 1, -1, -1):
        sift_down(root, n)
    for end in range(n - 1, 0, -1):
        a[0], a[end] = a[end], a[0]
        sift_down(0, end)
    return a
