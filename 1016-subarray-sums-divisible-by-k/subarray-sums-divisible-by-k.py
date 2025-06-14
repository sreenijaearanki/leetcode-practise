class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix=0
        d=defaultdict(int)
        d[0]=1
        ans=0
        for num in nums:
            prefix+=num
            target=prefix % k
            if target<0:
                target+=k
            ans+=d[target]
            d[target]+=1
        return ans