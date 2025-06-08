class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # kadane's algorithm
        # we init with nums[0] bcaz array can have all negative elem then having 0 will be wrong
        # and the other reason is the first elem is a valid subarray, we can have only one elem so in that case it is better to init both sums with the first elem
        curr_sum=nums[0]
        max_sum=nums[0]
        for i in range(1, len(nums)):
            curr_sum = max(nums[i],curr_sum +nums[i])
            max_sum =max(max_sum, curr_sum)
        return max_sum