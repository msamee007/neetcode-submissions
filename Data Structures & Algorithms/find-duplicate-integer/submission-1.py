class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        s=0
        for i in range(1,len(nums)+1):
            if s==nums[i-1]:
                return nums[i-1]
            s=nums[i-1]