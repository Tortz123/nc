# Time: O()
# Space: O()
# Approach - Length of set check
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(nums) > len(set(nums))
   