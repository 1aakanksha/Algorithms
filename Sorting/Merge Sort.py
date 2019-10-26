def mergeSort(arr):
    if len(arr) == 1:
        return arr
    m = int(len(arr) / 2)
    l = arr[:m]
    r = arr[m:]
    l = mergeSort(l)
    r = mergeSort(r)
    arr = merge(l, r)
    return arr


def merge(arr1, arr2):
    i = 0
    j = 0
    merged_array = []
    while len(merged_array) != len(arr1) + len(arr2):
        if arr1[i] <= arr2[j]:
            merged_array.append(arr1[i])
            if i < len(arr1) - 1:
                i += 1
            else:
                merged_array = merged_array + arr2[j:]
                break
        else:
            merged_array.append(arr2[j])

            if j < len(arr2) - 1:
                j += 1
            else:
                merged_array = merged_array + arr1[i:]
                break
    return (merged_array)


if __name__ == "__main__":
    arr=[2,1,6,4,7,5,9,3]
    print(mergeSort(arr))
