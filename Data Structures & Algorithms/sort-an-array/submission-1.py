class Solution:
 def sortArray(self, nums: List[int]) -> List[int]:
    # base case: array of 1 element is already sorted
    if len(nums) <= 1:
        return nums
    # find the middle point
    mid = len(nums) // 2
    # split into left and right halves
    left = self.sortArray(nums[:mid])
    right = self.sortArray(nums[mid:])
    # merge the two sorted halves
    return merge(left, right)
def merge(left, right):
    result = []
    i = 0  # pointer for left half
    j = 0  # pointer for right half
    
    # compare elements one by one from both halves
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # one half will finish first
    # append whatever remains in the other half
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result