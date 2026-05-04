class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        ans = [[rStart, cStart]]
        var = 1
        
        while len(ans) < rows * cols:
            for _ in range(var):
                cStart += 1
                if 0 <= rStart < rows and 0 <= cStart < cols:
                    ans.append([rStart, cStart])
            
        
            for _ in range(var):
                rStart += 1
                if 0 <= rStart < rows and 0 <= cStart < cols:
                    ans.append([rStart, cStart])
            
            var += 1 
            
            for _ in range(var):
                cStart -= 1
                if 0 <= rStart < rows and 0 <= cStart < cols:
                    ans.append([rStart, cStart])
            
            for _ in range(var):
                rStart -= 1
                if 0 <= rStart < rows and 0 <= cStart < cols:
                    ans.append([rStart, cStart])
            
            var += 1 
            
        return ans