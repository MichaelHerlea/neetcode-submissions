class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        end_point = 0
        output = 0

        for i in range(len(intervals)):
            if i == 0:
                end_point = intervals[i][1]
            elif intervals[i][0] < end_point:
                output += 1
                end_point = min(end_point, intervals[i][1])
            else:
                end_point = intervals[i][1]
        
        return output