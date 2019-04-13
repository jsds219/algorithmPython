def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubble_sort([100, 4, 1, 3, 200, 5,3,4,1,2]))

def selection_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        maxIndex = 0
        for j in range(i+1):
            if arr[j] > arr[maxIndex]:
                maxIndex = j
        arr[i], arr[maxIndex] = arr[maxIndex], arr[i]
    return arr

print(selection_sort([100, 4, 1, 3, 200, 5,3,4,1,2]))

def mergeSort(arr):
    if len(arr) == 1:
        return arr
    a = arr[:int(len(arr)/2)]
    b = arr[int(len(arr)/2):]

    a = mergeSort(a)
    b = mergeSort(b)
    c = []
    i = 0
    j = 0

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    c += a[i:]
    c += b[j:]
    return c

print(mergeSort([100, 4, 1, 3, 200, 5,3,4,1,2]))
