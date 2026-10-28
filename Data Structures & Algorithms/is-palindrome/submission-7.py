# Time: O(n)
# Space: O(n)
# Approach: strip string to alpha numerical characters then, reverse the string then compare with orginal
class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr = ""
        for c in s:
            if c.isalnum():
                newstr += c.lower()
        return newstr == newstr[::-1]
