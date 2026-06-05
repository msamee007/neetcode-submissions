class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        bs=[-1]*(len(nums)+1)
        for i in nums:
            if bs[i]==-1:
                bs[i]=1
            else:
                return i
        