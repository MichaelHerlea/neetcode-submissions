class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        output = []
        intervals.sort()
        for i in range(len(intervals)):
            if i < len(intervals) - 1 and intervals[i][1] >= intervals[i + 1][0]:
                intervals[i + 1] = [intervals[i][0], max(intervals[i][1], intervals[i + 1][1])]
            else:
                output.append(intervals[i])
        return output