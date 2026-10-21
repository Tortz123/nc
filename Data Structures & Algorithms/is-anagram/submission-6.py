# Time:  O(nlog(n) + mlog(m))
# Space: O(n + m)
# Approach: Sort both strings then compare 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
        