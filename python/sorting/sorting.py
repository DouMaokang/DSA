def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return _merge(left, right)


def _merge(arr1, arr2):
    result = []

    while arr1 and arr2:
        if arr1[0] >= arr2[0]:
            result.append(arr1.pop(0))
        else:
            result.append(arr2.pop(0))

    if arr1:
        result += arr1
    if arr2:
        result += arr2

    return result


def insertion_sort(arr):
    """
    Insertion sort.

    Time complexity:
        Worst-case: O(n^2) when the original array is sorted in reverse order.
        Best-case: O(n) when the original array is already sorted.
    Space complexity: O(1).
    Stability: stable.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def selection_sort(arr):
    """
    Selection sort.

    Time complexity: O(n^2).
    Space complexity: O(1).
    Stability: not stable in default implementation.
    """
    for i in range(len(arr)):
        idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[idx]:
                idx = j
        # swap two elements
        arr[i], arr[idx] = arr[idx], arr[i]
    return arr


def bubble_sort(arr):
    """
    Bubble sort.

    Time complexity: O(n^2).
    Space complexity: O(1).
    Stability: stable.
    """
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):  # in i-th iteration, the last i elements are in their final positions
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def merge_sort_in_place(arr, left, right):
    if left >= right:
        return arr

    mid = left + (right - left) // 2
    merge_sort_in_place(arr, left, mid)  # [left, mid)
    merge_sort_in_place(arr, mid, right)  # [mid, right]
    _merge_in_place(arr, left, mid, right)


def _merge_in_place(arr, left, mid, right):
    if left == mid or mid == right:
        return


def quick_sort():
    pass


def bucket_sort():
    pass


def heap_sort():
    pass


if __name__ == '__main__':
    arr = [1, 3, 5, 7, 2, 4, 6, 8]
    print(bubble_sort(arr))
    print(merge_sort(arr))
    print(insertion_sort(arr))
    print(selection_sort(arr))
