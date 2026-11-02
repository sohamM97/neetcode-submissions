class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = sorted(set(nums))
        print(nums_set)
        lcs = 0
        cur_lcs = 0

        for i in range(len(nums_set)):
            if cur_lcs == 0 or nums_set[i] == nums_set[i-1] + 1:
                cur_lcs += 1
            else:
                if cur_lcs > lcs:
                    lcs = cur_lcs
                cur_lcs = 1

        if cur_lcs > lcs:
            lcs = cur_lcs

        return lcs
