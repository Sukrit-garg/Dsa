class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        max_prod = nums[0]
        min_prod = nums[0]
        for i in range(1,len(nums)):
            temp = max_prod
            max_prod = max(max_prod*nums[i],nums[i],min_prod*nums[i])
            min_prod = min(min_prod*nums[i],nums[i],temp*nums[i])
            ans = max(max_prod,ans)
        return ans