class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d={0:1}
        res=0
        presum=0
        for num in nums:
            presum += num
            if presum - k in d:
                res+=d[presum - k]
            if presum not in d:
                d[presum]=1
            else:
                d[presum]+=1
        return res