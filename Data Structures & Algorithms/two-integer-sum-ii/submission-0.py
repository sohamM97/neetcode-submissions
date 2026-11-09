class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start_idx = 0
        end_idx = len(numbers) - 1

        while start_idx < end_idx:
            sum = numbers[start_idx] + numbers[end_idx]
            if sum == target:
                return [start_idx+1, end_idx+1]
            if sum > target:
                end_idx -= 1
            elif sum < target:
                start_idx += 1