class Solution:
    def merge(self, intervals):
        # if not intervals:
        #     return []

        intervals.sort()  # ✅ Automatically sorts by start times

        merged = [intervals[0]]  # Start with the first interval

        for current in intervals[1:]:
            last = merged[-1]

            # If current interval overlaps with last, merge them
            if current[0] <= last[1]:
                last[1] = max(last[1], current[1])
            else:
                merged.append(current)

        return merged
