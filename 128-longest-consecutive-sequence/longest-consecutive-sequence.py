class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)
        longest=0
        for num in numset:
            if num-1 not in numset:
                curr=num
                count=1
                while curr+1 in numset:
                    curr+=1
                    count+=1
                longest=max(longest, count)

        return longest