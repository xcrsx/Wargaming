# Since one of the conditions was that the array could already be sorted,
# I decided to choose the Timsort algorithm, since it was designed to sort such data.


minrun = 64


def insertion_sort(arr, start, end):
    end += 1
    for i in range(start, end):
        cursor = arr[i]
        pos = i - 1

        while pos >= start and arr[pos] > cursor:
            arr[pos + 1] = arr[pos]
            pos -= 1

        arr[pos + 1] = cursor
    return arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])
    return merge(left, right, arr.copy())

def merge( left, right, merged):

    left_cursor, right_cursor = 0, 0
    cursor = 0
    while left_cursor < len(left) and right_cursor < len(right):
        if left[left_cursor] <= right[right_cursor]:
            merged[cursor] = left[left_cursor]
            left_cursor += 1
        else:
            merged[cursor] = right[right_cursor]
            right_cursor += 1
        cursor += 1
    
    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]

    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor+right_cursor] = right[right_cursor]
    return merged

def tim_sort(arr):
    n = len(arr)

    for start in range(0, n, minrun):
        end = min(start + minrun - 1, n - 1)
        arr = insertion_sort(arr, start, end)
 
    arr = merge_sort(arr)
    return arr




if __name__ == "__main__":
    import random
    arr = [random.randint(1, 90) for i in range(1000000)]
    check = arr.copy()
    check.sort()
    print(tim_sort(arr) == check)
    