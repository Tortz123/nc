# Time: O(n)
# Space: O(n)
# Approach: Bucket Sort, count freq of each element. make array of buckets, index: count of freq
#           value: the element. traverse list backwards and return top k
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        arr = [[] for i in range(len(nums) + 1)]
        res = []
        
        # first thing is to count the occurences of each num
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        # now bucket sort
        # iterate over hashmap and store count and value into buckets
        # so i need the key and value
        for n, v in freq.items():
            arr[v].append(n)
        
        # iterating through freq list backwards
        for i in range(len(arr) - 1, 0, -1):
            for n in arr[i]:
                res.append(n)
                if len(res) == k:
                    return res
    

        
       