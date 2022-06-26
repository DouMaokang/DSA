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


def insertion_sort():
    pass


def bucket_sort():
    pass


def heap_sort():
    pass


if __name__ == '__main__':
    arr = [1, 3, 5, 7, 2, 4, 6, 8]
    print(merge_sort(arr))
