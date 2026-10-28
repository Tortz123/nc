# Time: O(n)
# Space: O(1)
# Approach: Two Pointers, return false if l != right using custom function
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.isAlphaNum(s[l]):
                l += 1

            while r > l and not self.isAlphaNum(s[r]):
                r -= 1
                
            if s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1

        return True 
    # check if character is between the asci values A-Z, a-z, and 0-9  
    def isAlphaNum(self, c: char):
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))
