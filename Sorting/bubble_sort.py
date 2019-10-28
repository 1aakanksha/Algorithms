def bubble_sort(collection):
    length = len(collection)
    for i in range(length):
        swapped = False
        for j in range(length-1):
            if collection[j] > collection[j+1]:
                swapped = True
                collection[j], collection[j+1] = collection[j+1], collection[j]
        if not swapped: break 
    return collection


if __name__ == '__main__':
    arr=[2,1,6,4,7,5,9,3]
    print(bubble_sort(arr))