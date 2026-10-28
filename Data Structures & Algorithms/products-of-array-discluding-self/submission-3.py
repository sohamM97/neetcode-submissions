class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_products = [1]
        suffix_products = [1]
        results = []

        for i in range(1, len(nums)):
            prefix_products.append(nums[i-1] * prefix_products[-1])

        for i in range(len(nums)-1, 0, -1):
            suffix_products.append(nums[i] * suffix_products[-1])
            
        # print(prefix_products)
        # print(suffix_products)

        for i in range(len(nums)):
            results.append(prefix_products[i] * suffix_products[len(nums)-i-1])

        return results