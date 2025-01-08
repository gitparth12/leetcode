class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        start = 0
        end = 1
        intervals = sorted(intervals, key=lambda x: (x[0], x[1]))
        result = []

        merge_start = intervals[0][start]
        merge_end = intervals[0][end]
        for i in range(len(intervals)):
            current = intervals[i]
            if (current[start] <= merge_end):
                merge_end = max(merge_end, current[end])
            else:
                result.append([merge_start, merge_end])
                merge_start = current[start]
                merge_end = current[end]
        result.append([merge_start, merge_end])
        return result
        
        