def linear_search(arr,item):
    for i in range(0,len(arr)):
        if(arr[i] == item):
            return i
    return -1

if __name__ == '__main__':
    import sys

    user_input = input("enter the elements with a comma: \n").strip()
    arr= [int(item) for item in user_input.split(",")]

    item = input("enter the element to be searched: \n")
    item = int(item)

    result = linear_search(arr,item)
    print("{} is at index {}".format(item,result))
    
