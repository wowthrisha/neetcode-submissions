class Solution:
    def isPalindrome(self, s: str) -> bool:
        t=''.join(c.lower() for c in s if c.isalnum())
        if t==t[::-1]:
            return True
        else:
            return False