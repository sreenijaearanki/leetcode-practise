class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lsum=0
        rsum= sum(num for num in nums)

        for i in range(len(nums)):
            rsum -= nums[i]
            if lsum == rsum:
                return i
            lsum+=nums[i]
        return -1