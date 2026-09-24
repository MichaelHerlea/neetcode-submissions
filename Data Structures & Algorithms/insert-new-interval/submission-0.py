class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []
        for start_i, end_i in intervals:
            if newInterval[0] > end_i or newInterval[1] < start_i:
                output.append([start_i, end_i])
                continue

            if newInterval[0] > start_i:
                newInterval[0] = start_i
            if newInterval[1] < end_i:
                newInterval[1] = end_i
        output.append(newInterval)
        output.sort()
        
        return output