#prerequisite: array should be sorted
#to sort an array, sort method could be used
#in this script, you need not to sort array explicitely

#to run the script
# python binary_search.py in cmd

def binary_search(arr,low,high,item):                   #high is the length of array
    mid = low + (high-low)//2                           #calculate the mid index of array
    if high<low:
        return -1                                        #base case
    else:
        if arr[mid] == item:
            return mid
        elif arr[mid] > item:
            return binary_search(arr,low,mid-1,item)             #recusrsion
        else:
            return binary_search(arr,mid+1,high,item)

if __name__ == '__main__':
    import sys
    user_input = input("enter values separated by comma: ").strip()       #input the array
    arr = [int(item) for item in user_input.split(',')]                   #list compressions

#sort the array to apply binart search
    arr.sort()

    item = input("enter the number to search: \n")
    item = int(item)

    low = input("enter the lower index: \n")
    low = int(low)

    high = input("enter the highest index: \n")
    high = int(high)

    result = binary_search(arr,low,high,item)

    if result is not None:
        print('{} is found at index {}'.format(item,result) )
    else:
        print('not found')


#example
#move to directory where the file is stored
#in cmd type - python binary_search.py
