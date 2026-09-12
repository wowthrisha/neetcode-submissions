class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        if n == 1:
            return s

        def check(left, right):
            best_length = 0
            best_left = 0
            best_right = 0

            while left >= 0 and right < n and s[left] == s[right]:
                current_length = right - left + 1

                if current_length > best_length:
                    best_length = current_length
                    best_left = left
                    best_right = right

                left -= 1
                right += 1

            return best_length, best_left, best_right

        max_length = 0
        max_left = 0
        max_right = 0

        for i in range(n):
            odd = check(i, i)
            even = check(i, i + 1)

            if odd[0] > max_length:
                max_length, max_left, max_right = odd

            if even[0] > max_length:
                max_length, max_left, max_right = even

        return s[max_left:max_right + 1]