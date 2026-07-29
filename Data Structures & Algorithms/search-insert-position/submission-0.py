class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i,j=0,len(nums)-1
        if nums[0]>target:
            return 0
        elif nums[-1]<target:
            return len(nums)
        while i<=j:
                mid=(i+j)//2
                if target>nums[mid]:
                    i=mid+1
                elif target<nums[mid]:
                    j=mid-1
                else:
                    return mid
        return i