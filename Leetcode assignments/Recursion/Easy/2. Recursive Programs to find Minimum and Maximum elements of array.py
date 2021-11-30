
def min_max(arr,mins,maxs,index):
    if index == len(arr):
        return ("Min: ", mins, "Max: ", maxs)
    else:
        return min_max(arr,min(mins,arr[index]),max(maxs,arr[index]),index+1)
