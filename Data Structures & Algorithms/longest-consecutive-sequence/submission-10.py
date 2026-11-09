class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Optimal

        nums_set = set(nums)
        lcs = 0

        for num in nums_set:
            if num - 1 not in nums_set:
                cur_lcs = 1
                while num + cur_lcs in nums_set:
                    cur_lcs += 1

                lcs = max(lcs, cur_lcs)

        return lcs
