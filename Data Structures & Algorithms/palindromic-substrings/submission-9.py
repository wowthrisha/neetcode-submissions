class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        def countPali(l, r):
            count = 0

            while l >= 0 and r < n and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

            return count

        result = 0

        for i in range(n):
            result += countPali(i, i)       # odd center
            result += countPali(i, i + 1)   # even center

        return result