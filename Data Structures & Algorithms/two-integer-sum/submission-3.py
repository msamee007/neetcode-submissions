class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            res=target-nums[i]
            if res in d:
                return [d[res],i]
            d[nums[i]]=i

        
