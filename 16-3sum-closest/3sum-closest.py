class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res=float('inf')
        for i in range(len(nums)-2):
            left=i+1
            right=len(nums)-1
            while left<right:
                curr_sum = nums[i]+nums[left]+nums[right]
                if abs(target-curr_sum)<abs(target-res):
                    res=curr_sum
                if curr_sum < target:
                    left+=1
                elif curr_sum > target:
                    right-=1
                else:
                    return curr_sum
        return res