def searchInsert(nums, target: int) -> int:
    left,right=0,len(nums)-1
    while left<=right:
        mid=(left+right)//2
        if nums[mid]<=target:
            left=mid+1
        else:
            right=mid-1
    return left

nums = [3,3,3,3,4]
target = 2
print(searchInsert(nums,target))