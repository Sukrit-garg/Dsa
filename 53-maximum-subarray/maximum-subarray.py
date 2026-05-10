class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        run_sum = nums[0]
        for i in range(1,len(nums)):
            run_sum = max(run_sum+nums[i],nums[i])
            max_sum = max(max_sum,run_sum)
        return max_sum