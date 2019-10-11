def partition(arr,low,high):
    i = low
    j = high
    pivot = arr[i]
    while i<=j :
        while arr[i]<pivot :
            i+=1
        while arr[j]>pivot :
            j-=1
        if i<=j:
            arr[i],arr[j] = arr[j],arr[i]
            i+=1
            j-=1
    return j

def quick(arr,low,high):
    j = partition(arr,low,high)
    if low < j-1:
        quick(arr,low,j-1)
    if high > j:
        quick(arr,j+1,high)
    
