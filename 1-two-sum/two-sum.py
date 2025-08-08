class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # use a map and check if the target - curr elem is in the map, if there then return those 2 indices

        hm={}
        for i,num in enumerate(nums):
            if target-num in hm:
                return [hm[target-num], i]
            hm[num]=i