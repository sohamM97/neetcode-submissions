class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counts = {}
        t_counts = {}

        for letter in s:
            if not letter in s_counts:
                s_counts[letter] = 1
            else:
                s_counts[letter] += 1

        for letter in t:
            if not letter in t_counts:
                t_counts[letter] = 1
            else:
                t_counts[letter] += 1

         
        return s_counts == t_counts