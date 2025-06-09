class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1
        while low<high:
            mid = low + (high-low)//2
            # if nums[low] < nums[mid]:
            #     low = mid + 1
            # else:
            #     high = mid
            # the above aproach fails because when low=mid then we might actually miss the min because we are not checking equivalent
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        return nums[low]