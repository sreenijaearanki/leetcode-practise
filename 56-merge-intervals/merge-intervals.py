class Solution:
    def merge(self, intervals):
        # Step 1: Sort intervals by their start value (manually)
        for i in range(len(intervals)):
            for j in range(i + 1, len(intervals)):
                if intervals[i][0] > intervals[j][0]:
                    intervals[i], intervals[j] = intervals[j], intervals[i]

        merged = []

        for interval in intervals:
            # If merged list is empty or current interval doesn't overlap, add it
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # Overlap → merge by updating the end time
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged