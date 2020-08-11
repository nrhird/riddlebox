def flip(array, i):
    start = 0
    while start < i:
        t = array[start]
        array[start] = array[i]
        array[i] = t
        start += 1
        i -= 1


def findMaximumIndex(arr, n):
    max_index = 0
    for i in range(0, n):
        if arr[i] > arr[max_index]:
            max_index = i
    return max_index


def pancakeSort(arr):
    curr_size = len(arr)
    while curr_size > 1:
        max_index = findMaximumIndex(arr, curr_size)
        if max_index != curr_size - 1:
            flip(arr, max_index)
            flip(arr, curr_size - 1)
        curr_size -= 1


if __name__ == "__main__":
    array = ["Z", "Y", "X", "C", "B", "A"]
    pancakeSort(array)
    print(array)
