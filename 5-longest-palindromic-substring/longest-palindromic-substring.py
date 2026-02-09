class Solution:
        def longestPalindrome(self, s: str) -> str:
            if len(s) <= 1:
                return s

            def expand(left, right):
                while left >= 0 and right < len(s):
                    if s[left] == s[right]:
                        left -= 1
                        right += 1
                    else:
                        break
                return s[left+1:right]
            
            longest_pal = ""

            for i in range(len(s)):
                odd_pal = expand(i, i)
                even_pal = expand(i, i+1)
                
                if len(odd_pal) > len(longest_pal):
                    longest_pal = odd_pal
                if len(even_pal) > len(longest_pal):
                    longest_pal = even_pal
            
            return longest_pal