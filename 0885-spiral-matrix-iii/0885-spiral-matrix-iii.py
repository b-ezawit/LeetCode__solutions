class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        ans = [[rStart, cStart]]
        val = 1
        
        while len(ans) < rows * cols:
            #Incrementing
            for _ in range(val):
                cStart += 1
            
                if 0<=rStart<rows and 0<=cStart<cols:
                    ans.append([rStart,cStart])
            
            for _ in range(val):
                rStart += 1
            
                if 0<=rStart<rows and 0<=cStart<cols:
                    ans.append([rStart,cStart])
            
            val += 1
            
            #Decrementing
            for _ in range(val):
                cStart -= 1
            
                if 0<=rStart<rows and 0<=cStart<cols:    
                    ans.append([rStart,cStart])
                
            for _ in range(val):
                rStart -= 1

                if 0<=rStart<rows and 0<=cStart<cols:
                    ans.append([rStart,cStart])  
            
            val += 1

        return ans