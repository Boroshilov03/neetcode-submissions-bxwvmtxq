class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda x: x[1])
        prevEnd = intervals[0][1]
        #[1, 5]
        #[2, 7]
        counter=0
        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                counter+=1
                prevEnd = min(end, prevEnd)
        return counter