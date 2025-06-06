class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm={}
        for i,num in enumerate(nums):
            elem = target - num
            if elem in hm:
                return [hm[elem],i]
            hm[num]=i
        return []