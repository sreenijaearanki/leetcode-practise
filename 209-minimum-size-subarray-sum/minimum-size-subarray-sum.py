class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums)<target:
            return 0
        start=0
        last=0
        res=len(nums)
        for i,num in enumerate(nums):
            start+=num
            while start>=target:
                start-=nums[last]
                res=min(res, i-last+1)
                last+=1
        return res