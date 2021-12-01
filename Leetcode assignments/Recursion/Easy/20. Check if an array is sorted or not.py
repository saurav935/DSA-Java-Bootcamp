def sort_check(arr,index):
    if index == len(arr):
        return True
    elif arr[index] < arr[index-1]:
        return False
    else:
        return sort_check(arr,index+1)
