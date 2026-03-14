class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
         #[1,6] , [2,8] , [7,12] , [10,16]
        #                   6
        
        #1...16  2...8
        points.sort(key = lambda x : x[0])

        arrow = 1
        end = points[0][1]

        for i in range(1,len(points)):
            balloon = points[i]
            if balloon[0] > end:
                arrow += 1
                end = balloon[1]
            else:
                end = min(end,balloon[1])
        return arrow



