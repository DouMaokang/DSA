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



if __name__ == '__main__':
    arr = [1, 3, 5, 7, 2, 4, 6, 8]
    print(merge_sort(arr))
