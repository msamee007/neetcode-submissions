class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if target in nums:
            return 1
        elif sum(nums)==target:
            return len(nums)
        s=float('inf')
        l=r=0
        while r!=len(nums):
            a=nums[l:r+1]
            if sum(a)<target:
                r+=1
            elif sum(a)>=target:
                if len(a)<s:
                    s=len(a)
                l+=1
        if s==float('inf'):
            return 0
        return s
