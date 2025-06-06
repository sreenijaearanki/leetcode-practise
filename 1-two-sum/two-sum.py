class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # num1(already in map) + curr_num = target

        hm={}
        for i,num in enumerate(nums):
            num1=target-num
            if num1 in hm:
                return [hm[num1], i]
            hm[num]=i
        
        return []
