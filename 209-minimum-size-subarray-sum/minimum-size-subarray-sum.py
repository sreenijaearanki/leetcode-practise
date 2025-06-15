class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0               # The window starts from index 0
        curr_sum = 0            # This will keep the sum of elements in the window
        min_len = float('inf')  # Start with a very big number; we’ll shrink it

        for end in range(len(nums)):
            curr_sum += nums[end]  # Add current box value to the sum

            # While sum is enough or more, try shrinking the window
            while curr_sum >= target:
                min_len = min(min_len, end - start + 1)  # Update answer if current window is smaller
                curr_sum -= nums[start]  # Remove the box at the beginning of the window
                start += 1              # Move the start of the window forward

        # If we never found a valid window, return 0
        if min_len == float('inf'):
            return 0
        else:
            return min_len
