class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        curr_sum=0
        seen=set()
        left=0
        max_sum=0

        for right in range(len(nums)):
            while nums[right] in seen:
                seen.remove(nums[left])
                curr_sum-=nums[left]
                left+=1
            seen.add(nums[right])
            curr_sum+=nums[right]

            if right-left+1 ==k:
                max_sum=max(curr_sum, max_sum)
                seen.remove(nums[left])
                curr_sum-=nums[left]
                left+=1
        return max_sum
