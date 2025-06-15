class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currsum=sum(nums[:k])
        maxsum=currsum

        for i in range(k,len(nums)):
            currsum=currsum - nums[i-k] + nums[i]
            maxsum=max(maxsum, currsum)
        return maxsum/k