from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        l=[]
        d=Counter(nums)
        for i,j in d.items():
            if j>(len(nums)//3):
                l.append(i)
        return l
