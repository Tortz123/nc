# Time: O(m * nlogn)
# Space: O(m * n)
# m -> number of strings, n -> length of longest string
# Approach: sort each string, if sorted string in hashmap append orignal string to value,
#           if doesnt not exist create empty list value 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for s in strs:
            sorted_str = "".join(sorted(s))
            # if key is missing, it automatically creates []
            hashmap[sorted_str].append(s)
        
        return list(hashmap.values())
        