

def traingle(nums,index,arr,temp):
    if len(nums) == 1:
        return arr
    elif index == len(nums)-1:
        temp.append(nums[index]+nums[index-1])
        arr.append(temp)
        return traingle(temp,1,arr,[])
    elif index != len(nums)-1:
        temp.append(nums[index]+nums[index-1])
        return traingle(nums,index+1,arr,temp)

nums = [1,2,3,4,5]
print(traingle(nums,1,[nums],[]))
