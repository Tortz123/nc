# Time: O(nlogn)
# Space: O(1)
# Approach - Sort list first then walk through to find duplicate 
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False
       