# Time: O(n)
# Space: O(n)
# Approach: Hashmap. Iterate over elements, check if difference is in hashmap, and return index if true
#           otherwise add difference the hashmap.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in hashmap:
                return [hashmap[difference], i]
            else:
                hashmap[nums[i]] = i
        return []