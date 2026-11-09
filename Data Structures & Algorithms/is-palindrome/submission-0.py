class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        def isalnum(char):
            return 'a' <= char <= 'z' or 'A' <= char <= 'Z' or '0' <= char <= '9'
        
        start_idx = 0
        end_idx = len(s) - 1

        while start_idx < end_idx:
            if not isalnum(s[start_idx]):
                start_idx += 1
            elif not isalnum(s[end_idx]):
                end_idx -= 1
            elif s[start_idx].lower() != s[end_idx].lower():
                return False
            else:
                start_idx += 1
                end_idx -= 1
        
        return True