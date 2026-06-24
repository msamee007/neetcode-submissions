class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        cnt1 = cnt2 = cand1 = cand2 = 0

        for num in nums:
            if cnt1 == 0 and cand2 != num:
                cand1 = num
                cnt1 += 1
            elif cnt2 == 0 and cand1 != num:
                cand2 = num
                cnt2 += 1
            elif cand1 == num:
                cnt1 += 1
            elif cand2 == num:
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        
        cnt1 = cnt2 = 0

        for num in nums:
            if cand1 == num:
                cnt1 += 1
            elif cand2 == num:
                cnt2 += 1
        result = []
        
        if cnt1 > len(nums) / 3:
            result.append(cand1)
        if cnt2 > len(nums) / 3:
            result.append(cand2)
        
        return result

        
        