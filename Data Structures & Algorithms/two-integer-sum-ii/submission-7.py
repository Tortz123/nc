# Time: O(n)
# Space: O(1)
# Approach: Two Pointers - Since list is sorted we have two pointers l, r. Calculate the sum of l and r. If
#           sum is larger than target we decrement r otherwise increment l. Then return indices of l and r
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            sum = numbers[l] + numbers[r]

            if sum < target:
                l += 1
            if sum > target:
                r -= 1
            if sum == target:
                return [l + 1, r + 1] 

        return []


        