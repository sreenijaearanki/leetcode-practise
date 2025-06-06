class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hs=set()
        for num in nums:
            if num not in hs:
                hs.add(num)
            else:
                return True
        return False