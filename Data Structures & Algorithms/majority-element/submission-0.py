class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l=set(nums)
        for i in l:
            if nums.count(i)> len(nums)//2:
                return i