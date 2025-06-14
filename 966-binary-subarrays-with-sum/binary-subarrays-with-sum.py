class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix=0
        d=defaultdict(int)
        d[0]=1
        res=0
        for i in range(len(nums)):
            prefix+=nums[i]
            target=prefix-goal
            if target in d:
                res+=d[target]
            d[prefix]+=1
        return res